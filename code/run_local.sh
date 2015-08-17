#!/bin/sh

if [ $# -lt 1 ]; then
  echo "No source path provided"
  echo "Use: $0 <source directory> [<filename pattern>]"
  echo "Sample: $0 reviews *18* # use all files in reviews/ with an 18 in the filename"
  exit 0
fi

# use provided pattern if given; else: use all files
if [ $# -gt 1 ]; then
  SOURCE_PATTERN=$2
else
  SOURCE_PATTERN="*"
fi

SOURCE_DIR=$1

# get document count
DOCUMENT_COUNT="$(ls $SOURCE_DIR/$SOURCE_PATTERN -1 | wc -l)"

# run it
cat $SOURCE_DIR/$SOURCE_PATTERN | ./src/mapper.py | sort -k1,1 | ./src/reducer.py $DOCUMENT_COUNT
