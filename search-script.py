import os # For interacting with the operating system
import sys # For accessing command-line arguments
import fnmatch # For pattern matching
import argparse # For parsing command-line arguments

def search_files(directory, pattern):
    """Search for files matching the given pattern in the specified directory and its subdirectories."""
    matches = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                matches.append(os.path.join(root, filename))
    return matches