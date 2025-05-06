from product import Product

def main():
    try:
        product = Product("Notebook", 2.50, 100)
        print(product.display_info())

        product.add_inventory(25)
        print("\nAfter adding inventory:")
        print(product.display_info())

        product.remove_inventory(30)
        print("\nAfter removing inventory:")
        print(product.display_info())

        # Uncomment to test validation
        # product.price = -5
        # product.remove_inventory(200)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
