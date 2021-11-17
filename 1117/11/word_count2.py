import collections,re
with open("word_list.txt","r",encoding="utf-8") as f:
    for a in [i+"  : "+str(v) for i,v in sorted(dict(collections.Counter(f.read().splitlines())).items())]:
        print (a)