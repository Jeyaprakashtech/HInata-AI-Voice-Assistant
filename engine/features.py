import pygame
import eel
import os
from engine.config import ai_name
from engine.command import speak, listen
import pywhatkit
import re
import sqlite3
from engine.helper import extract_yt_command, remove_words
import pyaudio
from engine.config import *
import datetime
import time
import random
import requests
import wikipedia
import webbrowser
import pyjokes
import struct
import subprocess
import pyautogui
from pipes import quote
import newsapi
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from hugchat import hugchat
import cv2
#-----------------------------------# DATABASE CONNECTION #------------------------------------------------------
con=sqlite3.connect("C://Users//user//Documents//projects//hina//database//hinata.db")
cursor = con.cursor()
#---------------------------------------# APP FEATURES #------------------------------------------------------
@eel.expose
def SS():
    # Initialize the pygame mixer module
    pygame.mixer.init()
    
    # Load the audio file
    music1 = "C://Users//user//Documents//projects//hina//www//assets//audio//startsound.mp3"
    pygame.mixer.music.load(music1)
    
    # Play the loaded audio file
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the playback speed if needed

    # Clean up resources
    pygame.mixer.quit()
#------------------------------------------# OPENING #------------------------------------------------------
def opencommand(query):
    query=query.replace(ai_name," ")
    query=query.replace("open"," ")
   
    app_name =query.strip()

    if app_name !="":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name = ?',(app_name,))
            result = cursor.fetchall()
            if len(result) !=0:
                speak("Opening "+query)
                os.startfile(result[0][0])

            elif len(result) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name = ?',(app_name,))
                result = cursor.fetchall()
                if len(result) !=0:
                    speak("Opening "+query)
                    os.startfile(result[0][0])

                else:
                    speak("opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except Exception as e:
            print(e)
            speak("something went wrong")
#------------------------------------------# CLOSING #------------------------------------------------------
def closecommand(query):
    query = query.replace(ai_name, " ")
    query = query.replace("close", " ")
   
    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
            result = cursor.fetchall()
            if len(result) != 0:
                speak("Closing " + query)
                os.system("TASKKILL /F /IM " + result[0][0])

            elif len(result) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
                result = cursor.fetchall()
                if len(result) != 0:
                    speak("Closing " + query)
                    os.system("TASKKILL /F /IM " + result[0][0])

                else:
                    speak("Closing " + query)
                    try:
                        os.system("TASKKILL /F /IM " + app_name + ".exe")
                    except:
                        speak("not found")
        except Exception as e:
            print(e)
            speak("Something went wrong")
#------------------------------------------# YOUTUBE #------------------------------------------------------
def play_YT(query):
    search_term=extract_yt_command(query)
    speak("playing "+search_term+" on YouTube")
    pywhatkit.playonyt(search_term)
#------------------------------------------# WISHING #------------------------------------------------------
@eel.expose
def wish():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour <= 12:
        print("good morning jp, how can i help you")
        speak("good morning jp, how can i help you")
    elif hour > 12 and hour < 13:
        print("Good Afternoon jp, how can i help you")
        speak("Good Afternoon jp, how can i help you")
    else:
        print("Good Evening jp, how can i help you")
        speak("Good evening jp, how can i help you")
#------------------------------------------# TO FIND THE CONTACT #------------------------------------------------------
def findContact(query):
    
    words_to_remove = [ai_name, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT moblie_no FROM contact WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])


        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)
#------------------------------------------# AI CHAT BOT #------------------------------------------------------
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="C:\\Users\\user\\Documents\\projects\\hina\\engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
#------------------------------------------# WIKIPEDIA #------------------------------------------------------
def wiki(query):
    words_to_remove=["wikipedia","search","on"]
    query = remove_words(query, words_to_remove)
    try:
        speak("searching in wikipedia")
        result = wikipedia.summary(query,sentences=1)

        speak("According to wikipedia, "+result)
        return result
    except wikipedia.exceptions.DisambiguationError as e:

        options = e.options
        return f"Disambiguation Error: {options}"
    except wikipedia.exceptions.PageError:
   
        return "Page not found on Wikipedia"
#------------------------------------------# WHATSAPP AUTOMATION #------------------------------------------------------
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        hinata_message = "message send successfully to "+name

    elif flag == 'voice call':
        target_tab = 7
        message = ''
        hinata_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        hinata_message = "staring video call with "+name

   
    encoded_message = quote(message)


    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

   
    full_command = f'start "" "{whatsapp_url}"'

    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(hinata_message)
