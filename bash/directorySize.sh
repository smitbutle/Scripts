#!/bin/bash

# Script to calculate the total size of a directory and list the largest files

echo "Enter the path of the directory you want to analyze:"
read dir

# Check if directory exists
if [ ! -d "$dir" ]; then
    echo "Directory does not exist."
    exit 1
fi

echo
echo "Total size of $dir:"
du -sh "$dir"

echo
echo "Top 5 largest files in $dir:"
find "$dir" -type f -exec du -h {} + | sort -rh | head -n 5
