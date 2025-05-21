# Shell Script Basics: Hello World and If-Else Examples

This README provides simple examples and explanations for basic shell scripting concepts, including printing "Hello World", using `if-else` statements, comparing variables, and a simple password prompt.

---

##  Hello World Example

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

##  If-Else in Shell Scripts

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

##  Example: Check if Two Numbers are Equal

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

##  Example: Simple Password Prompt

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

##  Tips

- Start your shell scripts with the appropriate shebang (`#!/bin/sh` or `#!/bin/bash`).
- Always make scripts executable with `chmod +x scriptname.sh`.
- For more complex scripts, consider adding comments and input validation.

---
