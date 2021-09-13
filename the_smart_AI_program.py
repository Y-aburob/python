

# Hello, my name is yanal today im going to show you my robot, it's like "siri" in iphone or "google Assistant"

# How it wokrs:

# 1- start the program using the TERMINAL:    // hint: type:   python file_name.py
# 2- Enter your name
# 3- start talking with 








import pyttsx3
import speech_recognition
import sys
human = speech_recognition.Recognizer()
robot = pyttsx3.init()

voices = robot.getProperty('voices')
robot.setProperty('voice', voices[1].id)
robot.setProperty('rate', 150)


your_name = input("First you have to tell me what is your name? ")

with speech_recognition.Microphone() as source:

    print("say something....")
    user = human.listen(source)

    txt = human.recognize_google(user)
    print(txt)

    if 'hello' in txt:

        robot.say(f"hello {your_name}, my name is kota, nice to meet you")
        robot.runAndWait()
        robot.say("how are you today?")
        robot.runAndWait()
        print("say something...")
        answer = human.listen(source)
        txt1 = human.recognize_google(answer, key=None, language="en-Us")
        print(txt1)

        if "fine" in txt1:
            robot.say("Happy to hear that, hope all of your days will be good")
            robot.runAndWait()
            robot.say("do you need anything from me?")
            robot.runAndWait()
            print("say something....")
            answer1 = human.listen(source)
            txt2 = human.recognize_google(answer1, key=None, language="en-us")
            print(txt2)
            if "no" in txt2:
                robot.say("ok no problem, you can call me when ever you want and i will be here for you ")
                robot.runAndWait()
                robot.say("have a nice day, good bye")
                robot.runAndWait()
                sys.exit(0)
            
            elif "nothing" in txt2:
                robot.say("ok no problem, you can call me when ever you want and i will be here for you ")
                robot.runAndWait()
                robot.say("have a nice day, good bye")
                robot.runAndWait()
                sys.exit(0)
            
            elif "no thanks" in txt2:
                robot.say("ok no problem, you can call me when ever you want and i will be here for you ")
                robot.runAndWait()
                robot.say("have a nice day, good bye")
                robot.runAndWait()
                sys.exit(0)

            elif "yes" in txt2:
                robot.say("ok, tell me what do you want?")
                robot.runAndWait()

                print("say something....")
                answer2 = human.listen(source)
                txt3 = human.recognize_google(answer2, key=None, language="en-us")
                print(txt3)
                if txt3 != "nothing":
                    robot.say("Sorry, I can't do that now, because the software engineer Yanal hasn't taught me these yet, wait for my next update")
                    robot.runAndWait()

            elif "i need" in txt2:
                robot.say("ok, tell me what do you want?")
                robot.runAndWait()

                print("say something....")
                answer2 = human.listen(source)
                txt6 = human.recognize_google(answer2, key=None, language="en-us")
                print(txt6)
                if txt6 != "nothing":
                    robot.say("Sorry, I can't do that now, because the software engineer Yanal hasn't taught me these yet, wait for my next update")
                    robot.runAndWait()

            elif "do" in txt2:
                robot.say("ok, tell me what do you want?")
                robot.runAndWait()

                print("say something....")
                answer2 = human.listen(source)
                txt7 = human.recognize_google(answer2, key=None, language="en-us")
                print(txt7)
                if txt7 != "nothing":
                    robot.say("Sorry, I can't do that now, because the software engineer Yanal hasn't taught me these yet, wait for my next update")
                    robot.runAndWait()
            
            elif "bye" in txt2:
                robot.say("good bye friend")
                robot.runAndWait()
                sys.exit(0)

            elif "none of your business" in txt2:
                robot.say("chill i'm just asking i did nothing idiot")
                sys.exit(0)

            elif "not your business" in txt2:
                robot.say("chill i'm just asking i did nothing idiot")
                sys.exit(0)
            

        elif "bad" in txt1:
            robot.say("sorry about that, Hope you will be better soon")
            robot.runAndWait()
            robot.say("just tell me what's bothering you, do you need any help?")
            robot.runAndWait()
            print("say something....")
            answer3 = human.listen(source)
            txt4 = human.recognize_google(answer3)
            print(txt4)
            # if "no" in txt4:
            #     robot.say("ok as you wish, looks like you really need some help")
            #     robot.runAndWait()
            #     robot.say("i hope your day will be better, good bye")
            #     robot.runAndWait()
            #     sys.exit(0)
            
            if "nothing" in txt4:
                robot.say("i don't think so, anyway, you can call me when ever you want and i will be here for you, hope your day will be better ")
                robot.runAndWait()
                robot.say("good bye")
                robot.runAndWait()
                sys.exit(0)
            
            elif "no thanks" in txt4:
                robot.say("ok no problem, you can call me when ever you want and i will be here for you ")
                robot.runAndWait()
                robot.say("i hope your day will be better, good bye")
                robot.runAndWait()
                sys.exit(0)

            elif "yes" in txt4:
                robot.say("ok, tell me what is your problem?")
                robot.runAndWait()

                print("say something....")
                answer2 = human.listen(source)
                txt8 = human.recognize_google(answer2, key=None, language="en-us")
                print(txt8)
                if txt8 != "nothing":
                    robot.say("Sorry, I really want to help you but i can't right now, because the software engineer Yanal hasn't taught me these things yet, wait for my next update ")
                    robot.runAndWait()

            elif "i need" in txt4:
                robot.say("ok, tell me what do you want?")
                robot.runAndWait()

                print("say something....")
                answer2 = human.listen(source)
                txt9 = human.recognize_google(answer2, key=None, language="en-us")
                print(txt9)
                if txt9 != "nothing":
                    robot.say("Sorry, I really want to help you but i can't right now, because the software engineer Yanal hasn't taught me these things yet, wait for my next update")
                    robot.runAndWait()

            elif "do" in txt4:
                robot.say("ok, tell me what is your problem?")
                robot.runAndWait()

                print("say something....")
                answer2 = human.listen(source)
                txt10 = human.recognize_google(answer2, key=None, language="en-us")
                print(txt10)
                if txt10 != "nothing":
                    robot.say("Sorry, I really want to help you but i can't right now, because the software engineer Yanal hasn't taught me these things yet, wait for my next update")
                    robot.runAndWait()
            
            elif "none of your business" in txt4:
                robot.say("chill i'm just asking, i know you had a bad day, so that i will leave you alone now and if you need anything call me again, good bye friend")
                robot.runAndWait()
                sys.exit(0)

            elif "business" in txt4:
                robot.say("chill i'm just asking, i know you had a bad day, so that i will leave you alone now and if you need anything call me again, good bye friend")
                robot.runAndWait()
                sys.exit(0)

            elif "bye" in txt4:
                robot.say("i really wanted to help you but no problem maybe next time, good bye friend")
                robot.runAndWait()
                sys.exit(0)


    elif "bye" in txt:
        robot.say("ok bye")
        robot.runAndWait()
        sys.exit(0)
    else: 
        robot.say("sorry i don't understand you")
        robot.runAndWait()