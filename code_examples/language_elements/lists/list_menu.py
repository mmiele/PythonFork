""" 
Executes the samples from the list group. 

"""

# Append the path to the modules location.
# This is important to allow pdoc to find the modules. 
import sys

sys.path.append('./code_examples/language_elements')

from create_menu import createMenu

from type_error import issue_type_error 
from list import get_list_item, get_list_range_items, create_number_list
from list import get_list_negative_range_items, get_list_range_items_in_steps
from list import create_number_list, create_number_list_in_range, create_string_list_in_range, remove_duplicated_list_elements

from dictionary import create_simple_dictionary, get_dictionary_element_value

# Define the menu item list.  
menuItems = ["Issue type error", "Index a list", "Slice a list", "Create a list", "Create a list in a range", "Create a string list in a range", 
"Remove duplicated list elments", "Create a simple dictionary",
"Get dictionary element value", "Quit"]

class listMenu:

    """ 
    Executes list group samples. 
    
    Remarks
    -------
    This class main nethod displays the menu to allow the user to select the samples to execute from the list group. 
    
    Use
    ---    

    From the main function perform the following steps:
    `amenu = listMenu()` # Instantiate the listMenu class.
    `amenu.listSelectionMenu()` # Dispkay the list samples selection menu.
  
    """
    def listSelectionMenu(self):
        """
            Display menu and process user's input.
            Call the proper method based on the user's selection.
        """
       
        # Instantiate the list menu class. 
        dsm = createMenu("List Menu")
        
        # Display the menu but ignore the user's choice.
        dummy = dsm.displayMenu(menuItems, True)

        while True:
            # Get the user's choice and do not display the menu.
            choice = dsm.displayMenu(menuItems, False)

            if choice == 1:
                print("\n**** Type error ****")
                issue_type_error()
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 2:
                print("\n*** Index a list ***")
                get_list_item(2)
                get_list_item(-2)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 3:
                print("\n*** Slice a list ***")
                get_list_range_items(3, 5)
                get_list_negative_range_items(-3, -1)
                get_list_range_items_in_steps(1, 10, 2)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 4:
                print("\n*** Create a list of numbers ***")
                create_number_list(1, 21)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 5:
                print("\n*** Create a list of numbers in a range ***")
                create_number_list_in_range(range(1, 21))
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 6:
                print("\n*** Create a list of strings in a range ***")
                create_string_list_in_range(range(1, 21))
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 7:
                print("\n*** Remove duplicated list elements ***")
                remove_duplicated_list_elements()
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 8:
                print("\n*** Create a simple dictionary ***")
                create_simple_dictionary("a", 1, "b", 2)
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == 9:
                print("\n*** Get dictionary element ***")
                d = dict(a=1, b=2)
                get_dictionary_element_value(d, "a")
                dummy = dsm.displayMenu(menuItems, True)
            elif choice == len(menuItems):
                break
