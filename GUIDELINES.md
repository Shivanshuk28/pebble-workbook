# 🚀 Shipd Pebble Quest Guidelines

> **💡 Quality First:** Creating exceptional problems takes time. We'd rather see one outstanding problem than five mediocre ones.

Welcome to the Pebble Quest! This guide will help you create high-quality, creative DSA problems that meet our standards. Please read this thoroughly before your first attempt, and keep it handy as a reference while creating problems.

At Shipd, we prioritize quality over speed. If a problem doesn't meet our standards, reviewers will send it back for revisions. We cannot accept problems or process payments until they have been revised based on feedback to meet the quality bar.

<br/>

## ⚠️ AI Usage Policy

**Absolutely no AI assistance is allowed for any part of problem creation.** This includes but is not limited to:

- Generating problem ideas or descriptions
- Writing solution code
- Creating test cases
- Reviewing or editing your work

**Detection of AI usage will result in immediate removal from the quest and forfeiture of all pending payments.** We have sophisticated detection methods and will be monitoring submissions closely.

This policy exists because:

- We need genuinely original human creativity
- AI-generated problems lack the quality and originality we require
- Using AI undermines the entire purpose of the quest

All work must be your own original creation. No exceptions.

---

## 🎨 What is the Task?

### Your Mission

You'll be creating **original Data Structures & Algorithms (DSA) problems** that developers will solve as coding challenges. Each problem is a self-contained programming puzzle that has clear requirements, comprehensive tests, and above all, is **creative and unique from anything online.**

### What You'll Deliver

For each problem, you'll create **three files**:

- `prompt.md` - Your problem description written as a **language-native docstring**
- `solution.{ext}` - Your complete solution in your chosen language
- `test_solution.{ext}` - Your comprehensive test suite written as module code

These files will be automatically processed by our system, so naming conventions must be followed exactly.

### Expected Problem Structure

Example of a problem description (written as a docstring, not a LeetCode-style problem):

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

/**
 * Determines if a positive integer is a mirror number.
 *
 * A mirror number is a number where if certain digits are replaced with their mirror number,
 * you get the same number when viewed upside down.
 *
 * Valid mirror pairs are: 0->0, 1->1, 6->9, 8->8, 9->6
 *
 * @param n - Input number (1 ≤ n ≤ 10000)
 * @return True if n is a mirror number, false otherwise
 *
 * Example:
 * isMirrorNumber(619)
 * // returns True, because when turned upside down 619 becomes 916, which is valid
 *
 * isMirrorNumber(123)
 * // returns False
 */
