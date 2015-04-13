#!/usr/bin/env python

import time
import sys

print "This program splits Amazon reviews file into individual .review files."
print "These are stored in a directory created in your current directory."
# master_file_path = raw_input("Enter master file path: ")
start_time = time.time()
print sys.argv[1]
try:
    master_file = open(sys.argv[1])
except:
    print "Invalid file:", master_file_path
    exit(0)


record_counter = 0
reviews_per_file = 100000
record_file_directory = "./reviews/"
current_record_file = open(record_file_directory +
                           str(record_counter).zfill(8) + ".review", 'w')
current_record_contents = ""

for line in master_file:
    if not line.isspace():
        if line.startswith("review/score") or line.startswith("review/text"):
            current_record_contents += line
    else:
        record_counter += 1
        if record_counter % reviews_per_file == 0:
            current_record_file.write(current_record_contents)
            current_record_file.close()
            print "%d reviews processed" % (record_counter)
            current_record_file = open(record_file_directory +
                                       str(record_counter / reviews_per_file)
                                       .zfill(8) + ".review", 'w')
            current_record_contents = ""
        else:
            current_record_contents += line

current_record_file.write(current_record_contents)
current_record_file.close()
print "%d reviews processed" % (record_counter)
print "Finished in: %s seconds" % (time.time() - start_time)
