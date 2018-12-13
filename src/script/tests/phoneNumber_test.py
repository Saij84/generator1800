from script.constants.constants import NUMDICT as nDict

phNum = "546541"

def numberTest(phNum):
    letterList = []

    for num in phNum:
        letterList.extend(nDict[int(num)] )
    print(letterList)


numberTest(phNum)