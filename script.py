import os
from collections import Counter

data_dir = '/Users/rahul/Desktop/docker_files'
result_file = '/Users/rahul/Desktop/docker_files'

# List name of all the text files at location: /home/data
files = os.listdir(data_dir)
print('List of files:', files)

# Read the two text files and count total number of words in each text file
if_file = os.path.join(data_dir, 'IF.txt')
limerick_file = os.path.join(data_dir, 'Limerick.txt')

if_words = open(if_file).read().split()
limerick_words = open(limerick_file).read().split()

if_word_count = len(if_words)
limerick_word_count = len(limerick_words)

print('IF.txt word count:', if_word_count)
print('Limerick.txt word count:', limerick_word_count)

# Add all the number of words to find the grand total (total number of words in both files)
total_word_count = if_word_count + limerick_word_count
print('Total word count:', total_word_count)

# List the top 3 words with maximum number of counts in IF.txt. Include the word counts for the top 3 words.
if_word_counts = Counter(if_words)
top_words = if_word_counts.most_common(3)
print('Top 3 words in IF.txt:', top_words)

# Find the IP address of your machine
ip_address = os.popen('hostname -I').read().strip()
print('IP address:', ip_address)

# Write all the output to a text file at location: /home/output/result.txt (inside your container)
with open(result_file, 'w') as f:
    f.write('List of files: {}\n'.format(files))
    f.write('IF.txt word count: {}\n'.format(if_word_count))
    f.write('Limerick.txt word count: {}\n'.format(limerick_word_count))
    f.write('Total word count: {}\n'.format(total_word_count))
    f.write('Top 3 words in IF.txt: {}\n'.format(top_words))
    f.write('IP address: {}\n'.format(ip_address))

print('Output written to', result_file)
