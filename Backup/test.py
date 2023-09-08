absenties = ("JS")

def printAbsenties(absentiesList:list):
    for i in range(len(absentiesList)):
        if i != len(absentiesList) - 1:
            print(f"{absentiesList[i]}, ",end="")
        else:
            print(absentiesList[i],end="")

printAbsenties(absenties)