class Management:

    @staticmethod
    def display_menu(self):
        print("Welcome to the management system!")

        while True:
            print("Main menu:")
            print("1. Doctors submenu")
            print("2. Patients submenu")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.doctors_submenu()
            elif choice == "2":
                self.patients_submenu()
            elif choice == "3":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice, please try again.")

    @staticmethod
    def doctors_submenu(self):
        while True:
            print("Doctors submenu:")
            print("1. Display doctors list")
            print("2. Search for a doctor by ID")
            print("3. Search for a doctor by name")
            print("4. Add a new doctor")
            print("5. Edit an existing doctor")
            print("6. Return to main menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                # display doctors list
                print("Displaying doctors list...")
            elif choice == "2":
                # search for doctor by ID
                print("Searching for a doctor by ID...")
            elif choice == "3":
                # search for doctor by name
                print("Searching for a doctor by name...")
            elif choice == "4":
                # add a new doctor
                print("Adding a new doctor...")
            elif choice == "5":
                # edit an existing doctor
                print("Editing an existing doctor...")
            elif choice == "6":
                # return to main menu
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice, please try again.")

    @staticmethod
    def patients_submenu(self):
        while True:
            print("Patients submenu:")
            print("1. Display patients list")
            print("2. Search for a patient by ID")
            print("3. Add a new patient")
            print("4. Edit an existing patient")
            print("5. Return to main menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                # display patients list
                print("Displaying patients list...")
            elif choice == "2":
                # search for patient by ID
                print("Searching for a patient by ID...")
            elif choice == "3":
                # add a new patient
                print("Adding a new patient...")
            elif choice == "4":
                # edit an existing patient
                print("Editing an existing patient...")
            elif choice == "5":
                # return to main menu
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice, please try again.")
