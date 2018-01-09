#!/usr/bin/python
import sys
filenames = ['dev', 'test', 'train']
labelDict = {'neutral':1, 'entailment':2, 'contradiction':3, '-':0}

for filename in filenames:
    print ('preprossing ' + filename + '...')
    fpr = open('/home/shyam/Downloads/MS/Sem1/NLP/Project/Data/original/snli_1.0/snli_1.0_'+filename+'.txt', 'r')
    count = 0
    fpr.readline()
    fpw = open(filename+'_s_'+'.txt', 'w')
    fpw_l  = open(filename+'_label_'+'.txt','w')
    for line in fpr:
	sentences = line.strip().split('\t')
	if sentences[0] == '-':
	   continue
	tokens = sentences[1].split(' ')
	tokens = [token for token in tokens if token != '(' and token != ')']
	fpw.write(' '.join(tokens)+'\t')
	tokens = sentences[2].split(' ')
	tokens = [token for token in tokens if token != '(' and token != ')' ]
	fpw.write(' '.join(tokens)+'\n')
	fpw_l.write(str(labelDict[sentences[0]])+'\n')
	count += 1
    fpw.close()
    fpw_l.close()
    fpr.close()
print ('SNLI preprossing finished!')
