#!/bin/bash

# Note, this must be used from the directory of the CTF you're writing in!
# Example, for SpringForwardCTF 2023, first cd to that directory, then run ../addWriteups.sh
# Prompt user for category, challenge, and name
read -p "Enter category name: " category
read -p "Enter challenge name: " challenge
read -p "Enter the developer's name: " theirName
read -p "Enter your name: " name


# Create directories and ReadMe.md files
mkdir -p "$category/$challenge/$name"
touch "$category/$challenge/$name/ReadMe.md"



# Populate ReadMe.md files with basic information
echo "# $category - $challenge" > "$category/$challenge/$name/ReadMe.md"
echo "Developer: $theirName" >> "$category/$challenge/$name/ReadMe.md"
echo " " >> "$category/$challenge/$name/ReadMe.md"
echo "Author: $name" >> "$category/$challenge/$name/ReadMe.md"
echo " " >> "$category/$challenge/$name/ReadMe.md"
echo "$(date "+%Y-%m-%d")" >> "$category/$challenge/$name/ReadMe.md"

