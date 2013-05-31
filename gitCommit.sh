echo 'current status:'
echo '=================================='
echo '=================================='

git status

echo 'adding all the files in the folder'

git add .

echo '=================================='
echo '=================================='

echo "Enter the commit message:"
read commitMes

git commit -m "$commitMes"

echo '=================================='
echo '=================================='
echo 'the changes have been comitted:'
echo '=================================='
echo '=================================='
git log

echo '=================================='
echo '=================================='
echo
echo 'press the return key to exit'
read
read
