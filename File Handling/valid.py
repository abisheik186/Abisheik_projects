import re
import logging
logging.basicConfig(filename='error_file.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')
def log(a):
  logging.debug(str(a))
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
def password_validation(a):
  try:
    if re.match(r"^(?![&!#])[\W]{1}+[a-zA-Z0-9\W]{3,9}$",a):        
      return True
    else:
      raise Exception("pasword should contain minimum three characters and maximum nine characters with combination of letters and numbers and special characters")
  except Exception as e:
    log(e)
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
      log(e)
      print(e)
def name_validation(a):
    try:
        if len(a)>2 and len(a)<25:
            if re.search(r"\b[a-zA-Z\s.]+\b",a):
                return True
            else:
                raise Exception("name should be in alphabet letters and between ")
        else:
            raise Exception("name should be above three characters and below 25 characters")
    except Exception as e:
      log(e)
      print(e)
def age_validation(a):
  try:
    if len(a)!=0:                     #validation for employee age
        if a.isnumeric():
            a=int(a)
            if a>16:
                if a<65:
                  return True
                else:
                    raise Exception("age should be below 65")
            else:
                raise Exception("age should be above 18")
        else:
            raise TypeError("please enter valid age")                
    else:
        raise ValueError("age should not be empty")
  except ValueError as e:
    log(e)
    print(e)
  except Exception as e1:
    log(e1)
    print(e1)
def gender_validation(a):
  try:
    if a=='male' or a=='female' or a=='other':
      return True
    else:
      raise Exception('gender should be either male, female or other only')
  except Exception as e:
    log(e)
    print(e)
def course_validation(a):
  course=['java','python','salesforce','dotnet']
  try:
    if len(a)>0:
      if a in course:
        return True
      else:
        raise Exception('Entered course is not available right now.')
    else:
      raise Exception('Course name should not be empty.')
  except Exception as e:
    log(e)
    print(e)
