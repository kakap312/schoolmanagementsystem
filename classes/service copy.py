

def generateParentKey(namePartList,totalNumerOfParents,update=False):
    key = "WD/PUN/CLS/" + namePartList + "/"  + str((totalNumerOfParents + 1))    
    return key.upper()
