

def calculate_circle_area_and_perimeter(radius):
    pi=3.14159
    area=pi*radius**2
    perimeter=pi*radius*2
    return area,perimeter

def calculate_rectangle_area_and_perimeter(length,width):
    area=length*width
    perimeter=(length+width)*2
    return area,perimeter

def calculate_triangle_area_and_perimeter(side1,side2,side3):
    s=(side1+side2+side3)*0.5
    area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
    perimeter=side1+side2+side3
    return area,perimeter

def is_or_not_a_triangle(side1,side2,side3):
    if side1<=0 and side2<=0 and side3<=0:
        return False
    if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
        return True
    else:
        return False

def main():
    while True:
        print("請選擇一個幾何圖形:")
        print("1.圓形")
        print("2.矩形")
        print("3.三角形")
        print("4.退出程式")
        
        choice=input("請輸入選擇的幾何圖形代號(1/2/3/4):")
    
        if choice == '1':
            radius=float(input("請輸入圓半徑:"))
            if radius>0:
                area,perimeter=calculate_circle_area_and_perimeter(radius)
                print(f"\n圓周長為:{perimeter:.2f}")
                print(f"圓面積為:{area:.2f}\n")
            else:
                print("\n半徑不能是負數或零！請再試一次。\n")
            
        if choice == '2':
            length=float(input("請輸入矩形長度:"))
            width=float(input("請輸入矩形寬度:"))
            if length>0 and width>0:
                area,perimeter=calculate_rectangle_area_and_perimeter(length,width)
                print(f"\n矩形周長為:{perimeter:.2f}")
                print(f"矩形面積為:{area:.2f}\n")
            else:
                print("\n長寬不能是負數或零！請再試一次。\n")
    
        if choice == '3':
            side1=float(input("請輸入三角形的第一邊長:"))
            side2=float(input("請輸入三角形的第二邊長:"))
            side3=float(input("請輸入三角形的第三邊長:"))
            if  is_or_not_a_triangle(side1,side2,side3):
                area,perimeter=calculate_triangle_area_and_perimeter(side1,side2,side3)
                print(f"\n三角形周長為:{perimeter:.2f}")
                print(f"三角形面積為:{area:.2f}\n") 
            else:
                print("\n三角形不成立！請再試一次。\n")
    
        if choice == '4':
            print("感謝使用，再見！")
            return
        
main()



