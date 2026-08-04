color_1 = input("Enter first color: ")
color_2 = input("Enter second color: ")
color_3 = input("Enter third color: ")
color_1, color_2, color_3 = color_1.lower(), color_2.lower(), color_3.lower()
if color_3 == color_1 == color_2:
    print("all colors are same")

elif color_1 == color_2 or color_3 == color_1 or color_3 == color_2:
    print("2 colors are same")
