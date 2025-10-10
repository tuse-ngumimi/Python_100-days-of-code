<<<<<<< HEAD

"""
File Finder - Main Application
A command-line utility for searching files and folders on the computer.
"""

from typing import Dict, Any
from dict_config import initialize_config, display_config, edit_settings
from menus import display_main_menu, get_menu_choice
from search import search_files_and_folders
from display import display_paginated_results


def main() -> None:
    """
    Main application loop that handles the primary user interface.
    Continuously displays the main menu and processes user choices until exit.
    """
    print("=" * 50)
    print("     Welcome to File Finder")
    print("=" * 50)
    print()
    
    # Initialize configuration
    config: Dict[str, Any] = initialize_config()
    
    while True:
        # Display main menu
        display_main_menu()
        
        # Get user choice
        choice = get_menu_choice(1, 4)
        
        if choice == 1:
            # Search for files/folders
            handle_search(config)
        elif choice == 2:
            # View current settings
            display_config(config)
        elif choice == 3:
            # Edit settings
            edit_settings(config)
        elif choice == 4:
            # Exit
            print("\nThank you for using File Finder! Goodbye!")
            break
        
        print() 


def handle_search(config: Dict[str, Any]) -> None:
    """
    Handle the file search functionality.
    
    Args:
        config: The configuration dictionary containing search settings
    """
    print("\n" + "=" * 30)
    print("     File Search")
    print("=" * 30)
    
    # Get search query from user
    query = input("Enter search term (filename): ").strip()
    
    if len(query) == 0:
        print("Error: Search term cannot be empty!")
        return
    
    print(f"\nSearching for '{query}' in {config['root_path']}...")
    print("Please wait...")
    
  
    results = search_files_and_folders(query, config)
    
    if len(results) == 0:
        print("No matching files or folders found.")
        return
    
    # Display results with pagination
    display_paginated_results(results, config)


if __name__ == "__main__":
=======

"""
File Finder - Main Application
A command-line utility for searching files and folders on the computer.
"""

from typing import Dict, Any
from dict_config import initialize_config, display_config, edit_settings
from menus import display_main_menu, get_menu_choice
from search import search_files_and_folders
from display import display_paginated_results


def main() -> None:
    """
    Main application loop that handles the primary user interface.
    Continuously displays the main menu and processes user choices until exit.
    """
    print("=" * 50)
    print("     Welcome to File Finder")
    print("=" * 50)
    print()
    
    # Initialize configuration
    config: Dict[str, Any] = initialize_config()
    
    while True:
        # Display main menu
        display_main_menu()
        
        # Get user choice
        choice = get_menu_choice(1, 4)
        
        if choice == 1:
            # Search for files/folders
            handle_search(config)
        elif choice == 2:
            # View current settings
            display_config(config)
        elif choice == 3:
            # Edit settings
            edit_settings(config)
        elif choice == 4:
            # Exit
            print("\nThank you for using File Finder! Goodbye!")
            break
        
        print() 


def handle_search(config: Dict[str, Any]) -> None:
    """
    Handle the file search functionality.
    
    Args:
        config: The configuration dictionary containing search settings
    """
    print("\n" + "=" * 30)
    print("     File Search")
    print("=" * 30)
    
    # Get search query from user
    query = input("Enter search term (filename): ").strip()
    
    if len(query) == 0:
        print("Error: Search term cannot be empty!")
        return
    
    print(f"\nSearching for '{query}' in {config['root_path']}...")
    print("Please wait...")
    
  
    results = search_files_and_folders(query, config)
    
    if len(results) == 0:
        print("No matching files or folders found.")
        return
    
    # Display results with pagination
    display_paginated_results(results, config)


if __name__ == "__main__":
>>>>>>> 38784bedb3032e34d3265a47b814b8d1ad0b14bb
    main()