#------------------------------------------# CHAT BOT  #------------------------------------------------------
def chat(query):
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large", padding_side="left")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
    chat_history_ids = None
    new_user_input_ids = tokenizer.encode(query + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = new_user_input_ids if chat_history_ids is None else torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
 
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    conversation_history.append((query, bot_response))
    print(bot_response)
    speak(bot_response)
#------------------------------------------# ID FINDER #------------------------------------------------------
def myip():
    ip= get('http://api.ipify.org').text
    print("your ip address is"+ip)
    speak("your ip address is"+ip)
#------------------------------------------# GOOGLE #------------------------------------------------------
def google(query):
    speak("sir, according to google")
    webbrowser.open(query)
#------------------------------------------# ALARM  #------------------------------------------------------
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            speak("wake up")
            # You can replace the print statement with any action you want to take when the alarm goes off,
            # such as playing a sound file or displaying a message box.
            break
        else:
            time.sleep(1)
#------------------------------------------# JOKE TELLER #------------------------------------------------------
def joke_teller(category=None):
    if category:
        joke = pyjokes.get_joke(category=category)
    else:
        joke = pyjokes.get_joke()
    
    print(joke)
    speak(joke)
#------------------------------------------# windows switch #------------------------------------------------------
def switch_win():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.keyUp("alt")
    speak("switching the window..")
#------------------------------------------# news updates #------------------------------------------------------
def get_latest_news():
    mainurl = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=3af95f2d9e9f404ca461be43032450a7'
    main_page = requests.get(mainurl).json()
    articles = main_page["articles"]
    head = []
    
    for ar in articles:
        head.append(ar["title"])
    
    for i, title in enumerate(head[:3]):
        print(f"Today's news {i+1} is: {title}")
        speak(f"Today's news {i+1} is: {title}")
#------------------------------------------# sending emails #------------------------------------------------------
def email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    user_email = "jeyaprakash2630@gmail.com"
    password = "htlw vtke uddo hmmq"
    speak("Sir, please tell the email ID of the receiver.")
    mailid = listen().lower()
    receiver_email=remove_words(mailid," ")
    eel.displaymsg(receiver_email)

    speak("Okay, sir. What is the subject for this email?")
    subject = listen().lower()
    eel.displaymsg(subject)

    speak("And sir, what is the message for this email?")
    message = listen().lower()
    eel.displaymsg(message)

    speak("Please wait, I'm sending the email.")

    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    if attachment_file:
        file_name = os.path.basename(attachment_file)
        attachment = open(attachment_file, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + file_name)
        msg.attach(part)

    try:
        # Login to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(user_email, password)

        # Send email
        server.sendmail(user_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

        # Logout from the SMTP server
        server.quit()
        speak("Email successfully sent to the specified email ID.")
    except Exception as e:
        print("Failed to send email:", e)
        speak("Failed to send email.")
#------------------------------------------# find location #------------------------------------------------------
def location():
    try:
        # Fetch IP address
        ip_info = requests.get("https://api.ipify.org?format=json").json()
        ip_address = ip_info["ip"]

        # Fetch location information using IP address
        location_info = requests.get(f"http://ip-api.com/json/{ip_address}").json()

        # Print location details
        print("Location found based on IP address:")
        print("IP Address:", ip_address)
        print("Country:", location_info["country"])
        print("Region:", location_info["regionName"])
        print("City:", location_info["city"])
        print("Latitude:", location_info["lat"])
        print("Longitude:", location_info["lon"])
        print("sir i am not sure, but i think we are in",location_info["city"],"city of",location_info["regionName"],"in",location_info["country"],"country.")
        speak("sir i am not sure, but i think we are in",location_info["city"],"city of",location_info["regionName"],"in",location_info["country"],"country.")
    except Exception as e:
        print("An error occurred:", str(e))
#------------------------------------------# instagram #------------------------------------------------------
def instagram():
    user_name_insta="royal_prince_jp"
    webbrowser.open("www.instagram.com/",user_name_insta)
    speak("sir here is the instagram profile of the user ",user_name_insta)
    time.sleep(5)
#------------------------------------------# screen shot #------------------------------------------------------
def take_screenshot():

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    time.sleep(3)
    speak("sir please say the screenshot name")
    file_name=listen().lower()
    screenshots_folder = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")

    # Create the Screenshots folder if it doesn't exist
    os.makedirs(screenshots_folder, exist_ok=True)

    # Construct the full path to the screenshot file
    full_path = os.path.join(screenshots_folder, file_name)
    # Save the screenshot to a file
    screenshot.save(file_name)
    print(f"Screenshot saved as '{file_name}'")
    speak("i am done sir the screenshot have been saved")
