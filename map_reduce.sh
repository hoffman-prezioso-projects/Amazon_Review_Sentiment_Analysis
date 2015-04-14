OUTPUT_DIR="output"

date

echo "Creating crawl directory..."
hadoop fs -mkdir crawl > /dev/null 2>&1

date

echo "Creating reviews directory..."
hadoop fs -mkdir crawl/reviews > /dev/null 2>&1
hadoop fs -rm crawl/reviews/* > /dev/null 2>&1

date

echo "Removing previous output..."
hadoop fs -rm -r crawl/$OUTPUT_DIR > /dev/null 2>&1

date

echo "Copying reviews..."
hadoop dfs -copyFromLocal reviews crawl > /dev/null 2>&1
echo "Copy complete!"

date

echo "Running mapReduce..."
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar \
-files src/mapper.py \
-files src/reducer.py \
-files src/spell_checker.py \
-files src/en_dictionary.txt \
-mapper src/mapper.py \
-reducer src/reducer.py \
-input crawl/reviews/* \
-output crawl/$OUTPUT_DIR
echo "mapReduce complete!"

date

# create local output directory
if [ ! -d $OUTPUT_DIR ]; then
	mkdir $OUTPUT_DIR
else
	rm -f $OUTPUT_DIR/*
fi

echo "Creating output directory"
hadoop dfs -copyToLocal crawl/$OUTPUT_DIR ./

date