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

        return get_doctor_id, get_name, get_specialization, get_working_time, get_qualification, get_room_number

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

        doctor = Doctor(*list_information)  # Important
        return doctor

    def read_doctors_file(self):
        with open("doctors.txt", "r") as my_file:
            for information in my_file:
                list_information = information.strip().split('_')
                doctor_info = list_information
                name = doctor_info[1]
                name = ' '.join([word.capitalize() for word in name.split()])
                doctor_info[1] = name
                doctor = Doctor(*doctor_info)
                self.doctors_list.append(doctor)

    def search_doctor_by_id(self):
        search_doctor_id = input("Enter the doctor Id: ")
        id_found = False
        for list_doctor_id in self.doctors_list:
