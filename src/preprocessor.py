#!/usr/bin/env python

import time

print "This program splits the Amazon reviews file into individual .review files."
print "These reviews are stored in a reviews directory created in your current directory."
master_file_path = raw_input("Enter master file path: ")
start_time = time.time()

try:
	master_file = open(master_file_path)
except:
	print "Invalid file:", master_file_path
	exit(0)


record_counter = 0
record_file_directory = "./reviews/"
current_record_file = open(record_file_directory + str(record_counter).zfill(5) + ".review", 'w')
current_record_contents = ""

for line in master_file:
	if not line.isspace():
		current_record_contents += line
	else:
		current_record_file.write(current_record_contents)
		current_record_file.close()
		record_counter += 1
		current_record_file = open(record_file_directory + str(record_counter).zfill(5) + ".review", 'w')
		current_record_contents = ""

print "Finished in: %s seconds" % (time.time() - start_time)
