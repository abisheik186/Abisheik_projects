import valid
from check_existing import check_existing_phone_number
import datetime
import os
class student_info():
    def __init__(self):
        self.stud_dict=[]
    def menu(self):
        while True:
            print('\n1.Add information\n2.View information\n3.Update information\n4.Log out')
            ch=input('Enter your choice :')
            if ch=='1':
                self.add_info()
            elif ch=='2':
                self.view_info()
            elif ch=='3':
                self.update_info()
            elif ch=='4':
                with open('log.txt','a') as f:
                    f.write('\nlogged out at {}'.format(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')))
                print('Logged out Successfully')
                break
            else:
                print('Please enter within available options')
    def add_info(self):
        while True:
            try:
                stu_name=input('Enter student name :').lower()
                if valid.name_validation(stu_name):
                    stu_file=open(stu_name+'.txt','x')      #creating file exclusive to avoid duplicate name
                    break
            except FileExistsError as e:
                print('Student name is already exist.')
                valid.log(e)    #storing error in error file
                
        while True:
            stu_age=input('Enter student age :')
            if valid.age_validation(stu_age):
                break
        while True:
            stu_gender=input('Enter student gender :').lower()
            if valid.gender_validation(stu_gender):
                break
        while True:
            stu_course=input('Enter student studying course :').lower()
            if valid.course_validation(stu_course):
                break
        while True:
            stu_phone_number=input('Enter student phone number :')
            if valid.phone_number_validation(stu_phone_number):
                if check_existing_phone_number(stu_phone_number):   #checking whether the given number is already existing or not in all the files on current working directory
                    break
        with open(stu_name+'.txt','w') as write_file:   #opening text file in write mode
            write_file.writelines([stu_name+'\n',stu_age+'\n',stu_gender+'\n',stu_course+'\n',stu_phone_number+'\n'])   #storing all the values in the text file in list format
        print(f'Information of {stu_name} added successfully')
    def view_info(self):
        while True:
            try:
                v_name=input('Enter student name to view :').lower()
                if valid.name_validation(v_name):
                    if os.path.exists(v_name+'.txt'):   #checking whether the file is exists or not using path.exists of os module
                        break
                    else:
                        raise Exception('Entered student name is not existed.')
            except Exception as e:
                valid.log(e)    #storing error in error file
                print(e)
        with open(v_name+'.txt','r') as view_file:
            listInfo=[i.strip() for i in view_file.readlines()] #converting file contents into list
        print(f'Student name :{listInfo[0]}\nStudent Age :{listInfo[1]}\nStudent Gender :{listInfo[2]}\nStudent Course :{listInfo[3]}\nStudent COntact number :{listInfo[4]}')
    def update_info(self):
        while True:
            try:
                u_name=input('Enter student name to update :').lower()
                if valid.name_validation(u_name):
                    if os.path.exists(u_name+'.txt'):   #checking whether the student name is existing or not
                        break
                    else:
                        raise Exception('Entered student name is not existed.')
            except Exception as e:
                valid.log(e)
                print(e)
        with open(u_name+'.txt','r') as upd_file:
            listInfo=[i.strip() for i in upd_file.readlines()]  #converting file contents into list
        print('1.Age\n2.Gender\n3.Course\n4.Contact Number')
        ch=input('Which one do you want update (1/2/3/4) :')
        if ch=='1':
            while True:
                u_age=input('Enter student age to update :')
                if valid.age_validation(u_age):
                    break
            upDAta='age'
            listInfo[1]=(u_age)
        elif ch=='2':
            while True:
                u_gender=input('Enter student gender to update :').lower()
                if valid.gender_validation(u_gender):
                    break
            upDAta='Gender'
            listInfo[2]=(u_gender)
        elif ch=='3':
            while True:
                u_course=input('Enter student course to update :').lower()
                if valid.course_validation(u_course):
                    break
            listInfo[3]=(u_course)
            upDAta='Course'
        elif ch=='4':
            while True:
                u_ph_number=input('Enter student phone number to update :')
                if valid.phone_number_validation(u_ph_number):
                    if check_existing_phone_number(u_ph_number):
                        break
            listInfo[4]=(u_ph_number)
            upDAta='contact number'
        else:
            print('Please enter within available options')
            
        for i in range(0,len(listInfo)):
            listInfo[i]+="\n"
        with open(u_name+'.txt','w') as upd_file:
            upd_file.writelines(listInfo)   #storing updated list into text file
        print(f'{upDAta} updated successfully')
class Login(student_info):
    def register(self):
        file=open('loginfile.txt','a+') #opning file in append access mode 
        while True:
            r_name=input('Enter user name :').lower()
            if valid.name_validation(r_name):
                break
        file.seek(0)    #seeking the pointer to the beginning of the file
        reg=file.readlines()    #converting the file contents into list
        if reg:         #checking whether the file have contents in it
            for i in reg:   
                existed_name,a=i.strip().split('!') #splitting the list at the ! symbol and storing into two seperate variables
            if r_name!=existed_name:
                file.write(r_name+'!')  #writing the user name into file
            else:
                print('entered user name is already given.please give alernate name.')
        else:
            file.write(r_name+'!')
        while True:
            r_password=input('Enter user password :')
            if valid.password_validation(r_password):
                break
        file.write(r_password+"\n") #writing the password into file
        print('you registered successfully')
        file.close()    #closing the file
    def login(self):
        file=open('loginfile.txt','r')
        file.seek(0)
        reg=file.readlines()
        f=1
        if reg:
            while f:
                l_name=input('Enter registered username :')
                if valid.name_validation(l_name):
                    for i in reg:
                        existed_name,existed_password=i.strip().split('!')
                        if l_name == existed_name:
                            f=0
                        else:
                            f=2
                if f==2:
                    print('Entered user name is not registered.please register before login.')
            f=1
            while f:
                l_password=input('Enter user password :')
                if valid.password_validation(l_password):
                    for i in reg:
                        existed_name,existed_password=i.strip().split('!')
                        if l_name==existed_name and l_password==existed_password:   #checking if both the regisered username and password are matching
                            f=2
                            
                        else:
                            f=3
                if f==2:
                    print('Welcome user..\nYou logged in successfully')
                    with open('log.txt','a') as f:
                        f.write('\n{} logged in at {}'.format(l_name,datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')))
                    self.menu()
                    f=0
                if f==3:
                    print('username and password is mismatching. please enter valid password')
        else:
            print('nobody has registered yet. please register first.')
        
        file.close()

s1=Login()
while True:
    print('1.Register\n2.Login\n3.Exit')
    ch=input('Enter the choice :')
    if ch=='1':
        s1.register()
    elif ch=='2':
        s1.login()
    elif ch=='3':
        print('Exiting the prgram...')        
        break
    else:
        print('please enter valid choice')
            

