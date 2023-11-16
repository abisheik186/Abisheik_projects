import os
dir_path = os.getcwd()  #getting path of currently working directorydef check_existing_phone_number(a):
def check_existing_phone_number(a):
    f=0
    for file in os.listdir(dir_path):   #iterating all the files in currently working directory
        if file.endswith('.txt'):
            cur_path = os.path.join(dir_path, file)
            if os.path.isfile(cur_path):    #check if it is a file
                with open(cur_path, 'r') as file:
                    #print(file.read())
                    if a in file.read():
                        print('yes')
                        print('mobile number is already given')
                        break
                    else:
                        return True
                   
