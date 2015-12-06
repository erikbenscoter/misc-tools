def makeGettersAndSetters(cls, type,varName):
	print("######function declarations#####")
	print(type," get",varName,"();")
	print("void set",varName,"(",type," ",varName,");")
	print("######function implementations #####")
	print(type,cls,"::get",varName,"(){return ",cls,"::",varName,";}")
	print("void", cls,"::set",varName,"(",type," input){",cls,"::",varName," = input;}")