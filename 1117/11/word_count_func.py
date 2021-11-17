import collections,re
with open("sentence.txt","r") as f:
    for i,v in sorted(dict(collections.Counter(re.split('[ ,.()\n":]',f.read().lower()))).items())[1:]:
        print(f"{i:<14s} : {v}")