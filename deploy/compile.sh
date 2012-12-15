#! /bin/bash
# Script to convert all the .txt files to .js arrays

#cd ../lists/denverpost/
cd /home/joe/work/heads/lists/denverpost/

for i in `ls *.txt`; 
do 
  # Get the first part of the file name
  slug=(`echo $i | tr '.' ' '`)
  echo $slug "= array(" > $slug.js
  for line in `cat $i`; do
    echo "\"$line\"," >> $slug.js
  done
  echo ");" >> $slug.js
done
