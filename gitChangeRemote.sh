#!/bin/bash

#this script will take the remote address from
#the user and overwrite the old stored address
#and connect the git repository to the server.

echo "note that in case this repository was linked with some other push destination, that destination will be overwritten and this new destination will become effective. Are you sure that's what you want to do?"
echo

echo 'if that is not what you want to do, then exit this script now.'
echo

echo 'otherwise you can continue:'
echo
echo

echo 'enter the url of the repository:'

read url

git remote set-url origin $url

echo "run gitPush.sh to push everything to the server"

read
