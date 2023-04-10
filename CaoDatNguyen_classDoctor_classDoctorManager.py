class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number ):
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

