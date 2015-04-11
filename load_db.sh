#!/bin/sh

if [ $# -ne 1 ]; then
  echo "No data file provided"
	echo "Use: $0 <data filename>"
	exit 0
fi

DATABASE="sentiment.db"
TABLE="data"

sqlite3 $DATABASE <<EOS

DROP TABLE IF EXISTS $TABLE;
CREATE TABLE $TABLE (word TEXT, rating REAL, occurrences INTEGER);

.mode csv
.separator "\t"
.import $1 $TABLE

EOS
