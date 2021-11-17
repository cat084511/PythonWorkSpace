import collections,re
with open("word_list.txt","r",encoding="utf-8") as f:
    #print("{"+str(collections.Counter(re.split('[ ,.()]',f.read().lower())))[17:][:-1])
    print(dict(collections.Counter(f.read().splitlines())))