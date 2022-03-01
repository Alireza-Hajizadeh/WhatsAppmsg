import subprocess


menu_options = {
    1: 'Send Whatsapp msg (After time) : ',
    2: 'Send Whatsapp msg (In grup)    : ',
    3: 'Send Whatsapp img              :',
    0: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-->', menu_options[key] )

def option1():
     print(f'Handle option {menu_options[1]}')
     subprocess.call('python3 a.py', shell=True)


def option2():
     print(f'Handle option {menu_options[2]}')

def option3():
     print(f'Handle option {menu_options[3]}')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 0:
            print(':D Thanks for using this Script <3')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')