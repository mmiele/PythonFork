""" 
Examples showing the use of list. 

Remarks
-------

A list can be written as a list of comma-separated values (items) between square brackets.
Lists might contain items of different types, but usually the all have 
the same type.
For more information, see
[List](https://docs.python.org/3/library/stdtypes.html#lists).

"""

from typing import OrderedDict

# Define a list.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Define a list with duplicated elements.
letters_duplicated = ["a", "b", "b", "d", "d", "f", "g", "h", "h", "j", "j"]

def get_list_item(index:int):
    """
    Display the item of a list at the specified index. 

    Parameters
    ----------
    index : int 
        The index of the element to display.

    Remarks
    -------
    Every item of a list is referenced with an index number starting from zero
    and increasing by one. 

    Besides the left-to-right positive indexing that starts from zero,
    list data types such as lists also have a second indexing system that
    starts from -1 and decreases by one from right-to-left. 

    """
    
    # Display the requested item. 
    try:
        item = letters[index]
        print(f"The item at index {index} is: {item}") 
    except Exception as error:
        print(f"{type(error).__name__} was raised: {index} {error}") 

def get_list_range_items(lower_bound: int, upper_bound: int):
    """
    Displays the items of a list in the specified range. 

    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.

    Remarks
    -------
    The list slicing syntax is upper-bound exclusive. For example, if you
    want to include the element whose index is 5, you need to pass 6 as the upper bound.

    """
    
    # Display the elements in the requested range. 
    try:
        range_items = str(letters[lower_bound:upper_bound+1])
        print(f"The items in the specified range are: {range_items}") 
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 


def get_list_negative_range_items(lower_bound: int, upper_bound: int):
    """
    Displays the items of a list in the specified range. 

    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.    

    Remarks
    -------
    The list slicing syntax is upper-bound exclusive. For example, if you
    want to include the element whose index is 5, you need to pass 6 as the upper bound.

    """
    
    # Display the elements in the requested range. 
    try:
        range_items = str(letters[lower_bound:upper_bound])
        print(f"The items in the specified range are: {range_items}") 
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 

def get_list_range_items_in_steps(lower_bound: int, upper_bound: int, step: int):
    """
    Displays the items of a list in the specified range, using the specified
    step. 
    
    Parameters
    ----------
    lower_bound : int 
        The index of the first element in the range.
    upper_bound : int 
        The index of the last element in the range.    
    step : int 
        The step to use when returning the elements. For example, if the step is
        2 every other item in the range is
        returned.

    Remarks
    -------
    The complete syntax of list slicing is [start:end:step] . When you don't
    pass a step, Python assumes the step is 1. [:]  itself means to get
    everything from start to end. So, [::2]  means get everything from start to
    end at a step of two.
    """
    
    # Display the elements in the requested range with the specified step.
    try:
        range_items = str(letters[lower_bound:upper_bound:step])
        print(f"The items in the specified range are: {range_items}") 
    except Exception as error:
        print(f"{type(error).__name__} was raised: {error}") 

def create_number_list(first_number: int, last_number: int):
    """
    Create a list of numbers in the specified number range. 

    Parameters
    ----------
    first_number : int 
        The value of the first number in the list.
    last_number : int 
        The value of the last number in the list.    

    Remarks
    -------
    This example uses the Python built-in function `range()` that generates a range of integers. 
    However, `range()` creates a Python range object. To get the list object, the example uses 
    the `list()` function to convert the range object into a list object.

    """
    
    try:
        # Get the range object. 
        my_range = range(first_number, last_number)
        # Get the related list.
        my_list = list(my_range)
        print(f"The list from {first_number} and {last_number} is: {my_list}") 
    except Exception as error:
        # Display the error.
        print(f"{type(error).__name__} was raised: {error}") 
    
def create_number_list_in_range(arange: range):
    """
    Create a list of numbers in the specified range. 

    Parameters
    ----------
    arange : range
        The range to create the number list.
    
    Remarks
    -------
    This example accepts a Python range object, as a parameter. To get the list
    object, the example uses the Pythonthe list comprehension construct to
    convert the range object into a list object.  For more information, see
    [list comprehension](https://realpython.com/list-comprehension-python/). 

    """
    
    try:
        # Create a list of numbers in the specified range. 
        my_list = [10 * n for n in arange]
        print(f"The list in the {arange} is: {my_list}") 
    except Exception as error:
        # Display the error.
        print(f"{type(error).__name__} was raised: {error}") 
       
