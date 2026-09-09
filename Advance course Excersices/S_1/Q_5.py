Answer = input("Salam Mikhaid kharid konid? ")
Answer = Answer.lower()
Answer = Answer.strip(' ')
if Answer == "yes":
    products = list(input("befarma'id yaddasht mikonam: ").split(","))
    print(f"mahsoolati ke goftid : {products}")
elif Answer == "no":
    print("mamnoon")
else:
    print("Lotfan faghat ba yes/no javab bedid")

