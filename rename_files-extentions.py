# Now i'm going to show you a program that renames the files and thier extensions, it will ask you for the cwdir url at the first
# then it will ask you if you want to rename them one by one or rename them all togather(the same name with a counter)




import os
import re

work_dir = input("Enter the work dir url: ")    # files place

os.chdir(f"{work_dir}")

my_list = os.listdir()  # add the files from the directory to a list

def change_name(old_name, new_name, file_type):

    os.rename(f"{old_name}", f"{new_name}.{file_type}")

def default( name,answer):

    os.rename(f"{name}", f"{answer}.py")




wanna_do = input("do you want to rename each file alone or give them the same name with a counter? a(each one alone) s(same name) //Enter a or s: ")

if wanna_do == 'A' or wanna_do == 'a':

    z = 0
    for i in my_list:

        new_name = input(f"Enter the new name for the file '{i}': ")
        new_extension = input(f"Enter the new extention for the file '{new_name}' // press n if you don't want to change it: ")

        if new_extension == 'n' or new_extension == 'N':

            new_one = re.findall("\.\w+", f"{i}")
            new_extension = new_one[0]


        change_name(i, new_name, new_extension)
        z += 1


elif wanna_do == 'S' or wanna_do == 's':

    b = input("what do you want to name the files? enter here: ")

    x = 0
    for i in my_list:


        default(i, f"{b}{x}")

        x += 1


print("--------all files have been renamed successfully--------")
