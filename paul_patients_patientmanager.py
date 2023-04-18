class Patient:
    def __init__(self, id, name, disease , gender, age):
        self.patient_id = id
        self.patient_name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def getters(self):
        def get_patient_id():
            return self.patient_id

        def get_patient_name():
            return self.patient_name

        def get_disease():
            return self.disease

        def get_gender():
            return self.gender

        def get_age():
            return self.age

        return get_patient_id, get_patient_name, get_disease, get_gender, get_age

    def setters(self):
        def set_patient_id(new_patient_id):
            self.patient_id = new_patient_id

        def set_patient_name(new_patient_name):
            self.patient_name = new_patient_name

        def set_disease(new_disease):
            self.disease = new_disease

        def set_gender(new_gender):
            self.gender = new_gender

        def set_age(new_age):
            self.age = new_age

        return set_patient_id, set_patient_name, set_disease, set_gender, set_age

    def __str__(self):
        return f"{self.patient_id}_{self.patient_name}_{self.disease}_{self.gender}_{self.age}"







patient1 = Patient(12, 'Pankaj', 'Cancer', 'Male', 30)
patient2 = Patient(13, 'Sumit', 'Cold', 'Male', 23)
patient3 = Patient(14, 'Alok', 'Maleriya', 'Male', 45)
patient4 = Patient(15, 'Ravi', 'Diabetes', 'Male', 25)

