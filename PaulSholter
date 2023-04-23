class Patient:
    def __init__(self, id, name, disease, gender, age):
        self.patient_id = id
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

    def set_patient_id(self, new_patient_id):
        self.patient_id = new_patient_id

    def set_patient_name(self, new_patient_name):
        self.patient_name = new_patient_name

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
                new_values = []

                for field in fields:
                    new_info = input(f"Enter the new {field}: ")
                    new_values.append(new_info)

            patient.set_patient_name, patient.set_patient_id, patient.set_disease, \
                patient.set_gender, patient.set_age = new_values
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


manager_of_patient = PatientManagement()



