<<<<<<< HEAD
"""
Configuration management for File Finder application.
Handles initialization and modification of application settings.
"""

from typing import Dict, Any
from pathlib import Path


def initialize_config() -> Dict[str, Any]:
    """
    Initialize the configuration dictionary with default values.
    
    Returns:
        Dict[str, Any]: Configuration dictionary with default settings
    """
    # Get user's Documents folder as default root path
    documents_path = Path.home() / "Documents"
    
    config = {
        'root_path': str(documents_path),
        'case_sensitive': True,
        'display_size': 10
    }
    
    return config


def display_config(config: Dict[str, Any]) -> None:
    """
    Display the current configuration settings.
    
    Args:
        config: The configuration dictionary to display
    """
    print("\n" + "=" * 30)
    print("     Current Settings")
    print("=" * 30)
    print(f"Root Search Path: {config['root_path']}")
    print(f"Case Sensitive: {'Yes' if config['case_sensitive'] else 'No'}")
    print(f"Results Per Page: {config['display_size']}")
    print("=" * 30)


def edit_settings(config: Dict[str, Any]) -> None:
    """
    Allow user to edit configuration settings.
    
    Args:
        config: The configuration dictionary to modify
    """
    while True:
        print("\n" + "=" * 30)
        print("     Edit Settings")
        print("=" * 30)
        print("1. Change Root Search Path")
        print("2. Toggle Case Sensitivity")
        print("3. Change Results Per Page")
        print("4. Return to Main Menu")
        print("=" * 30)
        
        from menus import get_menu_choice
        choice = get_menu_choice(1, 4)
        
        if choice == 1:
            change_root_path(config)
        elif choice == 2:
            toggle_case_sensitivity(config)
        elif choice == 3:
            change_display_size(config)
        elif choice == 4:
            break


def change_root_path(config: Dict[str, Any]) -> None:
    """
    Change the root search path after validating the new path.
    
    Args:
        config: The configuration dictionary to modify
    """
    print(f"\nCurrent root path: {config['root_path']}")
    new_path = input("Enter new root path (or press Enter to cancel): ").strip()
    
    if len(new_path) == 0:
        print("Operation cancelled.")
        return
    
    if validate_root_path(new_path):
        config['root_path'] = new_path
        print(f"Root path successfully changed to: {new_path}")
    else:
        print("Root path not changed.")


def validate_root_path(path_str: str) -> bool:
    """
    Validate that a path exists and is a directory.
    
    Args:
        path_str: The path string to validate
        
    Returns:
        bool: True if path is valid, False otherwise
    """
    path = Path(path_str)
    
    if not path.exists():
        print(f"Error: The path '{path}' does not exist.")
        return False
    
    if not path.is_dir():
        print(f"Error: The path '{path}' is not a directory.")
        return False
    
    return True


def toggle_case_sensitivity(config: Dict[str, Any]) -> None:
    """
    Toggle the case sensitivity setting.
    
    Args:
        config: The configuration dictionary to modify
    """
    config['case_sensitive'] = not config['case_sensitive']
    status = "enabled" if config['case_sensitive'] else "disabled"
    print(f"Case sensitivity {status}.")


def change_display_size(config: Dict[str, Any]) -> None:
    """
    Change the number of results displayed per page.
    
    Args:
        config: The configuration dictionary to modify
    """
    print(f"Current results per page: {config['display_size']}")
    
    while True:
        try:
            new_size = int(input("Enter new display size (3-20, or 0 to cancel): "))
            
            if new_size == 0:
                print("Operation cancelled.")
                return
            
            if 3 <= new_size <= 20:
                config['display_size'] = new_size
                print(f"Display size changed to {new_size} results per page.")
                return
            else:
                print("Error: Display size must be between 3 and 20.")
        
        except ValueError:
=======
"""
Configuration management for File Finder application.
Handles initialization and modification of application settings.
"""

from typing import Dict, Any
from pathlib import Path


def initialize_config() -> Dict[str, Any]:
    """
    Initialize the configuration dictionary with default values.
    
    Returns:
        Dict[str, Any]: Configuration dictionary with default settings
    """
    # Get user's Documents folder as default root path
    documents_path = Path.home() / "Documents"
    
    config = {
        'root_path': str(documents_path),
        'case_sensitive': True,
        'display_size': 10
    }
    
    return config


def display_config(config: Dict[str, Any]) -> None:
    """
    Display the current configuration settings.
    
    Args:
        config: The configuration dictionary to display
    """
    print("\n" + "=" * 30)
    print("     Current Settings")
    print("=" * 30)
    print(f"Root Search Path: {config['root_path']}")
    print(f"Case Sensitive: {'Yes' if config['case_sensitive'] else 'No'}")
    print(f"Results Per Page: {config['display_size']}")
    print("=" * 30)


def edit_settings(config: Dict[str, Any]) -> None:
    """
    Allow user to edit configuration settings.
    
    Args:
        config: The configuration dictionary to modify
    """
    while True:
        print("\n" + "=" * 30)
        print("     Edit Settings")
        print("=" * 30)
        print("1. Change Root Search Path")
        print("2. Toggle Case Sensitivity")
        print("3. Change Results Per Page")
        print("4. Return to Main Menu")
        print("=" * 30)
        
        from menus import get_menu_choice
        choice = get_menu_choice(1, 4)
        
        if choice == 1:
            change_root_path(config)
        elif choice == 2:
            toggle_case_sensitivity(config)
        elif choice == 3:
            change_display_size(config)
        elif choice == 4:
            break


def change_root_path(config: Dict[str, Any]) -> None:
    """
    Change the root search path after validating the new path.
    
    Args:
        config: The configuration dictionary to modify
    """
    print(f"\nCurrent root path: {config['root_path']}")
    new_path = input("Enter new root path (or press Enter to cancel): ").strip()
    
    if len(new_path) == 0:
        print("Operation cancelled.")
        return
    
    if validate_root_path(new_path):
        config['root_path'] = new_path
        print(f"Root path successfully changed to: {new_path}")
    else:
        print("Root path not changed.")


def validate_root_path(path_str: str) -> bool:
    """
    Validate that a path exists and is a directory.
    
    Args:
        path_str: The path string to validate
        
    Returns:
        bool: True if path is valid, False otherwise
    """
    path = Path(path_str)
    
    if not path.exists():
        print(f"Error: The path '{path}' does not exist.")
        return False
    
    if not path.is_dir():
        print(f"Error: The path '{path}' is not a directory.")
        return False
    
    return True


def toggle_case_sensitivity(config: Dict[str, Any]) -> None:
    """
    Toggle the case sensitivity setting.
    
    Args:
        config: The configuration dictionary to modify
    """
    config['case_sensitive'] = not config['case_sensitive']
    status = "enabled" if config['case_sensitive'] else "disabled"
    print(f"Case sensitivity {status}.")


def change_display_size(config: Dict[str, Any]) -> None:
    """
    Change the number of results displayed per page.
    
    Args:
        config: The configuration dictionary to modify
    """
    print(f"Current results per page: {config['display_size']}")
    
    while True:
        try:
            new_size = int(input("Enter new display size (3-20, or 0 to cancel): "))
            
            if new_size == 0:
                print("Operation cancelled.")
                return
            
            if 3 <= new_size <= 20:
                config['display_size'] = new_size
                print(f"Display size changed to {new_size} results per page.")
                return
            else:
                print("Error: Display size must be between 3 and 20.")
        
        except ValueError:
>>>>>>> 38784bedb3032e34d3265a47b814b8d1ad0b14bb
            print("Error: Please enter a valid number.")