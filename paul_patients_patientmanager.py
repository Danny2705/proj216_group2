class Patient:
    def __init__(self, id, name, disease , gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age


patient1 = Patient(12, 'Pankaj', 'Cancer', 'Male', 30)
patient2 = Patient(13, 'Sumit', 'Cold', 'Male', 23)
patient3 = Patient(14, 'Alok', 'Maleriya', 'Male', 45)
patient4 = Patient(15, 'Ravi', 'Diabetes', 'Male', 25)

