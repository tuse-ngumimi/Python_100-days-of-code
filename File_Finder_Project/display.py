<<<<<<< HEAD
"""
Results display and pagination functionality for File Finder application.
Handles displaying search results in paginated format.
"""

import math
from typing import List, Dict, Any
from menus import display_pagination_menu, get_pagination_choice


def display_paginated_results(results: List[Dict[str, Any]], config: Dict[str, Any]) -> None:
    """
    Display search results with pagination support.
    
    Args:
        results: List of file/folder information dictionaries
        config: Configuration dictionary containing display settings
    """
    display_size = config['display_size']
    total_results = len(results)
    total_pages = math.ceil(total_results / display_size)
    current_page = 1
    
    while True:
        # Display current page of results
        display_results_page(results, current_page, display_size, total_results)
        
        # Check if pagination is needed
        if total_pages <= 1:
            input("\nPress Enter to return to main menu...")
            break
        
        # Display pagination menu
        has_prev = current_page > 1
        has_next = current_page < total_pages
        
        display_pagination_menu(current_page, total_pages, has_prev, has_next)
        
        # Get user's pagination choice
        action = get_pagination_choice(has_prev, has_next)
        
        if action == 'prev':
            current_page -= 1
        elif action == 'next':
            current_page += 1
        elif action == 'menu':
            break


def display_results_page(results: List[Dict[str, Any]], page_num: int, page_size: int, total_results: int) -> None:
    """
    Display a single page of search results.
    
    Args:
        results: List of file/folder information dictionaries
        page_num: Current page number (1-based)
        page_size: Number of results per page
        total_results: Total number of results
    """
    start_idx = (page_num - 1) * page_size
    end_idx = min(start_idx + page_size, total_results)
    
    print(f"\n{'=' * 60}")
    print(f"    Search Results ({start_idx + 1}-{end_idx} of {total_results})")
    print(f"{'=' * 60}")
    
    for i in range(start_idx, end_idx):
        result = results[i]
        display_single_result(result, i + 1)
    
    print("=" * 60)


def display_single_result(result: Dict[str, Any], result_number: int) -> None:
    """
    Display information for a single search result.
    
    Args:
        result: Dictionary containing file/folder information
        result_number: The sequential number of this result
    """
    item_type = "Directory" if result['is_directory'] else "File"
    path = result['path']
    created = result['created']
    modified = result['modified']
    
    print(f"\n{result_number}. [{item_type}] {path}")
    print(f"    Created:  {created}")
=======
"""
Results display and pagination functionality for File Finder application.
Handles displaying search results in paginated format.
"""

import math
from typing import List, Dict, Any
from menus import display_pagination_menu, get_pagination_choice


def display_paginated_results(results: List[Dict[str, Any]], config: Dict[str, Any]) -> None:
    """
    Display search results with pagination support.
    
    Args:
        results: List of file/folder information dictionaries
        config: Configuration dictionary containing display settings
    """
    display_size = config['display_size']
    total_results = len(results)
    total_pages = math.ceil(total_results / display_size)
    current_page = 1
    
    while True:
        # Display current page of results
        display_results_page(results, current_page, display_size, total_results)
        
        # Check if pagination is needed
        if total_pages <= 1:
            input("\nPress Enter to return to main menu...")
            break
        
        # Display pagination menu
        has_prev = current_page > 1
        has_next = current_page < total_pages
        
        display_pagination_menu(current_page, total_pages, has_prev, has_next)
        
        # Get user's pagination choice
        action = get_pagination_choice(has_prev, has_next)
        
        if action == 'prev':
            current_page -= 1
        elif action == 'next':
            current_page += 1
        elif action == 'menu':
            break


def display_results_page(results: List[Dict[str, Any]], page_num: int, page_size: int, total_results: int) -> None:
    """
    Display a single page of search results.
    
    Args:
        results: List of file/folder information dictionaries
        page_num: Current page number (1-based)
        page_size: Number of results per page
        total_results: Total number of results
    """
    start_idx = (page_num - 1) * page_size
    end_idx = min(start_idx + page_size, total_results)
    
    print(f"\n{'=' * 60}")
    print(f"    Search Results ({start_idx + 1}-{end_idx} of {total_results})")
    print(f"{'=' * 60}")
    
    for i in range(start_idx, end_idx):
        result = results[i]
        display_single_result(result, i + 1)
    
    print("=" * 60)


def display_single_result(result: Dict[str, Any], result_number: int) -> None:
    """
    Display information for a single search result.
    
    Args:
        result: Dictionary containing file/folder information
        result_number: The sequential number of this result
    """
    item_type = "Directory" if result['is_directory'] else "File"
    path = result['path']
    created = result['created']
    modified = result['modified']
    
    print(f"\n{result_number}. [{item_type}] {path}")
    print(f"    Created:  {created}")
>>>>>>> 38784bedb3032e34d3265a47b814b8d1ad0b14bb
    print(f"    Modified: {modified}")