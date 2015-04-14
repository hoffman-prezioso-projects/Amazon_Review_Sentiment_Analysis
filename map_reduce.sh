OUTPUT_DIR="output"

echo "Creating crawl directory..."
hadoop fs -mkdir crawl > /dev/null 2>&1

echo "Creating reviews directory..."
hadoop fs -mkdir crawl/reviews > /dev/null 2>&1
hadoop fs -rm crawl/reviews/* > /dev/null 2>&1

echo "Removing previous output..."
hadoop fs -rm -r crawl/$OUTPUT_DIR > /dev/null 2>&1

echo "Copying reviews..."
hadoop dfs -copyFromLocal reviews crawl > /dev/null 2>&1
echo "Copy complete!"

echo "Running mapReduce..."
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar \
-file src/mapper.py \
-mapper src/mapper.py \
-file src/average_reducer.py \
-reducer src/average_reducer.py \
-input crawl/reviews/* \
-output crawl/$OUTPUT_DIR
echo "mapReduce complete!"

# create local output directory
if [ ! -d $OUTPUT_DIR ]; then
	mkdir $OUTPUT_DIR
else
	rm -f $OUTPUT_DIR/*
fi

echo "Creating output directory"
hadoop dfs -copyToLocal crawl/$OUTPUT_DIR ./