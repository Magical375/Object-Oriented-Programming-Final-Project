### by Dung Ngok Kenneth Li ID 888298
class Facility:
         
    def add_facility(self):
        # Adds and writes the facility name to the file
        print("Enter Facility name:")
        facility_name = input()
        f = open ("facilities.txt", 'a')
        f.write('\n'+facility_name)
          
    
    
    def display_facilities_list(self):
        # loop the facility list to print out facility name
                          
        f = open("facilities.txt", 'r')
        file_content = f.readlines()
        for line in file_content:
            print(line, end='\n')
        f.close()
              


while True:
    #  call read_facilities_file() to load facility data to a list first
    print('1 - Display Facilities list')
    print('2 - Add Facility')
    print('3 - Back to the Main Menu')
    option = int(input('\n'))
            
    if (option == 1):
        Facility().display_facilities_list()
        
    elif (option == 2):
        Facility().add_facility()
        
    else:
        continue
    print('\n''Back to the prevoius Menu')            
           
        
            