class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print(f"Name : {self.name}, Age : {self.age}")
class Patient(Person):
    def __init__(self, name, age,patient_id,illness):
        super().__init__(name, age)
        self.patient_id=patient_id
        self.illness=illness
    def show_info(self):
         super().show_info()
         print(f" ID  : {self.patient_id},  Illness  : {self.illness}")
class Doctor(Person):
    def __init__(self, name, age,doctor_id,speciality):
        super().__init__(name, age)
        self.doctor_id=doctor_id
        self.speciality=speciality
    def show_info(self):
         super().show_info()
         print(f"Doctor ID : {self.doctor_id} , Doctor Speciality : {self.speciality}")
class Appointment:
    def __init__(self,date,time,patient,doctor):
        self.date=date
        self.time=time
        self.patient=patient
        self.doctor=doctor
    def show_details(self):
        print(f"Appintment date : {self.date}")
        print(f"Appintment time : {self.time}")
        print(f"Patient name is {self.patient.name}")
        print(f"Patient ID : {self.patient.patient_id}")
        print(f"Doctor name : {self.doctor.name}")
        print(f"Doctor ID :{self.doctor.doctor_id}")
patient_list=[]
doctor_list=[]
appointment_list=[]
while True:
    print("**Welcome to our App**")
    print("-"*25)
    print("1-Add patient")
    print("-"*25)
    print("2-Add doctor")
    print("-"*25)
    print("3-Book appointment")
    print("-"*25)
    print("4-Show patients")
    print("-"*25)
    print("5-Show doctors")
    print("-"*25)
    print("6-Show appointment")
    print("-"*25)
    print("7-Search patient")
    print("-"*25)
    print("8-Delet patient")
    print("-"*25)
    print("9-Exit")
    print("-"*25)
    choice=input("Enter number of operation : ")
    if choice=="1":
        print("Follow all steps to add new patient")
        name=input("Enter your name : ")
        age=int(input("Enter your age : "))
        id=int(input("Enter your ID : "))
        illness=input("Enter your illness :")
        new_patient=Patient(name,age,id,illness)
        patient_list.append(new_patient)
        print("Patient added")
    elif choice=="2":
        print("Follow all steps to add new doctor")
        name=input("Enter your name : ")
        age=int(input("Enter your age : "))
        id=int(input("Enter your ID : "))
        sepciality=input("Enter doctor speciality : ")
        new_doctor=Doctor(name,age,id,sepciality)
        doctor_list.append(new_doctor)
        print("doctor added")
    elif choice=="3":
            print("Follow all steps to book appintment")
            date=input("Enter date follow this form (1-1-1988) : ")
            time=input("Enter time follow this form (13:50)")
            patinet_name=input("Enter patient name : ")
            selected_patient=None
            for p in patient_list:
                if p.name.lower().strip()==patinet_name.lower().strip():
                    selected_patient=p
                    break
            doctor_name=input("Enter doctor name : ")
            selected_doctor=None
            for d in doctor_list:
                if d.name.lower().strip()==doctor_name.lower().strip():
                    selected_doctor=d
                    break
            if selected_patient and selected_doctor:
                book_appointment=Appointment(
                    date,
                    time,
                    selected_patient,
                    selected_doctor
                )
                appointment_list.append(book_appointment)
                print("appointment is booked")
            else:
                print("selcted patient or doctor not found")
    elif choice=="4":
        print("patients list : ")
        print("*"*25)
        if not patient_list:
            print("NO patients in the list")
        else:
            for patient in patient_list:
                patient.show_info()
                print("-"*25)
    elif choice=="5":
        print("Doctor list : ")
        if not doctor_list:
            print("No doctors in the list")
        else:
            for doctor in doctor_list:
                doctor.show_info()
                print("-"*25)
    elif choice=="6":
        print("Appointment lsit :")
        if not appointment_list:
            print("No appointment in the list")
        else:
            for appointmnet in appointment_list:
                appointmnet.show_details()
                print("-"*25)
    elif choice=="7":
        print("Follow all steps to find a patient")
        print("*"*25)
        patient_name=input("Enter full name of patient : ")
        found_patient=None
        for p in patient_list:
             if p.name.lower().strip()==patient_name.lower().strip():
                found_patient=p
                break
        if found_patient:
            found_patient.show_info()
        else:
            print("Patient not found")
    elif choice=="8":
        print("follow all steps to delet patient")
        print("*"*25)
        delete_patient=input("Enter patient full name : ")
        found_patient=None
        for p in patient_list:
            if p.name.lower().strip()==delete_patient.lower().strip():
                found_patient=p
                break
        if found_patient:
            print("patient deleted")
            patient_list.remove(found_patient)
        else:
            print("Patient not existe")
    elif choice=="9":
        print("You press exit")
        print("*"*25)
        print("Thank you for choose our programe")
        print("Codeflow,Mohamed wassim tatari")
        break
    else:
        print("invalid operation please choisse a number existe")

                

            
            
        
        

            





               
    