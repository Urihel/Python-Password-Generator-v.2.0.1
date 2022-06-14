import random

def createNumbers(list1):
    for i in range(48,58):
        #print(chr(i))
        list1.append(chr(i))
def uppercaseAlphabet(list2):
    for j in range(65,91):
        list2.append(chr(j))
def lowercaseAlphabet(list3):
    for k in range(97,123):
        list3.append(chr(k))
def createSymbols(list4):
    for l in range(33,48):
        list4.append(chr(l)) 
def appendlists(list1,list2,list3,list4,list5):
    list5.append(list1)
    list5.append(list2)
    list5.append(list3)
    list5.append(list4)
def generatePassword(list5,list6):
    #print(list4)
    indexPosition1 = random.randint(0,3)
    #print(indexPosition1)
    indexPosition2 = random.randint(0,len(list5[indexPosition1]))
    #print(list4[indexPosition1][indexPosition2])
    n = 0
    while n < 15:
        list6.append(list5[indexPosition1][indexPosition2-1])
        indexPosition1 = random.randint(0,3)
        indexPosition2 = random.randint(0,len(list5[indexPosition1]))
        n+=1
def printPassword(list6):
    #print(list6)
    password = "".join(list6)
    print(password)
#--------------------------------------main----------------------------------
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
cn = createNumbers(list1)
uppercaseAlphabet(list2)
lowercaseAlphabet(list3)
createSymbols(list4)
appendlists(list1,list2,list3,list4,list5)
generatePassword(list5,list6)
printPassword(list6)



