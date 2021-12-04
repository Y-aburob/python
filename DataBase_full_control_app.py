import sqlite3, os
from typing import Iterable

# change dir of the file and set it into the same dir of the db folder, to make sure that no errors will be shown
os.chdir(r"C:\Users\gonce\.vscode\programming saves VS")


# connecting the file with the database
db = sqlite3.connect("skill_app.db")

# creating table: skills with columns: user_id | name | progress
db.execute("create table if not exists skills(user_id integer, name text, progress integer)")

# setting the cursor to start working on the database
cr = db.cursor()



# --------functions--------

# add function
def add(*info) -> Iterable: 

    """
    add an iterable (user_id, name, progress) then the function will unpack it 
    then put it in a tuple then add it into the database
    """

    cr.execute("insert into skills(user_id, name, progress) values(?, ?, ?)", info)

    db.commit()
    db.close()
    print("the info has been added successfully")
    

# delete by user_id function
def delete_by_id(value) -> int:

    """
    it will delete a skill by a user_id
    """
    cr.execute(f"delete from skills where user_id = {value}")
    db.commit()
    db.close()
    print(f"the skill with a user_id:{value} has been removed successfully")

# delete by name function
def delete_by_name(value) -> str:

    """
    it will delete a skill by it's name
    """
    cr.execute(f"delete from skills where name = '{value}'")
    
    print(f"the skill{value} has been removed successfully")
    db.commit()
    db.close()


# show all of the skills and thier progress and the user_ids for them
def show_all():

    cr.execute("select * from skills")

    list = cr.fetchall()

    for id,name,prog in list:

        print(f"id: {id}\t name: {name}\t progress: {prog}% \n")


# show one of the skills and it's progress and the user_id by it's name
def show_one_by_name(value) -> str:

    """
    show a skill by it's name
    """
    cr.execute(f"select * from skills where name = '{value}' ")

    list1 = cr.fetchone()

    print(f"user_id: {list1[0]}\t name: {list1[1]}\t progress: {list1[2]}")


# show one of the skills and it's progress and the user_id by the user_id
def show_one_by_id(value) -> int:

    """
    show a skill by it's name
    """
    cr.execute(f"select * from skills where user_id = {value}")

    list = cr.fetchone()

    print(f"user_id: {list[0]}\t name: {list[1]}\t progress: {list[2]}")


# show as many skills as you wish
def show_many(value) -> int:

    """
    show as many skills as you wish, all what you have to do is to select number of skills that you want show.
    """
    cr.execute("select * from skills")
    list = cr.fetchmany(value)

    for id,name,prog in list:

        print(f"user_id: {id}\t name: {name}\t progress: {prog}")


# rename a skill
def update_name(name, user_id):

    """
    it will update a skill name
    """
    cr.execute(f"select name from skills where user_id = {user_id}")

    old_skill = cr.fetchone()
    print(f"we will replace the old skill {old_skill[0]} with the new one {name} ....")
    cr.execute(f"update skills set name = '{name}' where user_id = {user_id}")
    print("")
    db.commit()
    db.close()
    print("Name replaced successfully")

# replace the user_id for a skill
def update_user_id(user_id, name):

    """
    it will update the user_id of a skill by it's name
    """
    
    cr.execute(f"select name,user_id from skills where name = '{name}'")
    infor = cr.fetchone()
    print(f"we will replace the old user_id: {infor[1]} of the skill: '{infor[0]}' with a new user_id: {user_id} ....")
    cr.execute(f"update skills set user_id = {user_id} where name = '{name}'")
    print("")
    db.commit()
    db.close()
    print("user_id replaced successfully")

def update_progress(progress, name):

    """
    it will update a progress of a skill by it's name
    """

    cr.execute("select name,progress from skills")

    old_infos = cr.fetchone()

    print(f"we will replace the old progress: {old_infos[1]} of the skill: {old_infos[0]} with the new progress: {progress} ....")

    cr.execute(f"update skills set progress = {progress} where name = '{name}'")
    print("")
    db.commit()
    db.close()
    print("progress replaced successfully")


Q = """ 
what do you want to do?

insert into database => i
delete a skill from the database => d
show skills => s
update skill info => u

Enter your answer: 
"""

answer = input(Q).strip().capitalize()


# check if the answer is one of the Q commands or not
if answer == 'I' or answer == 'A':

    # if answer == I => the add function will work
    cr.execute("select user_id from skills")
    user_id_list = cr.fetchall()

    number = 0
    for i in user_id_list:
        for x in user_id_list:

            if i[0] > x[0]:

                number = i[0]

    user_id = int(input(f"Enter the user_id, Note: the user_id counter is {number} now: "))
    name = input("Enter the skill name: ")
    progress = int(input("Enter the progress: "))

    my_info = (user_id, name, progress)

    add(*my_info)


# if answer == D => the delete function will work
elif answer =='D':

    q1 = input("do you want to delete the skill using the user_id or it's name Enter:: u/n: ").strip().capitalize()

    if q1 == 'U':

        user_id = int(input("Enter the user_id: "))

        delete_by_id(user_id)

    elif q1 == 'N':

        name = input("Enter the skill name: ")

        delete_by_name(name)

    else:

        print(f"no such a command called {q1}")


# if answer == S => one of the show functions will work
elif answer == 'S':

    ques = input("do you want to show them all or one or as many as you want? all =>a | one => o | as many as you want => m: ").strip().capitalize()


    # if ques = A => show all of the skills function will work
    if ques == 'A':

        show_all()

    # if ques = O => show one_skill function will work
    elif ques == 'O':

        ques1 = input("do you want to show the skill by it's name or user_id? n/u: ").strip().capitalize()

        # show the one skill by it's name
        if ques1 == 'N':

            quesname = input("Enter the name of the skill: ").strip().lower()
            show_one_by_name(quesname)


        # show the one skill by it's user_id
        elif ques1 == 'U':
            quesid = int(input("Enter the user_id of the skill that you want: "))
            show_one_by_id(quesid)
        
        else:
            print(f"sorry, no such a command called {ques1}")

    # if ques = M => show as many skills as you wish function will work you only need to select the number of skills
    elif ques == 'M':

        numbers = int(input("Enter the number of skills that you want to show// note: the skills will be shown from the first skill to the last: "))

        show_many(numbers)
    
    else:
        print(f"sorry, no such a command called {ques}")

# if answer == U => one of the update functions will work
elif answer == 'U':

    question = input("do you want to update a skill name(n) or the user_id(u) of a skill or the progress(p)? n / u / p: ").strip().capitalize()

    # if question == N => name of the skill will be updated
    if question == 'N':

        new_name = input("Enter the new name: ")
        user_id_num = int(input("Enter the user_id of the skill: "))

        update_name(new_name, user_id_num)

    # if question == U => the user_id of the skill will be updated
    elif question == 'U':

        new_user_id = int(input("Enter the new user_id: "))
        name_of_user = input("Enter the skill name that has the user_id that you want to change: ")

        update_user_id(new_user_id, name_of_user)

    # if question == P => the progress of the skill will be updated
    elif question == 'P':

        new_progress = int(input("Enter the new progress: "))
        name_for_prog = input("Enter the name of the skill that you want to change it's progress: ")

        update_progress(new_progress, name_for_prog)
    
    else:
        print(f"sorry, no such a command called {question}")

else:

    print(f"sorry, no such a command called {answer}")