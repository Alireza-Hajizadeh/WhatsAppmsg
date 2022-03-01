import subprocess
#Alireza-Hajizadeh
#send whatsapp msg Menu
import pyfiglet

ascii_banner = pyfiglet.figlet_format("WhatsAppmsg")
print(ascii_banner)
print ("Alireza Hajizadeh")



menu_options = {
    1: 'Send Whatsapp msg               | ',
    2: 'Send Whatsapp msg  with timer   | ',
    3: 'Send Whatsapp media             | ',
    0: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-->', menu_options[key] )

def option1():
     print(f'Handle option {menu_options[1]}')
     subprocess.call('python3 sendinstantly.py', shell=True)


def option2():
     print(f'Handle option {menu_options[2]}')
     subprocess.call('python3 sendontime.py', shell=True)

def option3():
     print(f'Handle option {menu_options[3]}')
     subprocess.call('python3 sendmedia.py', shell=True)

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
            print("")
            print(':D Thanks for using this Script <3')
            print("")
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')