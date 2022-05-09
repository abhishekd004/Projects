import os
import pyttsx3 as p
import time
import random
#input must be in small letters
#can open broesers,camera,spotify,paint,calculator,notepad,command prompt,jupyter,atom
print("~~~~~~~~~~~~~~ WELCOME ~~~~~~~~~~~~~~~")
p.speak("WELCOME")
#c is for taking task
while True:
    print("~"*140)
    p.speak("how I can help u \nplease enter : ")
    c = input("\nHow i can help u \nplease enter : ")
    if ("don't" in c) or ("dont" in c) or ('do not' in c):
        p.speak("OK \n What i can do for u")
        pass
        #c=input("ok,what I can do for u,\nEnter :")
    elif ("exit" == c) or ("close" == c) or ("quit" ==c) or ("bye" == c):
        print("~~~~~~~~~~~~~~~ THANKS ~~~~~~~~~~~~~~~~")
        p.speak("thanks,for coming \n bye")
        break
    elif ("run" in c) or ("execute" in c) or ("open" in c) or ("launch" in c):
        if (("browser" in c) and (("chrome" not in c) and ("firefox" not in c) and ("microsoft-edge" not in c) and ("edge" not in c))):
            p.speak("plz enter which browser u want to open \n1. chrome \n2. firefox \n3. edge")
            b= input("plz enter which browser u want to open \n1. chrome \n2. firefox \n3. edge : ")
            # b is for browser option
            if ("chrome" in b) or ("1" in b):
                p.speak("opening chrome")
                os.system("chrome")
            elif ("firefox" in b) or ("2" in b):
                p.speak("opening firefox")
                os.system("firefox")
            elif ("edge" in b) or ("3" in b) or ("microsoft" in b):
                p.speak("opening microsoft edge")
                os.system("start msedge")
            else:
                print("not available")
                p.speak("not available")
        elif ("chrome" in c) or ("1" in c):
            p.speak("opening chrome")
            os.system("chrome")
        elif ("firefox" in c) or ("2" in c):
            p.speak("opening firefox")
            os.system("firefox")
        elif ("edge" in c) or ("3" in c) or ("microsoft" in c):
            p.speak("opening microsoft edge")
            os.system("start msedge")
        elif ("spotify" in c) or ("music" in c):
            p.speak("opening spotify")
            os.system("start spotify")
        elif ("camera" in c):
            p.speak("opening camera")
            os.system("start microsoft.windows.camera:")
        elif ("calculator" in c) or ("calculation" in c):
            p.speak("opening calculator")
            os.system("calc")
        elif ("paint" in c):
            p.speak("opening paint")
            os.system("mspaint")
        elif ("notepad" in c) or ("editor" in c) or ("texteditor" in c):
            p.speak("openning notepad")
            os.system("notepad")
        elif ("cmd" in c) or ("command" in c) or ("prompt" in c):
            p.speak("openning command prompt")
            os.system("start")
        elif ("atom" in c):
            p.speak("openning atom")
            os.system("start atom")
        else:
            print("not available")
            p.speak("not available")
    elif ("close" in c) or ("exit" in c) or ("kill" in c):
        if ("browser" in c) and (("chrome" not in c) and ("firefox" not in c) and ("microsoft-edge" not in c) and ("edge" not in c)):
            p.speak("plz enter which browser u want to close \n1. chrome \n2. firefox \n3. edge")
            b= input("plz enter which browser u want to close \n1. chrome \n2. firefox \n3. edge")
                # b is for browser option
            if ("chrome" in b) or ("1" in b):
                p.speak("closing chrome")
                os.system("taskkill/im chrome.exe")
            elif ("firefox" in b) or ("2" in b):
                p.speak("closing firefox")
                os.system("taskkill/im firefox.exe")
            elif ("edge" in b) or ("3" in b) or ("microsoft" in b):
                p.speak("closing microsoft edge")
                os.system("taskkill/im msedge.exe")
        elif ("chrome" in c):
            p.speak("closing chrome")
            os.system("taskkill/im chrome.exe")
        elif ("firefox" in c):
            p.speak("closing firefox")
            os.system("taskkill/im firefox.exe")
        elif ("edge" in c) or ("microsoft" in c):
            p.speak("closing microsoft edge")
            os.system("taskkill/im msedge.exe")
        elif ("spotify" in c) or ("music" in c):
            p.speak("closing spotify")
            os.system("taskkill/im spotify.exe")
        elif ("camera" in c):
            p.speak("closing camera")
            os.system("taskkill/im WindowsCamera.exe")
        elif ("calculator" in c) or ("calculation" in c):
            p.speak("closing calculator")
            os.system("taskkill/im calculator.exe")
        elif ("paint" in c):
            p.speak("closing paint")
            os.system("taskkill/im mspaint.exe")
        elif ("notepad" in c) or ("editor" in c)	or ("texteditor" in c):
            p.speak("closing notepad")
            os.system("taskkill/im notepad.exe")
        else:
            p.speak("not supported")
            print("not supported")
    elif ("browser" in c) and (("chrome" not in c) or ("firefox" not in c) or ("microsoft-edge" in c)):
        p.speak("plz enter which browser u want to open \n1. chrome \n2. firefox \n3. edge")
        b= input("plz enter which browser u want to open \n1. chrome \n2. firefox \n3. edge : ")
        # b is for browser option
        if ("chrome" in b) or ("1" in b):
            p.speak("opening chrome")
            os.system("chrome")
        elif ("firefox" in b) or ("2" in b):
            p.speak("opening firefox")
            os.system("firefox")
        elif ("edge" in b) or ("3" in b) or ("microsoft" in b):
            p.speak("opening microsoft edge")
            os.system("start msedge")
        else:
            print("not available")
            p.speak("not available")
    elif ("chrome" in c):
        print("\nopenning chrome\n")
        p.speak("opening chrome")
        os.system("chrome")
    elif ("firefox" in c):
        print("\nopenning firefox\n")
        p.speak("opening firefox")
        os.system("firefox")
    elif ("edge" in c) or ("microsoft" in c):
        p.speak("opening microsoft edge")
        os.system("start msedge")
    elif ("spotify" in c) or ("music" in c):
        print("\nopenning spotify\n")
        p.speak("opening spotify")
        os.system("start spotify")
    elif ("camera" in c):
        print("\nopenning camera\n")
        p.speak("opening camera")
        os.system("start microsoft.windows.camera:")
    elif ("calculator" in c) or ("calculation" in c):
        print("\nopenning calculator\n")
        p.speak("opening calculator")
        os.system("calc")
    elif ("paint" in c) or ("draw" in c):
        print("\nopenning paint\n")
        p.speak("opening paint")
        os.system("mspaint")
    elif ("notepad" in c) or ("editor" in c) or ("texteditor" in c):
        print("\nopenning notepad\n")
        p.speak("openning notepad")
        os.system("notepad")
    elif ("cmd" in c) or ("command" in c) or ("prompt" in c):
        print("\nopenning command prompt\n")
        p.speak("openning command prompt")
        os.system("start")
    elif ("atom" in c):
        p.speak("openning atom")
        print("\natom\n")
        os.system("start atom")
    elif ("jupyter" in c) or ("notebook" in c):
        p.speak("openning jupyter notebook")
        print("\nopenning jupyter notebook\n")
        os.system("jupyter notebook")
    elif ("play" in c) or ("game" in c):
        print("OK\nwhat u wanna play")
        p.speak("OK\nwhat u wanna play\n1. guess the number\n2. guess the shape")
        a=input("1. guess the number\n2. guess the shape \n=> ")
        if ("1" in a) or ("number" in a) or ("no" in c):
            print("RULE:\nu have to guess a number between 1 to 50\nu have 3 chances to guess right")
            p.speak("RULE:\nu have to guess a number between 1 to 50\nu have 3 chances to guess right")
            n=3
            b = random.choice([i for i in range(51) ])
            #genrate a random no between 1 t0 50
            while n>0:
                print("chance left {}".format(n))
                p.speak("enter the number")
                d = int(input("enter the number : "))
                if d==b:
                    print("Great, you win")
                    p.speak("Great, you win")
                    break
                elif n >1:
                    p.speak("wrong guess, try again")
                    print("Wrong Guess\nTry Again")
                else:
                    print("Better Luck Next Time")
                    p.speak("Better Luck Next Time")
                n-=1
        elif ("2" in a) or ("shape" in a):
            for i in range(11):
                for j in range(11-i):
                    print("",end=' ')
                for k in range(i):
                    print("*",end =' ')
                print()
            p.speak("enter the shape name")
            d=input("enter the shape name : ")
            if ("triangle" in d):
                print("Hurray , you are right")
                p.speak("Hurray , you are right")
                for i in range(11):
                    for j in range(11):
                        print("*",end =' ')
                    print()
                p.speak("enter the shape name")
                d=input("enter the shape name : ")
                if ("square" in d):
                    print("Hurray , you are right")
                    p.speak("Hurray , you are right")
                else:
                    print("better luck next time")
                    p.speak("better luck next time")
            else:
                print("better luck next time")
                p.speak("better luck next time")
    else:
        print("sorry, I don't get it \nTry Again")
        p.speak("sorry, I don't get it \nTry Again")
