"""We want to first have a prompt where it ask for the person's ID
If the ID is not in the data base that means they have clokced in
if they are in the database they have clocked out that means the are clocking out.

We also want to create a way to time stamp the exact time to the millisecond

We want to store the data in a txt file

Everyday the data base should start with a new list

%TODO We will need a database file
%TODO We will need a timestamp file
"""

from TimeStamp import *
from DataBase import *
keepgoing = codeStoper(codeString)




while keepgoing:
    print(keepgoing)
    CheckMeIn()




