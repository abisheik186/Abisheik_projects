import re
def email_validation(a):
  try:
    if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', a):
        if len(a)>10 and len(a)<35:            
          return True
        else:
            raise Exception("Email length should be between ten")
    else:
      raise Exception("Email is not valid.Please enter valid Email")
  except Exception as e:
    print(e)
def phone_number_validation(a):
    try:
        if re.match(r"\b[0-9]{10}$",a):                
            if re.match(r"\b^[6-9]{1}",a):       #validation for employee phone number
                return True
            else:
                raise Exception("mobile number should starts with either 9 or 8 or 7 or 6")
        else:
            raise Exception("mobile number should be 10 digit long")
           # raise Exception("mobile number should starts with either 9 or 8 or 7 or 6")
    except Exception as e:
            print(e)
def name_validation(a):
    try:
        if len(a)>2 and len(a)<25:
            if re.search(r"^[a-zA-Z\s.]*$",a):
                return True
            else:
                raise Exception("name should be in alphabet letters and below 25 characters ")
        else:
            raise Exception("name should be above three characters and below 25 characters")
    except Exception as e:
        print(e)
def item_choice_validation(a):
    try:
        if re.search(r'\b[0-9q]+',a):
            return True
        else:
            raise Exception("Item number should be in numbers or q to quit")
    except Exception as e:
        print(e)
def valid_quantity(a):
  try:
    if a>0:
      return True
    else:
      raise Exception("please enter value above zero")
  except ValueError:
    print('please enter numerical values')
  except TypeError:
    print('please Enter valid numerical values')
  except Exception as e:
    print(e)
def decision(a):
  try:
    if re.search(r"\b[ynYN]",a):
      return True
    else:
      raise Exception("please enter only 'y' and 'n'")
  except Exception as e:
    print(e)
def isbn(a):
    if re.fullmatch(r'\b^ISBN-[0-9]{3}-[0-9]{1,5}-[0-9]{1,7}-[0-9]{1}$\b',a):
        return True
    else:
        print('please enter valid ISBN number with correct pattern')

