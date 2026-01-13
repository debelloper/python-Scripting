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

def main():
    parser = argparse.ArgumentParser(description="Search for files matching a pattern in a directory.")
    parser.add_argument("directory", help="The directory to search in")
    parser.add_argument("pattern", help="The filename pattern to search for (e.g., '*.txt')")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"The directory {args.directory} does not exist.")
        sys.exit(1)
    
    matched_files = search_files(args.directory, args.pattern)
    
    if matched_files:
        print("Matched files:")
        for file in matched_files:
            print(file)
    else:
        print("No files matched the given pattern.")

if __name__ == "__main__":
    main()