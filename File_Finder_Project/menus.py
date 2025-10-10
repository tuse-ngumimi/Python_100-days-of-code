<<<<<<< HEAD
"""
Menu display and user input handling for File Finder application.
Provides functions for displaying menus and getting validated user input.
"""

# from typing import int


def display_main_menu() -> None:
    """
    Display the main menu options to the user.
    """
    print("=" * 30)
    print("        Main Menu")
    print("=" * 30)
    print("1. Search for a File/Folder")
    print("2. View Current Settings")
    print("3. Edit Settings")
    print("4. Exit")
    print("=" * 30)


def get_menu_choice(min_choice: int, max_choice: int) -> int:
    """
    Get a validated menu choice from the user.
    Continues prompting until a valid choice is entered.
    
    Args:
        min_choice: The minimum valid choice number
        max_choice: The maximum valid choice number
        
    Returns:
        int: The validated user choice
    """
    while True:
        try:
            choice = int(input(f"Enter your choice ({min_choice}-{max_choice}): "))
            
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print(f"Error: Please enter a number between {min_choice} and {max_choice}.")
        
        except ValueError:
            print("Error: Please enter a valid number.")


def display_pagination_menu(current_page: int, total_pages: int, has_prev: bool, has_next: bool) -> None:
    """
    Display pagination menu options.
    
    Args:
        current_page: The current page number (1-based)
        total_pages: The total number of pages
        has_prev: Whether there is a previous page available
        has_next: Whether there is a next page available
    """
    print("\n" + "-" * 40)
    print(f"Page {current_page} of {total_pages}")
    print("-" * 40)
    
    option_count = 1
    
    if has_prev:
        print(f"{option_count}. Previous Page")
        option_count += 1
    
    if has_next:
        print(f"{option_count}. Next Page")
        option_count += 1
    
    print(f"{option_count}. Return to Main Menu")
    print("-" * 40)


def get_pagination_choice(has_prev: bool, has_next: bool) -> str:
    """
    Get user's pagination choice and return the action.
    
    Args:
        has_prev: Whether there is a previous page available
        has_next: Whether there is a next page available
        
    Returns:
        str: The chosen action ('prev', 'next', or 'menu')
    """
    max_option = 1
    options = []
    
    if has_prev:
        options.append('prev')
        max_option += 1
    
    if has_next:
        options.append('next')
        max_option += 1
    
    options.append('menu')
    
    choice = get_menu_choice(1, max_option)
    
=======
"""
Menu display and user input handling for File Finder application.
Provides functions for displaying menus and getting validated user input.
"""

# from typing import int


def display_main_menu() -> None:
    """
    Display the main menu options to the user.
    """
    print("=" * 30)
    print("        Main Menu")
    print("=" * 30)
    print("1. Search for a File/Folder")
    print("2. View Current Settings")
    print("3. Edit Settings")
    print("4. Exit")
    print("=" * 30)


def get_menu_choice(min_choice: int, max_choice: int) -> int:
    """
    Get a validated menu choice from the user.
    Continues prompting until a valid choice is entered.
    
    Args:
        min_choice: The minimum valid choice number
        max_choice: The maximum valid choice number
        
    Returns:
        int: The validated user choice
    """
    while True:
        try:
            choice = int(input(f"Enter your choice ({min_choice}-{max_choice}): "))
            
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print(f"Error: Please enter a number between {min_choice} and {max_choice}.")
        
        except ValueError:
            print("Error: Please enter a valid number.")


def display_pagination_menu(current_page: int, total_pages: int, has_prev: bool, has_next: bool) -> None:
    """
    Display pagination menu options.
    
    Args:
        current_page: The current page number (1-based)
        total_pages: The total number of pages
        has_prev: Whether there is a previous page available
        has_next: Whether there is a next page available
    """
    print("\n" + "-" * 40)
    print(f"Page {current_page} of {total_pages}")
    print("-" * 40)
    
    option_count = 1
    
    if has_prev:
        print(f"{option_count}. Previous Page")
        option_count += 1
    
    if has_next:
        print(f"{option_count}. Next Page")
        option_count += 1
    
    print(f"{option_count}. Return to Main Menu")
    print("-" * 40)


def get_pagination_choice(has_prev: bool, has_next: bool) -> str:
    """
    Get user's pagination choice and return the action.
    
    Args:
        has_prev: Whether there is a previous page available
        has_next: Whether there is a next page available
        
    Returns:
        str: The chosen action ('prev', 'next', or 'menu')
    """
    max_option = 1
    options = []
    
    if has_prev:
        options.append('prev')
        max_option += 1
    
    if has_next:
        options.append('next')
        max_option += 1
    
    options.append('menu')
    
    choice = get_menu_choice(1, max_option)
    
>>>>>>> 38784bedb3032e34d3265a47b814b8d1ad0b14bb
    return options[choice - 1]