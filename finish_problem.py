import sys
import os
import csv
import re

LANGUAGE_EXTENSIONS = {
    'cpp': ['.cpp'],
    'python': ['.py'],
    'javascript': ['.mjs'],  
    'java': ['.java']
}

def read_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError as e:
        raise Exception(f"❌ File not found: {filepath}") from e

def find_solution_file(base_path):
    for lang, exts in LANGUAGE_EXTENSIONS.items():
        for ext in exts:
            solution_path = os.path.join(base_path, f"solution{ext}")
            
            # not this one 
            if not os.path.exists(solution_path):
                continue

            files = os.listdir(base_path)
            test_file = next(f for f in files if re.match(rf"test.*{ext}$", f, re.IGNORECASE))
            #  construct full path
            test_path = os.path.join(base_path, test_file)
            
            return solution_path, test_path, lang

    return None, None, None

def bundle_problem(target_uuid, username):
    # Define paths
    base_path = target_uuid
    prompt_path = os.path.join(base_path, "prompt.md")
    
    # Find the correct solution and test files
    solution_path, test_path, lang = find_solution_file(base_path)
    
    if not solution_path:
        raise Exception(f"❌ No solution file found in supported languages")
    
    # Read contents
    prompt = read_file_content(prompt_path)
    solution = read_file_content(solution_path)
    test = read_file_content(test_path)

    # Create CSV
    output_file = os.path.join(base_path, f"{target_uuid}.csv")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        # Write header
        writer.writerow(['id', 'language', 'prompt', 'solution', 'test', 'username'])
        # Write data
        writer.writerow([target_uuid, lang, prompt, solution, test, username])
    
    print(f"✅ Bundle created: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python finish_problem.py <target_directory> [username]")
        sys.exit(1)
    
    uuid = sys.argv[1]
    
    if not os.path.exists(uuid):
        print(f"❌ Directory {uuid} not found")
        sys.exit(1)
    
    # Get username from argument or prompt
    if len(sys.argv) >= 3:
        username = sys.argv[2]
    else:
        username = input("Enter your Shipd username: ").strip()
        if not username:
            print("❌ Username cannot be empty")
            sys.exit(1)
        
    bundle_problem(uuid, username) 