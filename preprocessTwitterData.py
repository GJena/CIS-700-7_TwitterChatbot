from collections import Counter
import json
import itertools
import random

# filepath = "twitter_en.txt"
# f = open(filepath,"r")
# text = f.read()
# lines = text.split("\n")

# f1 = open("dialog1.txt",'w')
# f2 = open("dialog2.txt",'w')
# f3 = open("testdialog1.txt",'w')
# f4 = open("testdialog2.txt",'w')

# l = len(lines)/2
# crossvalSize = int(0.1*l)
# crossValInd =  set(random.sample(range(1, l), crossvalSize))
 
# for i in range(l):
# 	if i in crossValInd:
# 		f3.write(lines[i*2] +"\n")
# 		f4.write(lines[(i*2)+1] +"\n")		
# 	else:
# 		f1.write(lines[i*2] +"\n")
# 		f2.write(lines[(i*2)+1] +"\n")		

# f1.close()
# f2.close()
# f3.close()
# f4.close()


#check vocab
'''
dialog1: 251349, 155034 words occured only once  (96315)
dialog2: 229596, 150589 words occured only once  (79007)
'''

filepath = "data/dialog2.txt"
f = open(filepath,"r")
text = f.read().split()
wordCount = Counter(text)
print len(wordCount.keys())
print [(k, len(list(v))) for k, v in itertools.groupby(sorted(wordCount.values()))]

# f1 = open("dialog2_words.json",'w')
# json.dump(wordCount, f1)
