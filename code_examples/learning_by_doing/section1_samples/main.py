""" 
Executes samples that show the use of basic Python syntax.
Adapted from [How to create a menu for a python console application?](https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/)
"""
import sys
  
""" 
Append the path to the modules location.
This is important to allow pdoc to find the modules. 
"""
sys.path.append('./code_examples/learning_by_doing/section1_samples')

from exercise4_type_error import type_error 

# Define the menu dictionary. 
menu_options = {
    1: 'Issue type error message',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    " Prints the menu. "
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

def main():
    """
    Displays menu and processes user's input.
    It calls the proper function based on the user's selection.
    """
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            type_error()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Goodbye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

if __name__=='__main__':
   main()