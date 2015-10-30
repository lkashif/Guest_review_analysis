#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import sys

def lines(fp):
    print str(len(fp.readlines()))

def dataparse(rev_line, scores):
    
    score1 = 0
    textlist = []
    textlist = rev_line.split()
    for item in textlist:
        itemlower = item.lower()
        if itemlower in scores:
            score1 += scores[itemlower]
        else:
            score1 += 0

    return score1

def main():
    
    # run code as
    # $python test_1.py <sentiment txt file> <review CSV file>
    
    # get CSV file into Panads data frame
    df = pd.read_csv(sys.argv[2], header=None)
    sent_file = open(sys.argv[1])
    
    # parse scorefile and make dictionary of terms and corresponding scores
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    #rev_file = open(sys.argv[2])
    
    scorelist = []
    scoredict = {}
    #lines(sent_file)

# iterate over reviews and score each, saving counts of each score in a dictionary
    for i in range(df.shape[0]):
        rev_line = df[5][i]
        if type(rev_line) is not str:
            continue
        #scorelist.append(dataparse(rev_line, scores))
        score = dataparse(rev_line, scores)
        if score not in scoredict.keys():
            scoredict[score] = 1
        else:
            scoredict[score] = scoredict[score] + 1

    #pl.figure()
    pl.plot(scoredict.keys(), scoredict.values())
    #pl.hist(scoredict.keys(), scoredict.values(), bins=np.arange(min(scoredict.keys()), max(scoredict.keys()) + 5, 5))
    pl.show()

if __name__ == '__main__':
    main()
