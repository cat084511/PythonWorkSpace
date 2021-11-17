import collections
with open("word_list.txt","r") as f:
    for i,v in sorted(dict(collections.Counter(f.read().splitlines())).items()):
        print (i," :",v)