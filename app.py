import services
import sys, time

flag_0 = True
flag_1 = True

while flag_0:
    while flag_1:
        print("""
  =========================================================
 ║                                                         ║
 ║                     Menu Inventory                      ║
 ║                                                         ║
  =========================================================
 ║ ------------------------------------------------------- ║
 ║ 1. >>  Add product.                                     ║
 ║ ------------------------------------------------------- ║
 ║ 2. >>  Print inventory.                                 ║
 ║ ------------------------------------------------------- ║
 ║ 3. >>  Find product.                                    ║
 ║ ------------------------------------------------------- ║
 ║ 4. >>  Update product.                                  ║
 ║ ------------------------------------------------------- ║
 ║ 5. >>  Delete product.                                  ║
 ║ ------------------------------------------------------- ║
 ║ 6. >>  Stats inventory.                                 ║
 ║ ------------------------------------------------------- ║
 ║ 7. >>  Save Inventory.                                  ║
 ║ ------------------------------------------------------- ║
 ║ 8. >>  Load Inventory.                                  ║
 ║ ------------------------------------------------------- ║
 ║ 9. >>  Exit.                                            ║
  ---------------------------------------------------------
""")
        option = input("\n\nChoose one option -> ")
        if option == "1":
            services.add_product()
        elif option == "2":
            services.print_inventory()
        elif option == "3":
            services.find_product()
        elif option == "4":
            services.update_product()
        elif option == "5":
            services.remove_product()
        elif option == "6":
            services.stats_inventory()
        elif option == "7":
            services.update()
        elif option == "8":
            services.load()
        elif option == "9":
            print("\nExiting the program...")
            time.sleep(1)
            sys.exit()
        else:
            print("\nInvalid option, please choose one option.")
            continue