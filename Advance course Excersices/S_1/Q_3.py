Answer = input("Salam\nMikhaid kharid konid? ")
Answer = Answer.lower()
Answer = Answer.strip(' ')
if Answer == "yes":
    print("befarma'id\nyaddasht mikonam")
elif Answer == "no":
    print("mamnoon")
else:
    print("Lotfan faghat ba yes/no javab bedid")
