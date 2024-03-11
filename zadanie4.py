import math

shapes= ["circle","triangle","square","rectangle"]
shape=input("please input name of the geometric shape you want to calculate area of: ")
if shape in shapes:
    
    if shape.lower() == "circle":
        a=int(input("input radius of the shape"))
        if a <=0:
            print("values cant be lower or equal to 0")
        else:
            area=math.pi * (a**2)
            print("area of ", shape ," is ", area)
                           
    elif shape.lower() == "triangle":
        a=int(input("input base of the shape"))
        b=int(input("input heigh of the shape"))
        if a <=0 or b <=0 :
            print("values cant be lower or equal to 0")
        else:
            area=(a*b)/2
            print("area of ", shape ," is ", area)   

    elif shape.lower() == "square":
        a=int(input("input length of the side"))
        if a <=0:
            print("values cant be lower or equal to 0")
        else:
            area=a**2
            print("area of ", shape ," is ", area)
            
    elif shape.lower() == "rectangle":
        a=int(input("input length of the shape"))
        b=int(input("input width of the shape"))
        if a <=0 :
            print("values cant be lower or equal to 0")
        else:
            area=a*b
            print("area of ", shape ," is ", area)
        

else:
    print("im sorry but this shape does not exist or i was too lazy \n I can calculate area of ", shapes )
