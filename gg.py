import os
import pyttsx3 as a
print("Hello There")
a.speak("hello there")
print("I am Kapil Dev")
a.speak("i am kapil dev")
print("I will help you to open some files and folders present in your pc")
a.speak("i will help you to open some files and folders present in your pc")
print("Files and folders which i was able to open in your pc is :-")
a.speak("files and folders which i was able to open in your pc is")
print(" 1.Google Chrome            2.Microsoft Edge            3.Control panel")
print(" 4.Anaconda Navigator       5.Python                    6.VLC Media Player")
print(" 7.Window Media Player      8.Notepad                   9.Notepad++")
print("10.Directory of your pc ")
print("You can run any of them")
a.speak("You can run any of them")

while True:
    print("please type what you want to do:", end=" ")
    a.speak("please type what you want to do")
    p = input()

    if (("dont " in p) or ("don't " in p) or ("not " in p) or ("Dont" in p) or ("Don't " in p) or ("Not " in p) or
            ("never " in p) or ("Never " in p) or ("DON'T " in p) or ("DONT " in p) or ("NOT " in p) or ("NEVER " in p)):
            a.speak("your operation is performed successfully")
            print("your operation is performed successfully")

    elif (("run" in p) or ("Run" in p) or ("RUN" in p) or ("execute" in p)or ("Execute" in p) or ("EXECUTE" in p) or
            ("start" in p) or ("Start" in p) or ("START" in p) or ("open" in p) or ("Open" in p) or ("OPEN" in p)):

            if (("directory" in p) or ("Directory" in p) or ("DIRECTORY" in p) or ("files" in p) or ("Files" in p) or ("FILES" in p) #to open directory
                or ((("this" in p) or ("This" in p) or ("THIS" in p)) and (("pc" in p) or ("Pc" in p) or ("PC" in p)))):
                os.system("dir")
                a.speak("welcome to directory")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif (("notepad " in p) or ("Notepad " in p) or ("NOTEPAD " in p) or ("editor " in p) or ("Editor " in p) or ("EDITOR " in p) #to open notepad
                or ((("text " in p) or ("Text " in p) or ("TEXT " in p)) and (("editor " in p) or ("Editor " in p) or ("EDITOR " in p)))):
                os.system("notepad")
                a.speak("welcome to notepad")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif ("notepad++" in p) or ("Notepad++" in p) or ("NOTEPAD++" in p) or ("notepad ++" in p) or ("Notepad ++" in p) or ("NOTEPAD ++" in p):# to open notepad++
                os.system("notepad++")
                a.speak("welcome to notepad++")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif (("browser" in p) or ("Browser" in p) or ("BROWSER" in p) or ("google" in p) or ("Google" in p) or ("GOOGLE" in p)# to open chrome browser
                or ("chrome" in p) or ("Chrome" in p) or ("CHROME" in p)):
                os.system("chrome")
                a.speak("welcome to google chrome")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif ((("Microsoft" in p) or ("microsoft" in p) or ("MICROSOFT" in p)) and (("Edge " in p) or ("edge " in p) or ("EDGE " in p))):# to open microsoft EDGE
                os.system("msedge")
                a.speak("welcome to microsoft edge")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif ((("control" in p) or ("Control" in p) or ("CONTROL" in p)) and (("panel " in p) or ("Panel " in p) or ("PANEL" in p))): # to open control panel
                os.system("control")
                a.speak("welcome to control panel")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif("Anaconda " in p) or ("anaconda " in p) or ("ANACONDA " in p):# to run anaconda software
                os.system("anaconda-navigator")
                a.speak("welcome to anaconda navigator")                             #it cant run when you run this program in anaconda
                print("it cant run when you run this program in anaconda")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif ("vlc " in p) or ("Vlc " in p) or ("VLC" in p) or ("player" in p) or ("Player" in p) or ("PLAYER" in p):#f to run vlc media player
                os.system("vlc")
                a.speak("welcome to vlc media player")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif(((("media" in p) or ("Media" in p) or ("MEDIA" in p)) and (("player" in p) or ("Player" in p) or ("PLAYER" in p)))# to run window media player
                or ("video" in p) or ("Video" in p) or ("VIDEO" in p) or ("wmplayer" in p) or ("Wmplayer" in p) or ("Wmplayer" in p)):
                os.system("wmplayer")
                a.speak("welcome to window media player")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

            elif ("python" in p) or ("Python" in p) or ("PYTHON" in p):# to run python
                os.system("python")
                a.speak("welcome to python")
                print("your operation is performed successfully")
                a.speak("your operation is performed successfully")

    elif ("exit" in p) or ("Exit" in p) or ("EXIT" in p):
        break
    else:
        print()
        a.speak("try again")
        print("try again")
        a.speak("your input is invalid")
        print("**** your input is invalid ****")
        a.speak("please enter a valid operation")
        print("**** please enter a valid operation ****")
        print()
print("thank you for use this program sir")
a.speak("thank you for use this program sir")
print("i am always happy to halp you again ")
a.speak("i am always happy to halp you again")
print("I hope that you was enjou this program")
a.speak("i hope that you was enjoy this program")
print("Have a good day sir")
a.speak("Have a good day, sir")
