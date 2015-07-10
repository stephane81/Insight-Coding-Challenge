import sys

def solution(file_object):
    
    file=open(file_object)
    output=[]
    for line in file:
        
        line=line.replace("\n", "")
        string=line.lstrip().rstrip()
        string2=string
        if string[0] in ['+','-']:
            string2=string2[1:]
            
        if len(string2)<11:
            testnumber=True
            runner=0
            while runner<len(string2):
                if string2[runner] not in ['0','1','2','3','4','5','6','7','8','9']:
                    testnumber=False
                runner += 1
            
            if testnumber:
                number=int(string)
                
                if number<=1000000000 :
                    print 'yes'
                    output.append(number)
    
    
    return output

