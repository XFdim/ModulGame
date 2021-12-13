from convenience_store.models import Product, ProductCart

if __name__ == "__main__":

    store = {
        1: Product("apple", 15.5),
        2: Product("lemon", 26.7),
        3: Product("juice", 42.3),
    }
    cart = ProductCart()

    try:
        while True:

            choice = input("CHOICE (p, s, e): ")
            if choice == "p":
                print(f"1 - {store[1]}\n2 - {store[2]}\n3 - {store[3]}")
                while True:
                    try:
                        msg = "PRODUCT CHOICE 1, 2, 3: ".upper()
                        product_choice = int(input(msg))
                        product = store.get(product_choice)
                        if product is None:
                            continue
                        msg = f"AMOUNT OF {product}: ".upper()
                        amount = float(input(msg))
                        cart.put(product, amount)
                        break
                    except ValueError:
                        pass

            if choice == "s":
                print(cart)

            if choice == "e":
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        pass
    finally:
        print()
        print("GOOD BYE!")
