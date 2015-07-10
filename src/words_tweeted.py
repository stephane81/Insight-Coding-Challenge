#!/usr/bin/env python
#Stephane EGLY
#program that calculates the total number of times each word has been tweeted.

import sys

#manage input and output files 
filenameTweetInput = sys.argv[1]
filenameWordcount  = sys.argv[2]

fileOfTweets  = open(filenameTweetInput)
fileWordcount = open(filenameWordcount,"w")


wordcount={}
# for each tweet of the file
for tweet in fileOfTweets :
    # for each word of the tweet
    for word in tweet.split() :
        #if the word as already occured then increment its count 
        if word in wordcount :
            wordcount[word] +=  1
        #or create a new count for this word
        else :
            wordcount[word]=1
            
#Print word and its number of occurences
for word in sorted(wordcount) :    
    fileWordcount.write(word + " " + str(wordcount[word]) + "\n")


fileWordcount.close()
fileOfTweets.close()
    
            
