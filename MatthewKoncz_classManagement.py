# from CaoDatNguyen import Doctor, DoctorManager
# from PaulSholter import Patient, PatientManager
class Management:
    @staticmethod
    def display_menu():
        main_menu = 'Welcome to Alberta Hospital (AH) Management System\n' \
                    'Select from the following options, or select 3 to stop:\n' \
                    '1 -  Doctors\n' \
                    '2 -  Patients\n' \
                    '3 -  Exit Program\n'

        choice = ''
        while choice != '3':
            choice = input(main_menu)
            if choice == '1':
                Management.doctor_menu()
            elif choice == '2':
                Management.patient_menu()

        print('Thanks for using the program. Bye!')

    @staticmethod
    def doctor_menu():

        # doctor_manager = DoctorManager()

        doctor_menu = 'Doctors Menu:\n' \
                      '1 - Display Doctors list\n' \
                      '2 - Search for doctor by ID\n' \
                      '3 - Search for doctor by name\n' \
                      '4 - Add doctor\n' \
                      '5 - Edit doctor info\n' \
                      '6 - Back to the Main Menu\n'

        option = ''
        while option != '6':
            option = input(doctor_menu)
            if option == '1':
                # print(doctor_manager.display_doctors_list())
                x = '1'
            elif option == '2':
                # doctor_manager.search_doctor_by_id
                x = '1'
            elif option == '3':
                # doctor_manager.search_doctor_by_name
                x = '1'
            elif option == '4':
                # doctor_manager.add_dr_to_file
                x = '1'
            elif option == '5':
                # doctor_manager.edit_dr_info
                x = '1'

    @staticmethod
    def patient_menu():

        # patient_manager = PatientManager()

        patient_menu = 'Patients Menu:\n' \
                       '1 - Display patients list\n' \
                       '2 - Search for patient by ID\n' \
                       '3 - Add patient\n' \
                       '4 - Edit patients info\n' \
                       '5 - Back to the Main Menu\n'

        option = ''
        while option != '5':
            option = input(patient_menu)
            if option == '1':
                # patient_manager.display_patients_list()
                x = '1'
            elif option == '2':
                # patient_manager.search_patient_by_id
                x = '1'
            elif option == '3':
                # patient_manager.add_patient
                x = '1'
            elif option == '4':
                # patient_manager.edit_patient_info
                x = '1'


