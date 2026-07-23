from orders import (
    create_order,
    view_orders,
    search_order,
    edit_order,
    delete_order
)


def display_menu():
    while True:
        print("=" * 35)
        print("FASHION HOUSE MANAGER")
        print("=" * 35)
        print("1. Orders")
        print("2. Measurements")
        print("3. Styles")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            order_menu()

        elif choice == "2":
            print("Measurements feature coming soon")

        elif choice == "3":
            print("Styles feature coming soon")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


def order_menu():
    while True:
        print("=" * 30)
        print("          ORDERS")
        print("=" * 30)
        print("1. Create Order")
        print("2. View Orders")
        print("3. Search Order")
        print("4. Edit Order")
        print("5. Delete Order")
        print("6. Back")

        choice = input("Select option: ")

        if choice == "1":
            create_order()

        elif choice == "2":
            view_orders()

        elif choice == "3":
            search_order()

        elif choice == "4":
            edit_order()

        elif choice == "5":
            delete_order()

        elif choice == "6":
            break

        else:
            print("Invalid option")


def main():
    display_menu()


if __name__ == "__main__":
    main()
