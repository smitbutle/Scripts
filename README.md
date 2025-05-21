# Shell Script Basics: Hello World and If-Else Examples

This README provides simple examples and explanations for basic shell scripting concepts, including printing "Hello World", using `if-else` statements, comparing variables, and a simple password prompt. It also includes a practical script (`directorySize.sh`) to analyze directory sizes and find large files.

---

## Hello World Example

A basic shell script to print "Hello world" to the terminal.

```shell
#!/bin/sh
echo "Hello world"
```

**Usage:**
1. Save the script as `hello.sh`.
2. Make it executable: `chmod +x hello.sh`
3. Run it: `./hello.sh`

---

## If-Else in Shell Scripts

Shell scripts use `if-else` statements for conditional logic.

```shell
if [ condition ]
then
   statement1
else
   statement2
fi
```

---

## Example: Check if Two Numbers are Equal

This script checks if two numbers are equal.

```shell
#!/bin/bash
a=100
b=200

if [ $a -eq $b ]
then
    echo "Both variables are the same"
else
    echo "Both variables are different"
fi
```

---

## Example: Simple Password Prompt

A script that prompts the user to enter a password and checks if it matches a set value.

```shell
#!/bin/bash
echo "Enter password"
read pass
if [ "$pass" = "password" ]
then
  echo "The password is correct."
else
  echo "The password is incorrect, try again."
fi
```

**Note:**  
- Always quote variables in test conditions (e.g., `"$pass"`).
- Use `=` for string comparison, and `-eq` for numeric comparison in `[` ... `]`.

---

## 🛠️ Tips

- Start your shell scripts with the appropriate shebang (`#!/bin/sh` or `#!/bin/bash`).
- Always make scripts executable with `chmod +x scriptname.sh`.
- For more complex scripts, consider adding comments and input validation.

---

# Usage Guide: directorySize.sh

This script helps you quickly check the total size of a directory and find the top 5 largest files within it.

## How to Use

1. **Save the Script:**
   - Copy the script into a file named `directorySize.sh`.

2. **Make the Script Executable:**
   ```bash
   chmod +x directorySize.sh
   ```

3. **Run the Script:**
   ```bash
   ./directorySize.sh
   ```

4. **Follow the Prompt:**
   - When prompted, enter the full path of the directory you wish to analyze (e.g., `/home/username/Documents`).

## Example

```shell
$ ./directorySize.sh
Enter the path of the directory you want to analyze:
/home/hks/Streamlit_fort

Total size of /home/hks/Streamlit_fort:
228K    /home/hks/Streamlit_fort

Top 5 largest files in /home/hks/Streamlit_fort:
12K     /home/hks/Streamlit_fort/app.py
8.0K    /home/hks/Streamlit_fort/vgg16_model.py
8.0K    /home/hks/Streamlit_fort/se_resnext50_32x4d_model.py
8.0K    /home/hks/Streamlit_fort/se_resnet50_model.py
8.0K    /home/hks/Streamlit_fort/segformer_model.py
```

##  Notes

- Make sure you have permission to read the directory you want to analyze.
- The script works recursively, so it includes files in all subdirectories.
- The results will help you quickly identify which files take up the most space.

---
