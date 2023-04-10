

def display_menu():
    main_menu = {'1':'Doctors',
                '2':'Patients',
                '3':'Exit Program'}

    doctors_menu = {'1':'Display Doctor List',
                   '2':'Search Doctor By ID',
                   '3':'Search Doctor By Name',
                   '4':'Add New Doctor',
                   '5':'Edit Existing Doctor Information',
                   '6':'Main Menu'}

    patients_menu = {'1':'Display Patient List',
                    '2':'Search by ID',
                    '3':'Add New Patient',
                    '4':'Edit Existing Patient Information',
                    '5':'Main Menu'}

    do_main_menu = True
    do_doctor_menu = True
    do_patient_menu = True

    while do_main_menu:
        choice = input(main_menu)

        if choice in main_menu:
            choice = input(doctors_menu)



