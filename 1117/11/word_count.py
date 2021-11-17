import collections,re
with open("word_list.txt","r",encoding="utf-8") as f:
    #print(dict(collections.Counter(re.split('[ ,.()]',f.read().lower()))))
    print(dict(collections.Counter(f.read().splitlines())))