bool isMirrorNumber(int n) {
...
```

<br/>

## 💡 Originality Requirements

### The Heart of Pebble Quest

Originality is the most important aspect of our entire quest. We're building a collection of unique, creative problems that developers haven't encountered before. This means every problem must be genuinely novel - not a variation of existing challenges found elsewhere.

### What Makes a Problem Original

**✨ Unique Problem Concepts**  
Create completely new problems that haven't been explored before. For example, 'calculate euclidean distance between point A and B' is too common. But you can introduce one extra step:

> Calculate the euclidean distance between the optimal roasting points (global maxima) of two coffee bean temperature profiles represented as 2D coordinate grids.

**✨ Novel Constraint Combinations**  
Take familiar concepts and add unexpected twists through creative constraints. Perhaps integers can only be prime numbers, or array operations must maintain palindrome properties. The key is combining restrictions in ways that create genuinely new challenges.

### Avoiding Common Pitfalls

You must avoid any problems that resemble existing challenges from:

- **Competitive Programming Sites:** LeetCode, HackerRank, CodeForces, TopCoder
- **Academic Sources:** Textbook exercises, course assignments, tutorial problems
- **Common Patterns:** Standard interview questions, Stack Overflow discussions

If our reviewers find multiple instances of plagiarism, you may be removed from the quest and your pending review contributions will not be paid out.

Remember, even heavily modifying an existing problem isn't enough - we need completely original concepts.

<br/>

## 🎯 Difficulty Levels

### Understanding Our Difficulty Scale

We use a three-level difficulty system that's intentionally calibrated to be more approachable than typical technical interview questions. Each level has specific time targets and complexity expectations:

| Level       | Time Target  | Complexity         | Typical Implementation        |
| ----------- | ------------ | ------------------ | ----------------------------- |
| **Level 1** | < 5 minutes  | Trivial operations | Often one-line solutions      |
| **Level 2** | < 12 minutes | Multi-step logic   | Harder end of LeetCode Easy   |
| **Level 3** | < 30 minutes | Algorithm required | Easier end of LeetCode Medium |

### Important Difficulty Guidelines

When designing problems, remember that these are meant to be significantly easier than your typical LeetCode challenge. The goal is to create **unique and creative problems that the internet has never seen**, rather than problems that require extensive algorithmic knowledge.

Don't overcomplicate your problems. A Level 3 problem should still be solvable by a junior developer within 30 minutes. If you find yourself creating something that would take more than 30 minutes, you've gone way over the difficulty bar.

Feel free to ask your fellow developers in the Discord channel! You can post it in the #general channel and openly call out for help

Always test your timing estimates with developers who haven't seen the problem before. What seems obvious to you as the creator might take others longer to understand and implement.

> **📊 Difficulty Level Examples:**
>
> - **Level 1:**

```
def get_linux_file_perm_from_octet(user: int, group: int, others: int) -> str:
    """
    Converts three numeric octets (0-7) representing user, group, and others permissions to a Linux file permission string.

    Args:
        user (int): The numeric octet representing user permissions (0-7).
        group (int): The numeric octet representing group permissions (0-7).
        others (int): The numeric octet representing others permissions (0-7).

    Returns:
        str: The Linux file permission string (e.g., 'rwxr-xr--').

    Examples:
        >>> GetLinuxFilePermFromOctet(7, 5, 4)
        'rwxr-xr--'

        >>> GetLinuxFilePermFromOctet(4, 4, 4)
        'r--r--r--'
    """
```

> - **Level 2:**

```
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

/**
 * Given a positive integer n, determine if it is a mirror number.
 *
 * A mirror number is a number where if you replace certain digits with their mirror image,
 * you get the same number when viewed upside down.
 * Valid mirror pairs are: 0->0, 1->1, 6->9, 8->8, 9->6
 *
 * @param n - Input number (1 ≤ n ≤ 10000)
 * @return True if n is a mirror number, false otherwise
 *
 * Example:
 * isMirrorNumber(619)
 * // result is True, because when turned upside down 619 becomes 916, which is valid
 *
 * isMirrorNumber(123)
 * // result if False
 */
bool isMirrorNumber(int n) {
```

> - **Level 3:**

```
def give_sweets(happiness: List[List[int]]) -> int:
    """
    Implements a distributing sweets algorithm in a neighborhood with M different types of sweets and N houses.
    The algorithm follows these rules:

    1. Gives exactly one sweet to each house
    2. Adjacent houses cannot receive the same type of sweet (e.g., if house 0 gets sweet type 2, house 1 cannot get sweet type 2)
    3. The goal is to minimize the total happiness (sum of happiness values) across all houses

    Args:
        happiness (List[List[int]]): A MxN matrix where happiness[i][j] indicates the happiness of house i after getting sweet type j

    Returns:
        int: The minimum possible total happiness achievable. If the matrix is empty, returns 0.

    Raises:
        ValueError: If any happiness value is negative or the matrix has an incorrect format.

    Examples:

        >>> give_sweets([[1, 5, 3], [2, 9, 4]])
        5
        Explanation: Give sweet type 0 to house 0 (happiness 1) and sweet type 2 to house 1 (happiness 4). Total: 1+4=5.

        >>> give_sweets([[3, 1, 2]])
        1
        Explanation: Give sweet type 1 to house 0 (happiness 1). Total: 1.
    """
```

---

## ✍️ Writing Clear Prompts

### The Golden Rule of Clarity

Every prompt must pass this test: "Could a junior developer solve this problem with ONLY the prompt and test cases?" This means your problem description must be completely self-contained, with no ambiguity or hidden requirements.

### Docstring Style Writing

**Write as a function docstring, NOT as a LeetCode-style problem.** Your description should explain what the function does, not present it as a challenge to solve. Think of it as documentation for a function that already exists.

**Examples:**

❌ **Wrong (LeetCode style):** "Given an array of integers, find the maximum sum..."

✅ **Correct (Docstring style):** "Calculates the maximum sum of a contiguous subarray within the given array."

### Essential Prompt Components

**1. Function Purpose (1-2 sentences)**  
Clearly state what the function does. You can optionally include minimal context, but keep it brief and focus on functionality.

**2. Parameters and Return Value**

- Clearly define all input parameters with types and constraints
- Specify the return type and what it represents
- Include any validation requirements

**3. Comprehensive Examples**  
Provide 2-3 examples that demonstrate different aspects of the function. Each example must include:

- The exact input parameters
- The expected return value
- A brief explanation of the logic

These examples should be actual test cases from your test suite.

### Common Clarity Mistakes to Avoid

- Never assume "obvious" behavior - state everything explicitly
- Don't use ambiguous phrases like "process appropriately"
- Avoid technical jargon without definition
- Ensure examples cover edge cases mentioned in requirements

## 💻 Writing Your Solution

### Solution Quality Requirements

Your solution must represent the **optimal approach** to solving the problem. This means:

- Use the most efficient algorithm available (best time/space complexity)
- Avoid brute force approaches unless that's genuinely optimal
- Consider edge cases and handle them efficiently
- Write clean, readable code that demonstrates best practices

### Code Structure and Formatting

**Your solution code must continue directly from the problem description.** The problem description defines the function signature, and your solution provides the implementation body.

Here's exactly how this should work:

**Problem Description (prompt.md):**

```javascript
/**
 * Count and return all valid (a, b) pairs such that n = a / b.
 *
 * A valid pair must satisfy:
 * - l <= a <= r
 * - l <= b <= r
 * - a / b == n
 *
 * @param n The target ratio (a divided by b).
 * 1 <= n <= 1e6
 *
 * @param l The lower bound for both a and b.
 * @param r The upper bound for both a and b.
 * 1 <= l <= r <= 1e5
 *
 * @return A struct or object containing:
 * - count: total number of valid pairs
 * - pairs: list of all valid (a, b) pairs
 *
 * Examples:
 * countValidPairs(2, 1, 10)
 * // returns { count: 5, pairs: {{2, 1}, {4, 2}, {6, 3}, {8, 4}, {10, 5}} }
 *
 * countValidPairs(3, 2, 5)
 * // returns { count: 0, pairs: {} }
 *
 */
function countValidPairs(n, l, r) {
```

**Solution Code (solution.js):**

```javascript
  const pairs = [];
  for (let b = l; b <= r; b++) {
    const a = n * b;
    if (a >= l && a <= r) {
      pairs.push([a, b]);
    }
  }
  return {
    count: pairs.length,
    pairs: pairs
  };
}
```

Notice how the solution continues seamlessly from where the problem description left off - no repeated function signature, no duplicate imports, just the implementation body.

### Comment Guidelines

**Avoid low-value comments that don't explain anything meaningful.** Most of your code should be self-explanatory. Only add comments when:

- Explaining complex algorithms or non-obvious logic
- Clarifying why a particular approach was chosen
- Documenting important edge case handling

**Examples:**

❌ **Bad comments (don't do this):**

```python
# Loop through the array
for i in range(len(arr)):
    # Add element to result
    result.append(arr[i])
```

✅ **Good comments (when actually needed):**

```python
# Use two pointers to avoid O(n²) nested loop
left, right = 0, len(arr) - 1

# Handle edge case where target might not exist
if not arr or target < arr[0]:
    return -1
```

**In most cases, your code should require no comments at all.**

### Solution File Requirements

Your complete solution file should:

1. Include all necessary imports at the top (if any)
2. Contain the complete function implementation
3. Be executable as a standalone module
4. Handle all edge cases mentioned in the problem description
5. Use the optimal algorithm for the problem constraints

---

## 🧪 Testing Requirements

### Testing Philosophy

All tests must use only the native testing capabilities built into each language. We explicitly prohibit external testing frameworks to maintain simplicity and ensure consistent execution across our platform.

### Test Code Structure

**Write tests as direct module code, not as separate test functions.** Your test file should contain a series of function calls with assertions, as if the tests were part of the main module.

### Language-Specific Testing Methods

| Language      | Testing Method       |
| ------------- | -------------------- |
| 🐍 Python     | `assert` statements  |
| 🟨 JavaScript | `node:assert` module |
| ☕ Java       | `assert` keyword     |
| ⚡ C++        | `assert` macro       |

### Test Structure Example

Here's how your test file should be structured. This example is in Java:

```java
// Example Java test structure
int result1 = totalCost(3, 4, 2);
int expected1 = 24;
if (result1 != expected1) {
    System.out.println("Test 1 FAILED");
    System.out.println("Expected: " + expected1);
    System.out.println("Actual  : " + result1);
}
assert result1 == expected1;

int result2 = totalCost(5, 5, 3);
int expected2 = 75;
if (result2 != expected2) {
    System.out.println("Test 2 FAILED");
    System.out.println("Expected: " + expected2);
    System.out.println("Actual  : " + result2);
}
assert result2 == expected2;

int result3 = totalCost(2, 6, 1);
int expected3 = 12;
if (result3 != expected3) {
    System.out.println("Test 3 FAILED");
    System.out.println("Expected: " + expected3);
    System.out.println("Actual  : " + result3);
}
assert result3 == expected3;

int result4 = totalCost(4, 4, 5);
int expected4 = 80;
if (result4 != expected4) {
    System.out.println("Test 4 FAILED");
    System.out.println("Expected: " + expected4);
    System.out.println("Actual  : " + result4);
}
assert result4 == expected4;
```

### Comprehensive Test Coverage

Your test suite must contain between 6 and 10 tests total, distributed across three categories:

**1. Basic Functionality Tests (2-3 tests)**  
These verify that your solution correctly handles typical inputs and produces expected outputs.

**2. Edge Case Tests (1-3 tests)**  
Test boundary conditions such as empty inputs, single elements, or maximum/minimum values.

**3. Performance Tests (2+ tests)**  
Use large inputs that differentiate O(n) from O(n²) solutions and fail brute force approaches.

### Performance Requirements

The entire test suite must complete within 5 seconds. Individual tests should generally complete in under 1 second.

---

## 🎁 Best Practices for Success

### Creating Clear Problems

**Focus on Clarity Above All**  
The most important aspect is that your problem is crystal clear and unambiguous. Avoid unnecessary complexity or confusing descriptions.

**Keep It Simple**  
Don't overcomplicate the problem statement. A clear, straightforward problem is better than a convoluted one with unnecessary narrative.

**Define Every Constraint Explicitly**  
Never leave behavior undefined. Specify exactly what should happen in all edge cases.

### AI Usage

**All work must be 100% your own creation.** This quest is designed to showcase human creativity and problem-solving skills. Any attempt to use AI assistance or copy existing problems will result in immediate disqualification.

### Pre-Submission Quality Check

Before submitting any problem, honestly evaluate it against these criteria:

✅ **Clarity Test:** Could someone solve this without asking any clarifying questions? Are all requirements explicit?

✅ **Originality Test:** Have I searched thoroughly to ensure this problem doesn't exist elsewhere? Is the concept truly novel?

✅ **Solution Quality:** Is my solution optimal? Does it demonstrate best practices?

✅ **Test Coverage:** Do my tests catch all common mistakes? Would they reject inefficient solutions?

✅ **Performance Test:** Do my performance tests actually differentiate between good and bad time complexity?

Remember, quality over quantity! Having problems that pass on the first try will maximize the speed at which we get through your problems!
