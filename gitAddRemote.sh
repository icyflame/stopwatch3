#!/bin/bash

#this script will take the remote address from the user for the first time
#and connect the git repository to the server.

echo 'enter the url of the repository:'

read url

git remote add origin $url

echo 'push destination has been locked'
echo "run gitPush.sh to push everything to the server"

read
