from Teacher import Teacher

class Tec:
    def __init__(self):
        self.teachers = []
        
    def createTeacher(self):
        name = input("Angiv Lærens fornavn: ")
        lastname = input("Angiv Lærens efternavn: ")
        print("Vælg et fag fra listen")
        print("[1] Iot Embedded")
        print("[2] Python")
        print("[3] BigData")
        print("[4] Softwaresikkerhed og test")
        print("[5] Serversideprogrammering")
        subject_choice = input("Vælg et fag fra listen: ")
        
        subjects = {
            '1': "Iot Embedded",
            '2': "Python",
            '3': "BigData",
            '4': "Softwaresikkerhed og test",
            '5': "Serversideprogrammering"
        }
        subject = subjects.get(subject_choice)
        if subject:
            teacher = Teacher(name, lastname, [subject])
            self.teachers.append(teacher)
            print(f"{name} {lastname} er nu oprettet som lærer med følgende fag: {subject}")
        else:
            print("Ugyldigt fagvalg. Vælg venligst et fag fra listen.")




    def addTeacherSubject(self, teacher):
     print("Tilføj fag til læreren:")
     print("[1] Iot Embedded")
     print("[2] Python")
     print("[3] BigData")
     print("[4] Softwaresikkerhed og test")
     print("[5] Serversideprogrammering")
     subject_choice = input("Vælg et fag fra listen: ")
     subjects = {
        '1': "Iot Embedded",
        '2': "Python",
        '3': "BigData",
        '4': "Softwaresikkerhed og test",
        '5': "Serversideprogrammering"
     }
     subject = subjects.get(subject_choice)
     if subject:
        if subject not in teacher.subjects:
            teacher.subjects.append(subject)
            print(f"{subject} er tilføjet til {teacher.name} {teacher.lastname}'s fag.")
        else:
            print(f"{teacher.name} {teacher.lastname} underviser allerede i {subject}.")
     else:
        print("Ugyldigt fagvalg. Vælg venligst et fag fra listen.")







    def updateTeacherSubjects(self):
        if not self.teachers:
            print("There are no teachers to update.")
            return
        
        print("List of Teachers:")
        for t, teacher in enumerate(self.teachers, start=1):
            print(f"[{t}] {teacher.name} {teacher.lastname}")
        
        teacher_index = input("Vælg en lærer fra listen: ")
        if teacher_index.isdigit():
            teacher_index = int(teacher_index) - 1
            if 0 <= teacher_index < len(self.teachers):
                teacher = self.teachers[teacher_index]
                print(f"{teacher.name} {teacher.lastname} har følgende fag: {teacher.subjects}")
                print("[1] Tilføj flere fag")
                print("[2] Slet et fag")
                choice = input("Vælg 1 eller 2 :")
                if choice == '1':
                    self.addTeacherSubject(teacher)
                elif choice == '2':
                    self.deleteTeacherSubject(teacher)
                else:
                    print("Ugyldigt valg.")
            else:
                print("Ugyldigt lærer nummer.")
        else:
            print("Ugyldigt input. Indtast venligst et tal.")



    


    def deleteTeacherSubject(self, teacher):
     if not teacher.subjects:
        print("Der er ingen fag at slette.")
        return

     print(f"{teacher.name} {teacher.lastname} har følgende fag:")
     for i, subject in enumerate(teacher.subjects, start=1):
        print(f"[{i}] {subject}")

     choice = input("Vælg et fagnummer for at slette faget: ")
     if choice.isdigit():
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(teacher.subjects):
            deleted_subject = teacher.subjects.pop(choice_index)
            print(f"{deleted_subject} slettet fra {teacher.name} {teacher.lastname}'s fag.")
        else:
            print("Ugyldigt fagnummer.")
     else:
        print("Ugyldigt input. Indtast venligst et tal.")


    def displayallTeachers(self):
        if not self.teachers:
            print("Der er ingen Lærer .")
            return
        print("Liste af Lærer")
        for t, teacher in enumerate(self.teachers, start=1):
            print(f"Lærer {t}")
            teacher.display_info()  
    
    
    
    def start(self):     
        while True:
            print("[1] Opret Lærer")
            print("[2] Opdater lærer")
            print("[3] Vis list af alle lærer")
            print("[4] Exit")
            choice = input("Vælg 1, 2, 3, eller 4: ")
            
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    self.createTeacher()
                elif choice == 2:
                    self.updateTeacherSubjects()
                elif choice == 3:
                    self.displayallTeachers()
                elif choice == 4:
                    print("Programmet afsluttes.")
                    break
                else:
                    print("Ugyldigt valg")
            else:
                print("Ugyldigt valg. Indtast venligst et tal.")

def main():
    tec = Tec()
    tec.start()

if __name__ == "__main__":
    main()
