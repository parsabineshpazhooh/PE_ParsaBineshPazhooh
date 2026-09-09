Answer = input("Salam Mikhaid kharid konid? ")
Answer = Answer.lower()
Answer = Answer.strip(' ')
if Answer == "yes":
    print("befarma'id yaddasht mikonam")
elif Answer == "no":
    print("mamnoon")
else:
    print("Lotfan faghat ba yes/no javab bedid")
