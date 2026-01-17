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

# Test the function with example passwords
for password in ["12345678", "Abcd@1234"]:
  if(check_password(password)):
    print(password, " is a strong password.")
  else:
    print(password, "is a weak password.")

    