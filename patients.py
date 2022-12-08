class patients:
    def __init__(self, id, name, disease, gender, age):
        self.name = name
        self.id = id
        self.disease = disease
        self.gender = gender
        self.age = age


# patient_one = patients('Japsimran')


#print(patient_one)

#print(patient_one.name)
def format_print():
    with open('patients.txt') as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip().split("_")
            print(line[0]+'\t\t'+line[1]+'\t\t'+line[2]+'\t\t'+line[3]+'\t\t'+line[4])

def add_patient():
    new_patient = patients(input('enter your id\n'),input('enter your name\n'),input('enter your disease\n'),input('enter your gender\n'),input('enter your age\n'))
    new_patient_data=(new_patient.id+'_'+new_patient.name+'_'+new_patient.disease+'_'+new_patient.gender+'_'+new_patient.age)
    with open('patients.txt', 'a') as f:
        f.write('\n' + new_patient_data)

def check_id():
    id = (input("Enter the Id number what you have to find:\n"))

    with open('patients.txt') as f:
        lines = f.readlines()

        line_number_total = 0
        for line in lines:
            line = line.strip().split("_")
            line_number_total += 1
            line_number_check = 0
            

            for line[0] in line:
                
                while line_number_check != line_number_total:
                    try:
                        if line[0] == id:
                            print('\n'+line[0]+'\t\t'+line[1]+'\t\t'+line[2]+'\t\t'+line[3]+'\t\t'+line[4])
                            return

                        elif line[0] != id:
                            line_number_check += 1

                    except:
                        continue
        if line_number_check == line_number_total:
            print("Can't find the Patient with the same id on the system")



def edit_id():

    id = input("Please enter the id of the Patient that you want to edit their information:\n")

    with open('patients.txt','r+') as f:
        lines = f.readlines()

        global line_number_total
        line_number_total = 0
        for line in lines:
            line = line.strip().split("_")
            line_number_total += 1
            line_number_check = 0
            

            for line[0] in line:
                
                while line_number_check != line_number_total:
                    try:
                        if line[0] == id:
                            line[0] = input('Enter new ID\n')
                            line[1] = input('Enter new name\n')
                            line[2] = input('Enter new Disease\n')
                            line[3] = input('Enter new gender\n')
                            line[4] = input('Enter new age\n')
                            global edited_text
                            edited_text = (line[0]+'_'+line[1]+'_'+line[2]+'_'+line[3]+'_'+line[4])
                            return

                        elif line[0] != id:
                            line_number_check += 1

                    except:
                        continue
            
        if line_number_check == line_number_total:
            print("Can't find the Patient with the same id on the system")

def edit_line():

    with open('patients.txt','r') as f:
        data = f.readlines()


    data[line_number_total - 1] = edited_text + '\n'

    with open('patients.txt','w') as f:
        f.writelines(data)

def menu():

        while True:
            try:
                option = int(input('\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n'))
                if option == 1:
                    print('\n')
                    format_print()
                    print('\nBack to the previous Menu')
                    continue

                elif option == 2:
                    print('\n')
                    check_id()
                    print('\nBack to the previous Menu')
                    continue

                elif option == 3:
                    print('\n')
                    add_patient()
                    print('\nBack to the previous Menu')
                    continue

                elif option == 4:
                    print('\n')
                    edit_id() 
                    edit_line()
                    print('\nBack to the previous Menu')
                    continue
                
                elif option == 5:
                    break
            except:
                continue

menu()