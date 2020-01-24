#!/bin/bash
# usage
# sh leetcode_title.sh "208. Implement Trie (Prefix Tree)" medium


title=`echo $1 | sed -e 's/\.//g' | sed -e 's/?//g' `
whole_title="leetcode $2 $title"
echo $whole_title | pbcopy
echo "$whole_title (<-- pbcopied )"
echo $whole_title | sed -e 's/ /_/g' 
