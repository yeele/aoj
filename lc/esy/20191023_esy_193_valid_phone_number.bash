#!/bin/bash
# Read from the file file.txt and output all valid phone numbers to stdout.


#while read line
while read line || [ -n "${line}" ]
do
    if [[ $line =~ ^\([0-9]{3}\)[[:space:]][0-9]{3}-[0-9]{4}$ ]]; then
        echo $line
    elif [[ $line =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
        echo $line
    fi
done < file.txt

version="4.10.1"

if [[ ${version} =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
  all=${BASH_REMATCH[0]}
  major=${BASH_REMATCH[1]}
  minor=${BASH_REMATCH[2]}
  patch=${BASH_REMATCH[3]}

  echo ${all}    # 4.10.1
  echo ${major}  # 4
  echo ${minor}  # 10
  echo ${patch}  # 1
fi