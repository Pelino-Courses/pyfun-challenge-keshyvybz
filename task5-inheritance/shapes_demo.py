from shapes import Rectangle, Circle, Square

def main():
    try:
        rect = Rectangle(10, 5)
        print(rect)
        print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}\n")

        circ = Circle(7)
        print(circ)
        print(f"Area: {circ.area():.2f}, Perimeter: {circ.perimeter():.2f}\n")

        circ2 = Circle.from_diameter(14)
        print("Circle created from diameter:")
        print(circ2)
        print(f"Area: {circ2.area():.2f}, Perimeter: {circ2.perimeter():.2f}\n")

        sq = Square(4)
        print(sq)
        print(f"Area: {sq.area()}, Perimeter: {sq.perimeter()}")

        # Uncomment to test validation
        # bad_rect = Rectangle(-1, 3)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
