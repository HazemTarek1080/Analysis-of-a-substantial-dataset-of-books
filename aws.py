import pandas as pd
from collections import Counter
import time

start_time = time.time()  # Record the start time

tag_counter = Counter()  # Initialize a Counter to keep track of number of tags

chunk_size = 200
for chunk in pd.read_json('list.json', lines=True, chunksize = chunk_size): # read the list.json file in chunks
    for _, row in chunk.iterrows():                                         # Iterate over DataFrame rows as (index, Series) pairs, we use "_" to ignore the indexes
        tags = row['tags']                                                  # extract tags and check if it's a list of values
        if isinstance(tags, list):                                        
            tag_counter.update(tags)                                        # update the counter of each tag contained in the tags list

# Find the top 5 most common tags
top5_tags = tag_counter.most_common(5)
top5_tags_df = pd.DataFrame(top5_tags, columns=['tag', '#usage'])   # Create dataframe with the 5 most common tags

end_time = time.time()  # Record the end time
execution_time = end_time - start_time  # Calculate the elapsed time
print(top5_tags_df)
print('The execution time is', execution_time, 'seconds')


    

