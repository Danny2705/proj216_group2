class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
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
        print(f"{doctor.doctor_id:<4} {doctor.name:<22} {doctor.specialization:<15} {doctor.working_time:<15}"
              f" {doctor.qualification:<16} {doctor.room_number:<8}")

    def edit_doctor_info(self):
        edit_doctor_id = input("Please enter the ID of the doctor that you want to edit: ")
        doctor_found = False

        for doctor in self.doctors_list:
            if edit_doctor_id == doctor.get_doctor_id():
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
            print(f"Doctor whose ID is {new_doctor.get_doctor_id().split('_')[0]} has been added")


# manager_of_doctor = DoctorManager()
# # manager_of_doctor.add_dr_to_file()
# # manager_of_doctor.edit_doctor_info()
