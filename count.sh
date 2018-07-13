#!/bin/bash
cd ../js
for file in `find . -type f -name "*.js"`
do
echo "$file"
wc -l < "$file"
wc -c < "$file"
done