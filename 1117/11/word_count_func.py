import collections,re
with open("word_list.txt","r",encoding="utf-8") as f:
    for i,v in dict(collections.Counter(re.split('[ ,.()\n"]',f.read().lower()))).items():
        print(i," :",v)