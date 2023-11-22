

def generateParentKey(namePartList,totalNumerOfParents,update=False):
    fullnameInitials = "NOI"
    if update:
        if len(namePartList) > 2:
            firstnameInitial = namePartList[0]
            lastnameInitial = namePartList[1]
            middlenameInitial = namePartList[2]
            fullnameInitials = firstnameInitial[0] + lastnameInitial[0] + middlenameInitial[0]
        elif len(namePartList) == 2 :
            firstnameInitial = namePartList[0]
            lastnameInitial = namePartList[1]
            fullnameInitials = firstnameInitial[0] + lastnameInitial[0]

        key = "WD/PUN/" + fullnameInitials + "/"  + str((totalNumerOfParents))  
    else:
        if len(namePartList) > 2:
            firstnameInitial = namePartList[0]
            lastnameInitial = namePartList[1]
            middlenameInitial = namePartList[2]
            fullnameInitials = firstnameInitial[0] + lastnameInitial[0] + middlenameInitial[0]
        elif len(namePartList) == 2 :
            firstnameInitial = namePartList[0]
            lastnameInitial = namePartList[1]
            fullnameInitials = firstnameInitial[0] + lastnameInitial[0]

        key = "WD/PUN/PAR/" + fullnameInitials + "/"  + str((totalNumerOfParents + 1)) 

       
        
    return key.upper()
