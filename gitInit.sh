#!/bin/bash

#written by Siddharth Kannan

#this script will initialise(or reinitialise) a git repository and add the readme file.

echo 'initialising a git repository:'
echo
git init

echo 'created the readme file:'
touch readme

echo 
echo 'enter the contents of the readme file:'
read contentsOfReadme

echo "$contentsOfReadme" > readme

git add .

echo
echo
echo 'all the files added to repo'
echo '=================================='
echo '=================================='
echo 'current status:'
echo
echo
echo

git status

echo '=================================='
echo '=================================='

echo "Enter the commit message:"
read commitMes

git commit -m "$commitMes"

echo 'The log for this git repo is as so:'
echo
echo
echo '=================================='
echo '=================================='
git log

echo '=================================='
echo '=================================='
echo 'Changes comitted to the git repository'
echo 'Press return key to exit'
read



