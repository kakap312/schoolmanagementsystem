

def generateParentKey(namePartList,totalNumerOfParents,update=False):
    key = "WD/PUN/FEE/" + namePartList[0] + "/"  + str((totalNumerOfParents + 1))    
    return key.upper()
