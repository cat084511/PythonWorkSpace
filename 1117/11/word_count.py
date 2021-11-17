import collections
with open("word_list.txt","r") as f:
    print(dict(collections.Counter(f.read().splitlines())))