class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None,
                 working_time=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.working_time

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number

    def set_doctor_id(self, new_doctor_id):
        self.doctor_id = new_doctor_id

    def set_name(self, new_name):
        self.name = new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return f"{self.get_doctor_id()}_{self.get_name()}_{self.get_specialization()}_{self.get_working_time()}\
        _{self.get_qualification()}_{self.get_room_number()}"


class DoctorManager:
    def __init__(self):
        self.doctors_list = []
        self.read_doctors_file()

    @staticmethod
    def format_dr_info(doctor):
        return f"{doctor.get_doctor_id()}_{doctor.get_name()}_{doctor.get_specialization()}_" \
               f"{doctor.get_working_time()}_{doctor.get_qualification()}_{doctor.get_room_number()}"

    @staticmethod
    def enter_dr_info():
        list_dr_info = ["ID", "name", "speciality", "timing (e.g., 7am-10pm)", "qualification", "room number"]
        list_information = []
        for lists in list_dr_info:
            doctor_info = input(f"Enter the doctor's {lists}: ")
            list_information.append(doctor_info)
        doctor = Doctor(*list_information)
        return doctor

    def read_doctors_file(self):
        with open("Project Data/doctors.txt", "r") as my_file:
            my_file.readline()
            for information in my_file:
                list_information = information.strip().split('_')
                doctor = Doctor(*list_information)
                self.doctors_list.append(doctor)

    def search_doctor_by_id(self):
        search_doctor_id = input("Enter the doctor Id: ")
        id_found = False
        for list_doctor_id in self.doctors_list:
            if list_doctor_id.get_doctor_id() == search_doctor_id:
                print("{:<5}{:<23}{:<16}{:<16}{:<17}{:<8}".format(
                    "Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
                self.display_doctor_info(list_doctor_id)
                id_found = True
                break
        if not id_found:
            print(f"Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):
        search_doctor_name = input("Enter the doctor name: ")
        name_found = False
        for list_doctor_name in self.doctors_list:
            if list_doctor_name.get_name() == search_doctor_name:
                print("{:<5}{:<23}{:<16}{:<16}{:<17}{:<8}".format(
                    "Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
                self.display_doctor_info(list_doctor_name)
                name_found = True
                break
        if not name_found:
            print(f"Can't find the doctor with the same name on the system")

    @staticmethod
    def display_doctor_info(doctor):
        print(f"{doctor.get_doctor_id():<4} {doctor.get_name():<22} {doctor.get_specialization():<15}"
              f" {doctor.get_working_time():<15} {doctor.get_qualification():<16} {doctor.get_room_number():<8}")

    def edit_doctor_info(self):
        edit_doctor_id = input("Please enter the ID of the doctor that you want to edit: ")
        doctor_found = False

        for doctor in self.doctors_list:
            if edit_doctor_id == doctor.get_doctor_id():
                fields = ["Name", "Specialist in", "Timing", "Qualification", "Room Number"]
                setters = [doctor.set_name, doctor.set_specialization, doctor.set_working_time,
                           doctor.set_qualification, doctor.set_room_number]
                new_values = []

                for i in range(len(fields)):
                    new_value = input(f"Enter new {fields[i]}: ")
                    new_values.append(new_value)
                    setters[i](new_value)

                self.write_list_of_doctors_to_file()
                print(f"Doctor whose ID is {edit_doctor_id} has been edited.")
                doctor_found = True
                break

        if not doctor_found:
            print(f"Cannot find a doctor with ID {edit_doctor_id} in the system.")

    def display_doctors_list(self):
        print("{:<4}{:<22}{:<15}{:<15}{:<16}{:<8}".format("Id", "Name", "Speciality", "Timing", "Qualification",
                                                          "Room Number"))
        for doctor in self.doctors_list:
            print("{:<4}{:<22}{:<15}{:<15}{:<16}{:<8}".format(doctor.get_doctor_id().title(),
                                                              doctor.get_name().title(),
                                                              doctor.get_specialization().title(),
                                                              doctor.get_working_time().title(),
                                                              doctor.get_qualification().upper(),
                                                              doctor.get_room_number().title()))

    def write_list_of_doctors_to_file(self):
        with open("Project Data/doctors.txt", "w") as my_file:
            for doctor in self.doctors_list:
                my_file.write(f"{self.format_dr_info(doctor)} \n")

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors_list.append(new_doctor)
        format_doctor = self.format_dr_info(new_doctor)
        with open("Project Data/doctors.txt", "a") as my_file:
            my_file.write(f"{format_doctor} \n")
            print(f"Doctor whose ID is {new_doctor.get_doctor_id()} has been added")


class Patient:
    def __init__(self, patient_id=None, name=None, disease=None, gender=None, age=None):
        self.patient_id = patient_id
        self.patient_name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_patient_id(self):
        return self.patient_id

    def get_patient_name(self):
        return self.patient_name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_name(self, new_patient_name):
        self.patient_name = new_patient_name

    def set_patient_id(self, new_patient_id):
        self.patient_id = new_patient_id

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"{self.get_patient_id()}_{self.get_patient_name()}_{self.get_disease()}_{self.get_gender()}\
        _{self.get_age()}"


class PatientManagement:
    def __init__(self):
        self.patient_list = []
        self.read_patients_file()

    @staticmethod
    def format_patient_info(patient):
        return f"{patient.patient_id}_{patient.patient_name}_{patient.disease}_{patient.gender}_{patient.age}"

    @staticmethod
    def enter_patient_info():
        list_patient_info = ["ID", "name", "disease", "gender", "age"]
        list_information = []
        for lists in list_patient_info:
            patient_info = input(f"Enter the patients {lists}:")
            list_information.append(patient_info)
        patient = Patient(*list_information)
        return patient

    def read_patients_file(self):
        with open("Project Data/patients.txt", "r") as my_file:
            next(my_file)
            for information in my_file:
                list_information = information.strip().split('_')
                patient = Patient(*list_information)
                self.patient_list.append(patient)

    def search_patient_by_id(self):
        search_patient_id = input("Enter patients ID: ")
        id_found = False
        for list_patient_id in self.patient_list:
            if list_patient_id.get_patient_id() == search_patient_id:
                print("{:<5}{:<23}{:<16}{:<16}{:<17}".format("Id", "Name", "Disease", "Gender", "Age"))
                self.display_patient_info(list_patient_id)
                id_found = True
                break
        if not id_found:
            print(f"Cannot find the patient with that ID in the system")

    @staticmethod
    def display_patient_info(patient):
        print(f"{patient.patient_id:<4} {patient.name:<22} {patient.disease:<15} {patient.gender:<15}"
              f"{patient.age:<16}")

    def edit_patient_info(self):
        edit_patient_id = input("Please enter the ID of the patient you would like to edit: ")
        patient_found = False

        for patient in self.patient_list:
            if edit_patient_id == patient.get_patient_id():
                fields = ["Name", "Disease", "Gender", "Age"]
                setters = [patient.set_patient_name, patient.set_patient_id, patient.set_disease,
                           patient.set_gender, patient.set_age]
                new_values = []

                for i in range(len(fields)):
                    new_value = input(f"Enter new {fields[i]}")
                    new_values.append(new_value)
                    setters[i](new_value)

            self.write_list_of_patients_to_file()
            print(f"Patients who's ID is {edit_patient_id} has been edited.")
            patient_found = True
            break

        if not patient_found:
            print(f"Cannot find a patient with the ID {edit_patient_id} in the system.")

    def display_patient_list(self):
        print("{:<4}{:<22}{:<15}{:16}".format("Id", "Name", "Disease", "Gender", "Age"))

        for patient in self.patient_list:
            print("{:<4}{:<22}{:<15}{:<15}{:<16}".format(patient.get_patient_id().title(),
                                                         patient.get_patient_name().title(),
                                                         patient.get_disease().title(),
                                                         patient.get_gender().title(),
                                                         patient.get_age().title()))

    def write_list_of_patients_to_file(self):
        with open("Project Data/patients.txt", "w") as my_file:
            for patient in self.patient_list:
                my_file.write(f"{self.format_patient_info(patient)} \n")

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patient_list.append(new_patient)
        format_patient = self.format_patient_info(new_patient)
        with open("Project Data/patients.txt", "a") as my_file:
            my_file.write(f"{format_patient} \n")
            print(f"Patients whose ID is {new_patient.get_patient_id()} has been added")


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

        doctor_manager = DoctorManager()

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
                print(doctor_manager.display_doctors_list())
            elif option == '2':
                doctor_manager.search_doctor_by_id()
            elif option == '3':
                doctor_manager.search_doctor_by_name()
            elif option == '4':
                doctor_manager.add_dr_to_file()
            elif option == '5':
                doctor_manager.edit_doctor_info()

    @staticmethod
    def patient_menu():

        patient_manager = PatientManagement()

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
                patient_manager.display_patient_list()
            elif option == '2':
                patient_manager.search_patient_by_id()
            elif option == '3':
                patient_manager.enter_patient_info()
            elif option == '4':
                patient_manager.edit_patient_info()


manager = Management()
manager.display_menu()
