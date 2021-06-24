from DataBase import *
from datetime import datetime
from collections import defaultdict

timeNow = str(datetime.now().time())
name = ''
nameInDataBase = {}
timeList= []
stopper = False


def CheckMeIn():

    name = input("Hi my name is Roger what is your name: ")


    if name not in nameInDataBase.keys():
        nameInDataBase[name] = nameInDataBase.get(name, [])+ [timeNow]
        timeList.append(timeNow)
        nameAndTimeAdder(name, timeList[0])

    if name in nameInDataBase.keys():
        nameInDataBase[name] = nameInDataBase.get(name, []) + [timeNow]
        timeList.append(timeNow)
        nameAndTimeAdder(name, timeList[0])

    if name=="0":
        stopper=True





# def CheckInCheckOut():
#     noNameHere = True
#      while noNameHere:


