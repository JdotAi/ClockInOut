from DataBase import *
name = ''
codeString = ""
def CheckMeIn():
    name = input("Hi my name is Roger what is your name: ")
    timeNow = str(datetime.now().time())
    codeString = codeStoper(name)


    if name not in nameInDataBase.keys():
        nameInDataBase[name] = nameInDataBase.get(name, [])+ [timeNow]
        checkInAdder(name, nameInDataBase[name])

    elif name in nameInDataBase.keys():
        nameInDataBase[name] = nameInDataBase.get(name, []) + [timeNow]
        checkOutAdder(name, nameInDataBase[name])





def codeStoper(codeString):
    if name=='000':
        return False
    else:
        return True



# def CheckInCheckOut():
#     noNameHere = True
#      while noNameHere:



# name = input("Hi my name is Roger what is your name: ")
#
#
# if name not in nameInDataBase.keys():
#     nameInDataBase[name] = nameInDataBase.get(name, [])+ [timeNow]
#     timeList.append(timeNow)
#     nameAndTimeAdder(name, timeList[0])
#
# if name in nameInDataBase.keys():
#     nameInDataBase[name] = nameInDataBase.get(name, []) + [timeNow]
#     timeList.append(timeNow)
#     nameAndTimeAdder(name, timeList[0])
#
# if name=="0":
#     stopper=True