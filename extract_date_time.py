#161101014,Yasar Can Kakdas,BIL334

import re
import sys


x=sys.argv.pop()
file=open(x[:-4]+'_date-time.txt','w')

for line in open(x) :
    s=re.findall(r'(?:[0-9][0-9]|[1-9]).(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).'
                 r'(?:19|20)[0-9][0-9].\d{2}.\d{2}.\d{2}',line)
    if(len(s)!=0):
        str=s.pop()
        index=str.index(':')
        if(str[1]!='/'):
            if(int(str[:2])<=31 ):
                correct=True
            else :
                correct=False
        if(str[1]=='/'):
            file.write('0'+str[:index]+'   '+str[index+1:]+'\n')
        elif(str[1]!='/' ) :
            if(correct):
                file.write(str[:index] + '   ' + str[index + 1:] + '\n')







