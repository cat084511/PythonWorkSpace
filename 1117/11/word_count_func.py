import collections,re
with open("sentence.txt","r",encoding="utf-8") as f:
    for i,v in sorted(dict(collections.Counter(re.split('[ ,.()\n":]',f.read().lower()))).items())[1:]:
        print(i," :",v)