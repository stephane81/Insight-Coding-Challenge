#!usr/bin/env python
#Stephane EGLY
# this program Calculate the median number of unique words per tweet, and update
#this median as tweets come in.
# first argument is file of tweets, second argument is median values

# It is designed to be scalable : the time complexity is O(1)

# In a real project, I would put classes in a separate file.
# the class 'listOfCountWithRunningMedian' manage a list where the index is number
# of unique words per tweet and the value is the count of how many times the number
# of unique words has already occured.
#the class 'position' define the position in that list, and allows to move in the
#list from one value to the next or previous one.  




from __future__ import division
import sys


class position:
    def __init__(self,index,rank,listOfCount) :
        self.index=index
        self.rank=rank
        self.listOfCount=listOfCount
        
    def previous(self):
    #return the previous position in the list of Counts
        if self.rank>1:
            return position( self.index , self.rank - 1,self.listOfCount ) 
        if self.rank == 1:
            runningIndex = self.index - 1;
            while ( self.listOfCount[runningIndex]==0 ):
                runningIndex -= 1
            return position( runningIndex , 1 , self.listOfCount )
                    
    def next(self):
    #return the next position in the list of Counts  
        if self.rank<self.listOfCount[self.index]:
            return position( self.index , self.rank + 1 ,self.listOfCount ) 
        if self.rank == self.listOfCount[self.index]:
            runningIndex = self.index + 1;
            while ( self.listOfCount[runningIndex]==0 ):
                runningIndex += 1
            return position( runningIndex , 1 , self.listOfCount )  


class listOfCountWithRunningMedian:
    
    def __init__(self,sizeList):
        self.listOfCount = [0]* sizeList
        self.listIsEmpty    = True
        self.sizeListIsEven = False
        self.medianOdd      = None
        self.medianEven     = None
        
    def median(self):
    #return the median number of the list
        if not self.listIsEmpty:            
            if self.sizeListIsEven:
                return ( self.medianEven1.index + self.medianEven2.index ) / 2
            else:
                return self.medianOdd.index
        
    def addNumber(self,numberToAdd):
    # add a new number in the list and update the position of the median
    
    #if the list is empty :                
        if self.listIsEmpty:
        #add the number
            self.listOfCount[numberToAdd] = 1
            self.listIsEmpty    = False
            self.sizeListIsEven = False
        #track the median
            self.medianOdd = position (numberToAdd , 1 ,self.listOfCount ) 
        else:
    #if the list is not empty
        #add the number     
            self.listOfCount[numberToAdd] += 1
            self.sizeListIsEven = not (self.sizeListIsEven)
        #track the median
            # if size list is even => return 2 values
            if self.sizeListIsEven:        
                if   numberToAdd >= self.medianOdd.index:
                    self.medianEven1 = self.medianOdd
                    self.medianEven2 = self.medianOdd.next()
                elif numberToAdd < self.medianOdd.index:
                    self.medianEven1 = self.medianOdd.previous()
                    self.medianEven2 = self.medianOdd  
            # if size list is odd => return 1 value
            else:
                if numberToAdd >= self.medianEven2.index:
                    self.medianOdd = self.medianEven2
                elif numberToAdd < self.medianEven1.index :
                    self.medianOdd = self.medianEven1
                elif numberToAdd == self.medianEven1.index :
                    self.medianOdd = self.medianEven1.next()
                elif (numberToAdd > self.medianEven1.index) and (numberToAdd < self.medianEven2.index):
                    self.medianOdd = position( numberToAdd , 1 , self.listOfCount )
   
#main part :                                                             

#manage input and output files       
fileOfTweets     = open ( sys.argv[1] )
fileMedians = open ( sys.argv[2] , 'w')

#create list of count of unique words
UniqueWordCount  = listOfCountWithRunningMedian(70) # max 140 characters =>  max 70 words 

#for each tweet of the file :
for tweet in fileOfTweets:
    
    #count number of unique words in tweet 
    words=set()
    for word in tweet.split(' '):
        if word not in words :
            words.add(word)
    numberUniqueWords = len(words)
    
    #Update the list of counts and track the median
    UniqueWordCount.addNumber(numberUniqueWords)
    
    #Print median in output file
    fileMedians.write(str(UniqueWordCount.median()) + "\n")


fileMedians.close()
fileOfTweets.close()   
    
        

        
    
        