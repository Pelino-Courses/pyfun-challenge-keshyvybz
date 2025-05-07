from product import Product
def main():
    try:
        product = Product("notebook",2.50,100)
        print (product.display_info())

        product.add_investory(25)
        print("\nAfter adding inventory")
        print(product.display_info())
         
        product.remove_inventory(30)
        print(product.display_info()) 


    except ValueError as e :
        print(f"error {e}")

if __name__=="__main__":
    main()


