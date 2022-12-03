# create laboratory class and functions
'''
3


Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu
'''

class Laboratory:


    def __init__(self, lab, cost):

        self.lab = lab
        self.cost = cost


    def append_text_data(self):

        text_data = object.lab + '_' + object.cost
        with open('laboratories.txt', 'a') as f:
            f.write('\n' + text_data)


    def format_data_print():

        with open('laboratories.txt') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip().split('_')
                print(line[0] + '\t\t\t' + line[1])


    def menu():

        while True:
            try:
                option = int(input('\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n'))
                
                if option == 1:
                    print('\n')
                    Laboratory.format_data_print()
                    print('\nBack to the previous Menu')
                    continue

                elif option == 2:
                    print('\n')
                    global object
                    object = Laboratory(input("Enter Laboratory facility: "), input("Enter Laboratory cost: "))
                    object.append_text_data()
                    Laboratory.format_data_print()
                    print('\nBack to the previous Menu')
                    continue

                elif option == 3:
                    #return to main menu of classes
                    break
            except:
                continue
