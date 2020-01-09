import pymongo


def fetchChange(instr):
    inputList = instr.split()
    for items in inputList:
        if(len(items)==10):
            if(items[:3].upper() == "CHG"):
                return items.upper()
    return False
            
inputString = input("Enter Change Number : ").strip()
chgNumber = fetchChange(inputString)
#print(chgNumber)
if(chgNumber == False):
	print("OOPS !! No Change Number found");
else:
	obj = pymongo.MongoClient();
	db=obj.Change;
	output=db.info.find_one({"changeNumber" : chgNumber })
	if(output == None):
		print("Change not found. Please provide a  valid change number");
	else:
		ctsk= output.get("changeTask");
		print(ctsk)