def create_string_list_in_range(arange: range):
    """
    Create a list of strings in the specified range. 

    Parameters
    ----------
    arange : range
        The range to create the number list.
    
    Remarks
    -------
    This example accepts a Python range object, as a parameter. To get the list
    object, the example uses the Python built-in function 'map()` to transform
    each mumber in the iteratable object `arange` in a string and then appliese
    the function `list()` to convert the output into a list object containing
    strings. 

    For more information, see [map
    function](https://www.w3schools.com/python/ref_func_map.asp).
    """
    
    try:
        # Create a list of numbers in the specified range. 
        my_list = list(map(str, arange))
        # my_list = [str(10 * n) for n in arange]
        print(f"The list in the {arange} is: {my_list}") 
    except Exception as error:
        # Display the error.
        print(f"{type(error).__name__} was raised: {error}") 
      

def remove_duplicated_list_elements():
    """
    Remove duplicated elments in a lists.  

    Parameters
    ----------
    arange : range
        The range to create the number list.
    
    Remarks
    -------
    To remove deplicated elements in a list, you can use one of the following
    approaches: 1. Use the  `set` function to convert the list to a set that
    would remove all duplicates because `set` objects cannot contain duplicates.
    Then use the `list` function to convert the set back to a list. The drawback
    here is that the original order of the items is lost.

    For more information, see [set
    function](https://www.w3schools.com/python/ref_func_set.asp).
    """

    try:
        # Method 1: using set.  
        my_set = set(letters_duplicated)
        my_list = list(my_set)
        print(f"Using set function. The unordered list is: {my_list}") 

        my_dictionary = OrderedDict.fromkeys(letters_duplicated)
        my_list = list(my_dictionary)
        print(f"Using OrderedDict.fromkeys function. The ordered list is: {my_list}") 
    except Exception as error:
        # Display the error.
        print(f"{type(error).__name__} was raised: {error}") 

def index_list():
    """ 
    Perform basic index operations. 
    """

    # Define a list.
    my_list = ['p', 'r', 'o', 'b', 'e']
    print(f"The list is: {my_list}") 

    # At index 0 is : p
    print("At index 0 is : " + my_list[0])

    # At index 2 is : o
    print("At index 2 is : " + my_list[2])

    # At index 4 is : e
    print("At index 4 is : " + my_list[4])

    # Error!
    # List indices must be integers or slices, not float
    try:
        element = my_list[4.0]
    except Exception as error:
        # Display the error.
        print(f"{type(error).__name__} was raised: {error}") 

    # Negative indexing
    # The index -1 refers to the last element
    # The index -5 refers to the first element (in this example)

    # At index -1 is : e
    print("At index -1 is : " + my_list[-1])

    # At index -5 is : p
    print("At index -5 is : " + my_list[-5])

    # Create nested list
    n_list = ["Happy", [2, 0, 1, 5]]

    print(f"The nested list is: {n_list}") 

    # Nested indexing

    # In the nested list at index 0,1 is : a
    print("In the nested list at index 0, 1 is : " + n_list[0][1])

    # In the nested list at index 1,3 is : 5
    print("In the nested list at index 1,3 is : " + str((n_list[1][3])))

def change_list_element():
    """ 
    Change element in a list.
    
    Remarks
    -------
    
    Lists are mutable objects, meaning that their elements can be changed programmatically at run time,  unlike a string or a tuple.

    """ 

    # Define a list
    my_list = [2, 4, 6, 8]
    print(f"The list is: {my_list}") 

    # Change the first item
    my_list[0] = 1
    result = '{0} {1}'.format('Changed first item: ', str(my_list[:]))
    print(result)

    # Change 2nd to 4th items
    my_list[1:4] = [3, 5, 7]
    result = '{0} {1}'.format('Changed 2nd to 4th items: ', str(my_list[:]))
    print(result)

def add_list_element():
    """ 
    Add element to a list. 
    """

    # Define a list
    my_list = [1, 3, 5]
    print(f"The list is: {my_list}") 


    # Add an element to the list
    my_list.append(7)
    result = '{0} {1}'.format('Added one item to the list: ', str(my_list[:]))
    print(result)

    # Add several elements to the list
    my_list.extend([9, 11, 13])
    result = '{0} {1}'.format('Added several elements to the list: ', 
            str(my_list[:]))
    print(result)       

def slice_list():
    """ 
    Perform list slicing.
    
    Remarks
    -------

    Slicing can be best visualized by considering
    the index to be between the elements as shown below.

    0___1___2___3___4___5___6___7___8___9

    |P  |R  |O  |G  |R  |A  |M  |I  |Z  |
    
    -9 -8  -7  -6  -5  -4  -3  -2  -1
    
    So if we want to access a range, we need two index
    that will slice that portion from the list.
    
    """

    # Define the list. 
    my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
    print(f"The list is: {my_list}") 

    # Select elements 3rd to 5th
    print("Select 3rd to 5th element: " +  str(my_list[2:5]))

    # Select elements beginning to 4th
    print("Select 1st to 4th element: " + str(my_list[:-5]))

    # Select elements 6th to end
    print("Select 6th to end element: " + str(my_list[5:]))



