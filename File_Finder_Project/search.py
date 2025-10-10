<<<<<<< HEAD
"""
File and folder search functionality for File Finder application.
Handles recursive directory traversal and file matching.
"""

import os
import time
from typing import Dict, List, Any
from pathlib import Path
from datetime import datetime


def search_files_and_folders(query: str, config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Search for files and folders matching the query string.
    
    Args:
        query: The search term to match against filenames
        config: Configuration dictionary containing search settings
        
    Returns:
        List[Dict[str, Any]]: List of dictionaries containing file/folder information
    """
    start_time = time.time()
    results = []
    
    root_path = config['root_path']
    case_sensitive = config['case_sensitive']
    
    # Prepare query for case-insensitive search if needed
    search_query = query if case_sensitive else query.lower()
    
    try:
        # Walk through all directories and subdirectories
        for dirpath, dirnames, filenames in os.walk(root_path):
            # Check directories
            for dirname in dirnames:
                if matches_query(dirname, search_query, case_sensitive):
                    dir_path = os.path.join(dirpath, dirname)
                    result = create_file_info_dict(dir_path, is_directory=True)
                    if result is not None:
                        results.append(result)
            
            # Check files
            for filename in filenames:
                if matches_query(filename, search_query, case_sensitive):
                    file_path = os.path.join(dirpath, filename)
                    result = create_file_info_dict(file_path, is_directory=False)
                    if result is not None:
                        results.append(result)
    
    except PermissionError as e:
        print(f"Warning: Permission denied accessing some directories: {e}")
    except Exception as e:
        print(f"Error during search: {e}")
    
    end_time = time.time()
    search_duration = end_time - start_time
    
    # Display search statistics
    print(f"\nSearch completed!")
    print(f"Found {len(results)} matching items in {search_duration:.2f} seconds.")
    
    return results


def matches_query(filename: str, query: str, case_sensitive: bool) -> bool:
    """
    Check if a filename matches the search query.
    
    Args:
        filename: The filename to check
        query: The search query
        case_sensitive: Whether the search should be case-sensitive
        
    Returns:
        bool: True if filename matches query, False otherwise
    """
    if case_sensitive:
        return query in filename
    else:
        return query in filename.lower()


def create_file_info_dict(file_path: str, is_directory: bool) -> Dict[str, Any] | None:
    """
    Create a dictionary containing file or directory information.
    
    Args:
        file_path: The path to the file or directory
        is_directory: Whether the path is a directory
        
    Returns:
        Dict[str, Any] | None: Dictionary with file info, or None if error occurred
    """
    try:
        path_obj = Path(file_path)
        stat_info = path_obj.stat()
        
        # Convert timestamps to readable dates
        created_time = datetime.fromtimestamp(stat_info.st_ctime)
        modified_time = datetime.fromtimestamp(stat_info.st_mtime)
        
        return {
            'path': str(path_obj.absolute()),
            'is_directory': is_directory,
            'created': created_time.strftime("%Y-%m-%d %H:%M:%S"),
            'modified': modified_time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    except (OSError, PermissionError) as e:
        print(f"Warning: Could not access file info for {file_path}: {e}")
=======
"""
File and folder search functionality for File Finder application.
Handles recursive directory traversal and file matching.
"""

import os
import time
from typing import Dict, List, Any
from pathlib import Path
from datetime import datetime


def search_files_and_folders(query: str, config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Search for files and folders matching the query string.
    
    Args:
        query: The search term to match against filenames
        config: Configuration dictionary containing search settings
        
    Returns:
        List[Dict[str, Any]]: List of dictionaries containing file/folder information
    """
    start_time = time.time()
    results = []
    
    root_path = config['root_path']
    case_sensitive = config['case_sensitive']
    
    # Prepare query for case-insensitive search if needed
    search_query = query if case_sensitive else query.lower()
    
    try:
        # Walk through all directories and subdirectories
        for dirpath, dirnames, filenames in os.walk(root_path):
            # Check directories
            for dirname in dirnames:
                if matches_query(dirname, search_query, case_sensitive):
                    dir_path = os.path.join(dirpath, dirname)
                    result = create_file_info_dict(dir_path, is_directory=True)
                    if result is not None:
                        results.append(result)
            
            # Check files
            for filename in filenames:
                if matches_query(filename, search_query, case_sensitive):
                    file_path = os.path.join(dirpath, filename)
                    result = create_file_info_dict(file_path, is_directory=False)
                    if result is not None:
                        results.append(result)
    
    except PermissionError as e:
        print(f"Warning: Permission denied accessing some directories: {e}")
    except Exception as e:
        print(f"Error during search: {e}")
    
    end_time = time.time()
    search_duration = end_time - start_time
    
    # Display search statistics
    print(f"\nSearch completed!")
    print(f"Found {len(results)} matching items in {search_duration:.2f} seconds.")
    
    return results


def matches_query(filename: str, query: str, case_sensitive: bool) -> bool:
    """
    Check if a filename matches the search query.
    
    Args:
        filename: The filename to check
        query: The search query
        case_sensitive: Whether the search should be case-sensitive
        
    Returns:
        bool: True if filename matches query, False otherwise
    """
    if case_sensitive:
        return query in filename
    else:
        return query in filename.lower()


def create_file_info_dict(file_path: str, is_directory: bool) -> Dict[str, Any] | None:
    """
    Create a dictionary containing file or directory information.
    
    Args:
        file_path: The path to the file or directory
        is_directory: Whether the path is a directory
        
    Returns:
        Dict[str, Any] | None: Dictionary with file info, or None if error occurred
    """
    try:
        path_obj = Path(file_path)
        stat_info = path_obj.stat()
        
        # Convert timestamps to readable dates
        created_time = datetime.fromtimestamp(stat_info.st_ctime)
        modified_time = datetime.fromtimestamp(stat_info.st_mtime)
        
        return {
            'path': str(path_obj.absolute()),
            'is_directory': is_directory,
            'created': created_time.strftime("%Y-%m-%d %H:%M:%S"),
            'modified': modified_time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    except (OSError, PermissionError) as e:
        print(f"Warning: Could not access file info for {file_path}: {e}")
>>>>>>> 38784bedb3032e34d3265a47b814b8d1ad0b14bb
        return None