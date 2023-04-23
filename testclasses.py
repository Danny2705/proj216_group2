class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def read_patients_file(self):
        with open('patients.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                patient_data = line.strip().split('_')
                patient = Patient(*patient_data)
                self.patients.append(patient)

    # Just wanted to see if this works. Not formatted properly
    def display_patients_list(self):
        for patient in self.patients:
            print(str(patient))


class Patient:
    def __init__(self, pid='', name='', disease='', gender='', age=''):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid

    def set_pid(self, pid):
        self.pid = pid

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_disease(self):
        return self.disease

    def set_disease(self, disease):
        self.disease = disease

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f'{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}'


class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def read_doctors_file(self):
        with open('doctors.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                doctors_data = line.strip().split('_')
                doctor = Doctor(*doctors_data)
                self.doctors.append(doctor)

    # Just wanted to see if this works. Not formatted properly
    def display_doctors_list(self):
        doctors_list = ''
        for doctor in self.doctors:
            doctors_list += str(doctor) + '\n'
        return doctors_list


class Doctor:
    def __init__(self, did='', name='', specialization='', working_time='', qualification='', room_number=''):
        self.did = did
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_did(self):
        return self.did

    def set_did(self, did):
        self.did = did

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, specialization):
        self.specialization = specialization

    def get_working_time(self):
        return self.working_time

    def set_working_time(self, working_time):
        self.working_time = working_time

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, qualification):
        self.qualification = qualification

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, room_number):
        self.room_number = room_number

    def __str__(self):
        return f'{self.did}_{self.name}_{self.specialization}_{self.working_time}_' \
               f'{self.qualification}_{self.room_number}'


patientM = PatientManager()
doctorM = DoctorManager()

patientM.display_patients_list()
doctorM.display_doctors_list()

