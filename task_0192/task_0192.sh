# LeetCode #0192 | Word Frequency | [MEDIUM]

grep -oE '\b\w+\b' words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'

# (1)
# grep --> searches for patterns in text; 
# parameter -o -->  prints only the matching part;
# parameter -E --> uses extended regular expressions;
# \b --> word boundary;
# \w+ --> one or more word characters;

# (2)
# sort - sorts the output alphabetically;

# (3)
# uniq --> removes CONSECUTIVE duplicates;
# -c --> adds a count of occurrences before each unique value;

# (4)
# -n --> sorts numerically;
# -r --> reverse order sorting;

# (5)
# awk processes each line by fields (columns):
# $1 --> first column;
# $2 --> second column;
# {print $2, $1} --> swaps the order;
