

def generateParentKey(namePartList,totalNumerOfParents,update=False):
    key = "WD/PUN/SUB/" + namePartList[0] + "/"  + str((totalNumerOfParents + 1))    
    return key.upper()
