from shapes import Rectangle,Circle,Square
def main():
    try:
        rect = Rectangle(10,5)
        print (rect)
        print (f"area of the rectangle{rect.area()},and its perimeter {rect.perimeter()}")

        circ = circle(7)
        print(rect)
        print(f"area of a circle {circ.area():.2f},perimeter :{circ.perimeter():.2f}")
        
        
        sp =Square(4)
        print(sq)
        print (f"area is :{sq.area()}, and the perimeter {sq.perimeter():.2f}")

    except ValueError as e:
        print (f"error:{e}") 

    if __name__=="__main__" : 
        main ()    

       