import os
from datetime import date


#Gets the data and formates it for day,month, year
today = date.today()
fileDateName= today.strftime("%d_%m_%Y")


#These are the name in which we will use to make the folder
# and the file name and to the path address
folderName = 'CheckInOutFolder'
fileName= fileDateName+".txt"
pathFinder = folderName+"/"+fileName

#checks if the folder and if the file is there
folderThere= os.path.isdir(folderName)
pathThere = os.path.exists(pathFinder)

path = os.path.join(folderName,fileName)



#If folder is not there it will make a folder to store the data
if folderThere==False:
    os.makedirs(folderName)


# if the folder is there but the file is not there for the new day
# it will add a txt file for the all the log of that day
if pathThere == False:

    file = open(path,'w' )

# This will add your name and the time you signed in
def nameAndTimeAdder(name, time):
    with open (path,'w') as f:
        f.write(name + "\n Check In: "+time[0])
    if time[1]:
        with open (path,'w') as f:
            f.write("Check Out: "+time[1])




