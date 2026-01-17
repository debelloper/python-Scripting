import re # importing regular expression module

# Function to check the strength of a password
def check_password(password):
  if len(password) < 8:
    return False
  elif re.search('[0-9]',password) is None:
    return False
  elif re.search('[a-z]',password) is None:
    return False
  elif re.search('[A-Z]',password) is None:
    return False
  elif re.search('[@#$^&]',password) is None:
    return False
  return True

def main():
  password = input("Enter a password to check its strength: ")
  if check_password(password):
    print("The password is strong.")
  else:
    print("The password is weak. It should be at least 8 characters long and include uppercase letters, lowercase letters, numbers, and special characters (@, #, $, ^, &).")   


if __name__ == "__main__": # Entry point of the script
    main()