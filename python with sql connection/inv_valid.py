import re
import logging
logging.basicConfig(filename='sql_error_file.txt',level=logging.DEBUG,format='%(asctime)s - %(message)s')
def log(a):
    logging.debug(str(a))
def prod_valid(a):
    try:
       if len(a)>=2:
            if re.match(r"^[a-zA-Z]+$",a):
                return True
            else:                    
                raise Exception("Name should contain only alphabets")
       else:                
            raise Exception("Name should not empty or below two characters")
    except Exception as e:
        log(e)
        print(e)

def prod_price_valid(a):
  try:
    if re.search(r"^[1-9]+|[0-9].[0-9]{1,2}|.[0-9]{1,2}",a):
       if float(a)>0:
          return True
       else:
            raise Exception("cost price should not be negative values")
    else:
         raise Exception("cost should contain only price values and should not be empty")
  except Exception as e:
      log(e)
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
def id_valid(a):
    try:
        if re.match(r'\b[0-9]\b',a):
            return True
        else:
            raise Exception('id should be in numbers')
    except Exception as e:
        log(e)
        print(e)
