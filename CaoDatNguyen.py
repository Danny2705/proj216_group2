class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def getters(self):
        def get_doctor_id():
            return self.doctor_id

        def get_name():
            return self.name

        def get_specialization():
            return self.specialization

        def get_working_time():
            return self.working_time

        def get_qualification():
            return self.qualification

        def get_room_number():
            return self.room_number

        return get_doctor_id(), get_name(), get_specialization(), get_working_time(), get_qualification(), \
            get_room_number()

    def setters(self):
        def set_doctor_id(new_doctor_id):
            self.doctor_id = new_doctor_id

        def set_name(new_name):
            self.name = new_name

        def set_specialization(new_specialization):
            self.specialization = new_specialization

        def set_working_time(new_working_time):
            self.working_time = new_working_time

        def set_qualification(new_qualification):
            self.qualification = new_qualification

        def set_room_number(new_room_number):
            self.room_number = new_room_number

        return set_doctor_id, set_name, set_specialization, set_working_time, set_qualification, set_room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}\
        _{self.qualification}_{self.room_number}"


class DoctorManager:
    def __init__(self):
        self.doctors_list = []
        self.read_doctors_file()

    @staticmethod
    def format_dr_info(doctor):
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_" \
               f"{doctor.qualification}_{doctor.room_number}"

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
            if list_doctor_id.doctor_id == search_doctor_id:
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
            if list_doctor_name.name.strip() == search_doctor_name:
                print("{:<5}{:<23}{:<16}{:<16}{:<17}{:<8}".format(
                    "Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
                self.display_doctor_info(list_doctor_name)
                name_found = True
                break
        if not name_found:
            print(f"Can't find the doctor with the same name on the system")

    @staticmethod
    def display_doctor_info(doctor):
        print(f"{doctor.doctor_id:<4} {doctor.name:<22} {doctor.specialization:<15} {doctor.working_time:<15}"
              f" {doctor.qualification:<16} {doctor.room_number:<8}")

    def edit_doctor_info(self):
        edit_doctor_id = input("Please enter the ID of the doctor that you want to edit: ")
        doctor_found = False

        for doctor in self.doctors_list:
            if edit_doctor_id == doctor.doctor_id:
                fields = ["Name", "Specialist in", "Timing", "Qualification", "Room Number"]
                new_values = []

                for field in fields:
                    new_info = input(f"Enter new {field}: ")
                    new_values.append(new_info)

                doctor.name, doctor.specialization, doctor.working_time, doctor.qualification, doctor.room_number \
                    = new_values
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
            print("{:<4}{:<22}{:<15}{:<15}{:<16}{:<8}".format(doctor.doctor_id.title(), doctor.name.title(),
                                                              doctor.specialization.title(),
                                                              doctor.working_time.title(),
                                                              doctor.qualification.upper(),
                                                              doctor.room_number.title()))

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
            print(f"Doctor whose ID is {new_doctor.doctor_id.split('_')[0]} has been added")


# manager_of_doctor = DoctorManager()
# # manager_of_doctor.add_dr_to_file()
# # manager_of_doctor.edit_doctor_info()

class Patient:
    def __init__(self, patient_id=None, name=None, disease=None,
                 gender=None, age=None):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def getters(self):
        def get_patient_id():
            return self.patient_id

        def get_name():
            return self.name

        def get_disease():
            return self.disease

        def get_gender():
            return self.gender

        def get_age():
            return self.age

        return get_patient_id, get_name, get_disease, get_gender, get_age

    def setters(self):
        def set_patient_id(new_patient_id):
            self.patient_id = new_patient_id

        def set_name(new_name):
            self.name = new_name

        def set_disease(new_disease):
            self.disease = new_disease

        def set_gender(new_gender):
            self.gender = new_gender

        def set_age(new_age):
            self.age = new_age

        return set_patient_id, set_name, set_disease, set_gender, set_age

    def __str__(self):
        return f"{self.patient_id}_{self.name}_{self.disease}_{self.gender}_{self.age}"


class PatientManager:
    def __init__(self):
        self.patients_list = []
        self.read_patients_file()

    @staticmethod
    def format_patient_info_for_file(patient):
        return f"{patient.patient_id}_{patient.name}_{patient.disease}_{patient.gender}_" \
               f"{patient.age}"

    @staticmethod
    def enter_patient_info():
        patient_id = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")

        patient = Patient(patient_id, name, disease, gender, age)
        return patient

    def read_patients_file(self):
        with open('D:/School/OOP/Project/Project Data/patients.txt', 'r') as my_file:
            for information in my_file:
                list_information = information.strip().split('_')
                patient_id, name, disease, gender, age = list_information
                patient = Patient(patient_id, name, disease, gender, age)
                self.patients_list.append(patient)

    def search_patient_by_id(self):
        search_patient_id = input("Enter the Patient Id: ")
        id_found = False
        for list_patient_id in self.patients_list:
            if list_patient_id.patient_id == search_patient_id:
                self.display_patient_info(list_patient_id)
                id_found = True
                break
        if not id_found:
            print(f"Can't find the Patient with the same id on the system")

    @staticmethod
    def display_patient_info(patient):
        print(f"{patient.patient_id:<5} {patient.name:<20} {patient.disease:<15} {patient.gender:<15}"
              f" {patient.age:<15} ")

    def edit_patient_info_by_id(self):
        edit_patient_id = input("Please enter the id of the Patient that you want to edit their information: ")
        id_found = False
        for patient in self.patients_list:
            if edit_patient_id == patient.patient_id:
                id_found = True
                name = input("Enter new Name:")
                disease = input("Enter new disease ")
                gender = input("Enter new gender: ")
                age = input("Enter new age: ")
                patient.name = name
                patient.disease = disease
                patient.gender = gender
                patient.age = age
                self.write_list_of_patients_to_file()
                print(f"Patient whose ID is {edit_patient_id} has been edited")
                break
        if not id_found:
            print("Can't find the Patient with the same ID on the system")

    def display_patients_list(self):
        for patient in self.patients_list:
            self.display_patient_info(patient)

    def write_list_of_patients_to_file(self):
        with open("D:/School/OOP/Project/Project Data/patients.txt", "w") as my_file:
            for patient in self.patients_list:
                my_file.write(
                    f"{self.format_patient_info_for_file(patient)} \n")

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients_list.append(new_patient)
        format_patient = self.format_patient_info_for_file(new_patient)
        with open("/pythonProject5/venv/Scripts/doctors.txt", "a") as my_file:
            my_file.write(f"{format_patient} \n")
        print(f"Doctor whose ID is {new_patient} has been added")


class Management:
    def __init__(self, doctor_manager):
        self.doctor_manager = doctor_manager
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            user_choice = input("Select from the following options, or select 3 to stop: \n"
                                "1 - Doctors \n"
                                "2 - Patients \n"
                                "3 - Exit Program \n")
            if user_choice == "1":
                while True:
                    option = input("Doctors Menu: \n"
                                   "1 - Display Doctors list \n"
                                   "2 - Search for doctor by ID \n"
                                   "3 - Search for doctor by name \n"
                                   "4 - Add doctor \n"
                                   "5 - Edit doctor info \n"
                                   "6 - Back to the Main Menu \n")

                    doctor_menu = {
                        "1": self.doctor_manager.display_doctors_list,
                        "2": self.doctor_manager.search_doctor_by_id,
                        "3": self.doctor_manager.search_doctor_by_name,
                        "4": self.doctor_manager.add_dr_to_file,
                        "5": self.doctor_manager.edit_doctor_info,
                        "6": self.display_menu
                    }
                    if option in doctor_menu:
                        doctor_menu[option]()
                        if option == "6":
                            break
            elif user_choice == "2":
                while True:
                    option = input("Patients Menu: \n"
                                   "1 - Display patients list \n"
                                   "2 - Search for patient by ID \n"
                                   "3 - Add patient \n"
                                   "4 - Edit patient info \n"
                                   "5 - Back to the Main Menu \n")

                    patient_menu = {
                        "1": self.patient_manager.display_patients_list,
                        "2": self.patient_manager.search_patient_by_id,
                        "3": self.patient_manager.add_patient_to_file,
                        "4": self.patient_manager.edit_patient_info_by_id,
                        "5": self.display_menu
                    }
                    if option in patient_menu:
                        patient_menu[option]()
                        if option == "5":
                            break
            elif user_choice == "3":
                print("Thanks for using the program. Bye!")
                break


# Main program
print("Welcome to Alberta Hospital (AH) Management system")
management = Management(DoctorManager())
management.display_menu()
