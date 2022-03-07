# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:46:17 2022

Email Validator

@author: Damian.M
"""

import re

strRegex = '^\w+([\.-]?\w+)*\w([\.-]?\w+)*(\.w{2,3})+$=&'
strSourceDataFileName = r"C:\Users\HomeInNature\Desktop\python_kurs-master\Data_Process\email-sample.txt"
strValidDataFileName = r"C:\Users\HomeInNature\Desktop\python_kurs-master\Data_Process\ValidEmailData.txt"
strInvalidDataFileName = r"C:\Users\HomeInNature\Desktop\python_kurs-master\Data_Process\InvalidEmailData.txt"


#Open files for Writing

objValidDataStream = open(strValidDataFileName, 'w')
objInvalidDataStream = open(strInvalidDataFileName, 'w')

#Read a line of text from the source txt file
objSourceDataStream = open(strSourceDataFileName, 'r')
 
strHeaderRow = objSourceDataStream.readline()
objValidDataStream.write(strHeaderRow)
objInvalidDataStream.write(strHeaderRow)

#Read all the other lines of text from the source file
for strLine in objSourceDataStream:
    if (re.search(strRegex,strLine)):
        print("Valid")
        objValidDataStream.write(strLine)
    else:
        print("Invalid")
        objInvalidDataStream.write(strLine)
        
objSourceDataStream.close()
objValidDataStream.close()
objInvalidDataStream.close()
