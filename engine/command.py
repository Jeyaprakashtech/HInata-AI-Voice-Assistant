import pyttsx3
import speech_recognition as sr
import eel
import random
#--------------------------------------------------------#SPEAK FUNCTION#------------------------------------------------------------------
def speak(text):
    text=str(text)
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    female_index = 1
    engine.setProperty('voice', voices[female_index].id)
    engine.setProperty('rate', 145)
    engine.say(text)
    print(text)
    eel.displaymsg(text)
    eel.recivertxt(text)
    engine.runAndWait()
#----------------------------------------------------# SPEECH RECOG FUNCTION #------------------------------------------------------------------
def listen():
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        eel.displaymsg("listening.....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=5)
    try:
        eel.showloader()
        print("Recognizing.....")
        eel.displaymsg("Recognizing.....")
        query = r.recognize_google(audio)
        print(f"You said, {query}")
        eel.displaymsg(query)
        
    
    except Exception as e:
        return ""

    return query.lower()
#--------------------------------------------------------#TASK PREFORMANCE#------------------------------------------------------------------
def process_command(query):
    command=query.lower()
    eel.sendertxt(command)
    try:
        print(command)
        if "open" in command:
            from engine.features import opencommand
            opencommand(command)
        elif "close" in command:
            from engine.features import closecommand
            closecommand(command)
        elif "on youtube" in command:
            from engine.features import play_YT
            play_YT(command)
        elif "send a message" in command or "phone call" in command or "video call" in command:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(command)
            if(contact_no != 0):
                message = ""
                if "send a message" in command:
                    flag = 'message'
                    speak("what message to send")
                    message = listen()
                    
                elif "phone call" in command or "voice call" in command:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, message, flag, name)
        elif "wikipedia" in command:
            from engine.features import wiki
            wiki(command)
        elif "my ip address" in command:
            from engine.features import myip
            myip()
        elif "set alarm" in command:
            from engine.features import set_alarm
            speak("sir, tell me the time to set the alarm") 
            time = listen()
            set_alarm(time)
        elif "tell me a joke" in command:
            from engine.features import joke_teller
            joke_teller()
        elif "google" in command:
            speak("sir, what should i search in google")
            google_cmd=listen()
            from engine.features import google
            google(google_cmd)
        elif "shut down the system" in command:
            os.system("shutdown /s /t 5")
        elif "restart the system" in command:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in command:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "switch the window" in command:
            from engine.features import switch_win
            switch_win()
        elif "news" in command:
            from engine.features import get_latest_news
            get_latest_news()
        elif "send a email" in command or "send a mail" in command:
            from engine.features import email
            email()
        elif "where i am" in command or "where are you" in command:
            from engine.features import location
            location()
        elif "take" in command and "screenshot" in command:
            from engine.features import take_screenshot
            take_screenshot()
        else:
            from engine.features import chatBot
            chatBot(command)
    except Exception as e:
        print(e)
        speak("something went wrong")
    eel.showhood()
#--------------------------------------------------------#VOICE COMMAND INPUT#------------------------------------------------------------------
@eel.expose
def voice_command():
    try:
        query = listen()
        print(query)
        process_command(query)

    except Exception as e:
        print(e)
        speak("something went wrong")
#--------------------------------------------------------#TEXT COMMAND INPUT#------------------------------------------------------------------
@eel.expose
def  text_command(txtcommand):
    try:
        print(txtcommand)
        process_command(txtcommand)

    except Exception as e:
        print(e)
        speak("something went wrong")
