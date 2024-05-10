# Hello World

\`\`\`shell
#!/bin/sh
echo "Hello world"
\`\`\`

# How does if-else in shell scripts work?
if [condition]
then
   statement1
else
   statement2
fi

# Using if-else to check whether two numbers are equal
\`\`\`shell
#!/bin/bash
a=100
b=200

if [ $n -eq $m ]
then
        echo "Both variables are the same"
else
        echo "Both variables are different"
fi
\`\`\`

# EXAMPLE - Using if-else as a simple password prompt

\`\`\`shell
#!/bin/bash
echo "Enter password"
read pass
if [ $pass="password" ]
then
  echo "The password is correct."
else
  echo "The password is incorrect, try again."
fi
\`\`\`
