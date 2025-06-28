# Shipd Pebble (a.k.a DSA II) Quest Workbook

Hey everyone. While the quest is being set up on https://shipd.ai, we will be using this repository to help everyone maximize convenience when creating + solving problems.

**Any question?** Please make sure you're in the Discord and ask them in the questions channel.

## Video

[Watch the loom video walkthrough again](https://www.loom.com/share/5b6759a285f442e49d6c59dec281fadf)

## Setup

To get started using this to create + solve DSA questions, you should run the `init.sh` command.

Note that you might need to run the commands below first:

#### Linux/MacOS:

```bash
chmod +x init.sh
```

#### Windows:

If using Git Bash or WSL, the command above should also apply.

If using PowerShell, the scripts _should_ work without modification.

You must also have Docker and Python 3.0 installed on your machine.

<br/>
<br/>
<br/>

## Starting a new problem

To start a new problem, run the following after you run the initialization script:

```bash
./start_new_question.sh <python|javascript|cpp|java>
```

This will create a new folder in this repository, and create the following files which you will need to submit:

```
prompt.md
test file (e.g. Test.java, test.solution.mjs...)
solution file (e.g. solution.cpp, solution.py...)

```

Follow the rules in the guideline (at the bottom of this README) to create a high-quality problem.

<br/>
<br/>
<br/>

## Testing a problem

Testing is made simple in this repository. As long as you follow the convention that is provided in the sample files, you can run the following command from the root directory:

```bash
./test_question.sh <target_directory> <language>
```

where `target_directory` is a UUID.

When you run this, it should show the test output using the language's built-in testing capabilities.

## Submitting a problem

When you've finished everything, run the following:

```bash
python finish_problem.py <target_directory> [username]
```

This will convert the contents inside a folder to a `csv` format.

Once you have your csv file, head over to https://tally.so/r/nW6zML and drop it in there. Remember to provide your Shipd + Discord usernames 🚀

<br/>
<br/>
<br/>
