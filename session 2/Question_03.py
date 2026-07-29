Name = input("Enter your Full name: ")
compressed_name, last_name = Name.split()
compressed_name = compressed_name[0]
print(f"{compressed_name}.{last_name}")
