#!/bin/bash

echo "Who are you?"
read -p "Enter username: " username
read -s -p "Enter password: " password

if [ "$password" == "Kingvadee" ]; then
    echo "Welcome, $username"

    read -p "Do you want to add a file? (yes/no): " add_file

    if [ "$add_file" == "yes" ]; then
        read -p "Enter file name: " file_name
        read -p "Enter commit message: " commit_message

        git add "$file_name"
        git commit -m "$commit_message"
        git push

        if [ $? -eq 0 ]; then
            echo "File successfully pushed to the repository."
        else
            echo "Error: Unable to push the file."
        fi
    else
        echo "No file added."
    fi
else
    echo "Incorrect password"
fi

