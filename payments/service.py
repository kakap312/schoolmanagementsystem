

def generateKey(totalNumerOfParents,update=False):
    key = "WL/PUN/PAY/NO/"    + str((totalNumerOfParents + 1))    
    return key.upper()
