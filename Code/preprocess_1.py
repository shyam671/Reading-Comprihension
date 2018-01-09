#!/usr/bin/python
import sys
filenames = ['dev', 'test', 'train']
labelDict = {'neutral':1, 'entailment':2, 'contradiction':3, '-':0}

for filename in filenames:
    print ('preprossing ' + filename + '...')
    fpr = open('snli_1.0/snli_1.0/snli_1.0_'+filename+'.txt', 'r')
    count = 0
    fpr.readline()
    fpw_s1 = open(filename+'_s1_'+'.txt', 'w')
    fpw_s2 = open(filename+'_s2_'+ '.txt','w')
    fpw_l  = open(filename+'_label_'+'.txt','w')
    for line in fpr:
	sentences = line.strip().split('\t')
	if sentences[0] == '-':
	   continue
	tokens = sentences[1].split(' ')
	tokens = [token for token in tokens if token != '(' and token != ')']
	fpw_s1.write(' '.join(tokens)+'\n')
	tokens = sentences[2].split(' ')
	tokens = [token for token in tokens if token != '(' and token != ')' ]
	fpw_s2.write(' '.join(tokens)+'\n')
	fpw_l.write(str(labelDict[sentences[0]])+'\n')
	count += 1
    fpw_s1.close()
    fpw_s2.close()
    fpw_l.close()
    fpr.close()
print ('SNLI preprossing finished!')
