from random import randint
import re
class Employee:
    def __init__(self):
        emp_names=[]
        self.emp_names=emp_names
        emp_age=[]
        self.emp_age=emp_age
        emp_phone_number=[]
        self.emp_phone_number=emp_phone_number
        emp_salary=[]
        self.emp_salary=emp_salary
        emp_id=[]
        self.emp_id=emp_id
        emp_details=()
        self.emp_details=emp_details
        emp_info=[]
        self.emp_info=emp_info

    def Add_Employee(self):         #function for add employee
        while True:
            try:
                self.emp_name=input("Enter employee name :").lower()     #getting employee name from user
                if len(self.emp_name)!=0:                        #validation for employee name
                    if self.emp_name.isalpha():
                        if len(self.emp_name)>2:
                            self.emp_names.append(self.emp_name)
                            break
                        else:
                            raise Exception("name should be atleast three characters long")
                    else:
                        raise ValueError("name should be in alphabet characters")
                else:
                    raise ValueError("name should not be empty")
            except ValueError as e:
                print(e)
            except Exception as e1:
                print(e1)
        while True:
            try:
                age=input("Enter employee age :")       #getting employee age from user
                if len(age)!=0:                     #validation for employee age
                    if age.isnumeric():
                        age=int(age)
                        if age>18:
                            if age<65:
                                self.emp_age.append(age)
                                break
                            else:
                                raise Exception("age should be below 65")
                        else:
                            raise Exception("age should be above 18")
                    else:
                        raise TypeError("please enter valid age")                
                else:
                    raise ValueError("age should not be empty")
            except ValueError as e:
                print(e)
            except Exception as e1:
                print(e1)
        while True:
            try:
                phone_number=input("Enter Employee Phone Number :")     #getting employee phone number from user
                if re.match(r"\b^[6-9]{1}",phone_number):       #validation for employee phone number
                    if re.match(r"\b[0-9]{10}$",phone_number):
                        if phone_number not in self.emp_phone_number:
                            self.emp_phone_number.append(phone_number)
                            break
                        else:
                            raise Exception("phone number is already existed please enter another phone number")
                    else:
                        raise Exception("mobile number should 10 digit long")
                else:
                    raise Exception("mobile number should starts with either 9 or 8 or 7 or 6")
            except Exception as e:
                    print(e)
        while True:
            try:
                salary=input("Enter employee salary :")     #getting employee salary from user
                if len(salary)!=0:                  #validation for employee salary
                    if float(salary)>=0:
                            self.emp_salary.append(salary)
                            break
                    else:
                        raise Exception("employee salary should not be negative value")
                else:
                    raise Exception("salary should not be empty")
            except ValueError:
                print("please enter valid salary")
            except Exception as e:
                    print(e)
        
        empId=randint(1001,1010)        #getting employee ID by random
        self.emp_id.append(empId)        #storing  employee id
        empDetails=()
        emp_details=(self.emp_name,age,phone_number,salary,empId)    #storing all details into one tuple
        emp_info=[]
        emp_info.append(emp_details)    #storing all employee details into a list
        print("\nEmployee added successfully!\n ")
        
    def Update_Employee(self,employee_update):           #function for update the details of given employee
        while True:
            try:
                update_employee=input("Enter employee name to update :").lower()    #getting name of the employee to update
                if len(update_employee)!=0:         #validation for search name
                    if update_employee.isalpha():
                        if len(update_employee)>2:                       
                           break
                        else:
                            raise Exception("name should be atleast two characters long")
                    else:
                        raise ValueError("name should be in alphabet characters")
                else:
                    raise ValueError("name should not be empty")
            except ValueError as e:
                print(e)
            except Exception as e1:
                print(e1)
        if update_employee in self.emp_names:        #checking whether the given name is found in list or not 
            while True:
                try:
                    empage=input("Enter employee age to update :")  #getting employee age to update
                    if len(empage)!=0:      #validation for age
                        if empage.isnumeric():
                            empage=int(empage)
                            if empage>18:
                                if empage<100:                                
                                    break
                                else:
                                    raise Exception("age should be below 100")
                            else:
                                raise Exception("age should be above 18")
                        else:
                            raise TypeError("age should be in numbers")                
                    else:
                        raise ValueError("age should not be empty")
                except ValueError as e:
                    print(e)
                except Exception as e1:
                    print(e1)
            while True:
                try:
                    empphone_number=input("Enter Employee Phone Number to update :")   #getting employee phone number to update
                    if re.match(r"\b^[6-9]{1}",empphone_number):        #validation for phone number
                        if re.match(r"\b[0-9]{10}$",empphone_number):
                           break
                        else:
                            raise Exception("mobile number should 10 digit long")
                    else:
                        raise Exception("mobile number should starts with either 9 or 8 or 7 or 6")
                except Exception as e:
                        print(e)
            while True:
                try:
                    empsalary=input("Enter employee salary to update:") #getting employee salary to update
                    if len(empsalary)!=0:   #validation for employee salary
                        if int(empsalary)!=0:
                            if empsalary.isdigit():
                                break
                            else:
                                raise Exception("salary should be in numbers")
                        else:
                            raise ValueError("employee salary should not be empty")
                    else:
                        raise Exception("salary should not be empty")
                        print(ValueError)
                except Exception as e:
                        print(e)
        else:
            print("please enter existing employee name")
        for i in range(len(self.emp_names)):
            if self.emp_names[i]==update_employee:
                self.emp_age[i]=empage
                self.emp_phone_number[i]=empphone_number
                self.emp_salary[i]=empsalary
                print("Employee updated successfully!")
                break
            
    def Display_Employee_Information(self,employee_details):     #function for display the employee details
        search_name=input("Enter employee name to display :")   #getting employee name to display
        for i in range(len(self.emp_names)):     #printing the details according to the given name
            if self.emp_names[i]==search_name:
                print("\nEmployee ID :",self.emp_id[i])
                print("\nEmployee Name :",''.join(self.emp_names[i]))
                print("\nEmployee Age :",self.emp_age[i])
                print("\nEmployee Phone Number :",''.join(self.emp_phone_number[i]))
                print("\nEmployee Salary :",''.join(self.emp_salary[i]))
        else:
            print("Please enter existing employee name")
    def main(self):
        while True:
            print("1.Add Employee\n2.Update Employee Details\n3.Display Employee Details\n4.Quit")
            choice=input("Enter your choice :")         #getting choice value from user      
            if choice=="1":
                self.Add_Employee()
            elif choice=="2":
                if self.emp_names!=[]:
                    self.Update_Employee(self.emp_names)
                else:
                    print('please add employee before update')
            elif choice=="3":
                if self.emp_names!=[]:
                    self.Display_Employee_Information(self.emp_info)
                else:
                    print('please add employee before display')
            elif choice=="4":
                print("Exiting the program.......")
                break
            else:
                print("please enter numbers between 1 and 4")

obj=Employee()
#print(obj.emp_names)
obj.main()
