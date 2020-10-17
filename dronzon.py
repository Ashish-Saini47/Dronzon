import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
import os
import subprocess
import pyjokes
import winshell
from twilio.rest import Client
import pyautogui
import cv2
import numpy as np
import pyowm
import smtplib
import shutil
from googletrans import Translator
import socket
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import selenium
from selenium import webdriver
from gtts import gTTS
import sys
import time
import random
import wolframalpha
from tkinter import *
from tkinter import messagebox
####################################################################### importing voice ###############################################################################
engine = pyttsx3.init('sapi5')
#rate = engine.getProperty('rate')
#print(rate)
#engine.setProperty("rate",170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

######################################################################### functions####################################################################################
client = wolframalpha.Client("KUKU9X-7A3EEEP68H")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def find(name):
    for root, dirs, files in os.walk("c:\\"):
        if name in files:
            return(root, name)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morining, welcome back, sir")
    elif(hour>=12 and hour <18):
        speak("Good Afternoon, welcome back, sir")
    else:
        speak("good evening, welcome back, sir")
    
    


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("trying to  listen.......")
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print("Trying to recogining.....")
        #r.adjust_for_ambient_noise(source)
        query=r.recognize_google(audio)#,language='en-IN' or language= 'hi')
        print("User said:")
        print(query)
        
    except Exception as e:
        print(e)
        print("Say it again ......")
        return "None"
    return query


def create_dir():
    parent_dir = "C:\\Users\\ravina sheoran\\Desktop"
    speak("Name the folder")
    dic_name = takecommand()
    
    try:
        path = os.path.join(parent_dir, dic_name)
        os.mkdir(path)
    except OSError:
        speak("Creation of the directory failed")
    else:
        speak("Successfully created the directory")


def delete_dir():
    parent_dir = "C:\\Users\\ravina sheoran\\Desktop"
    speak("name the folder")
    dic_name = takecommand()
    try:
        path = os.path.join(parent_dir, dic_name)
        os.rmdir(path)
    except OSError as error:
        speak("Deletion of the directory  failed" )
        speak(error)
    else:
        speak("Successfully deleted the directory  " )


def take_pic():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("C:/Users/ravina sheoran/Desktop/Dronzon/pic/newpic"+str(time.time())+".jpg",frame)
        #cv2.imshow("NewPicture.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def message_to():
    acc_id='AC2e9463331614e5eb291e9c3e884af6ac'
    auth_token ='cc2c3fcbeefdcf401baa7ab79aee5fbd'
    client =Client(acc_id, auth_token)
    message=client.messages.create(
        body= "jai mata di",
        from_ = '+12019285099',
        to= "+918239675766"
        )
    print(message.sid)


def make_call():
    acc_id='AC2e9463331614e5eb291e9c3e884af6ac'
    auth_token ='cc2c3fcbeefdcf401baa7ab79aee5fbd'
    client =Client(acc_id, auth_token)
    call=client.calls.create(
        
        from_ = '+12019285099',
        to= "+918058450553",
        url = "https://www.youtube.com/redirect?v=-AChTCBoTUM&event=video_description&q=https%3A%2F%2Fwww.twilio.com%2Fdocs%2Fguides%2Fhow-to-make-outbound-phone-calls-in-python&redir_token=vyUST3aQLsV51i_Y76rDDiLCnVp8MTU5Mjk4MTkwM0AxNTkyODk1NTAz"
        )
    print(call.sid)

def sec_f():
    entry_val= entry.get()
    user_name= entry_val
    sys.exit()
########################################################Items of dronzon ############################################################################################### 

my_name="Dronzon"
user_name="Ashish"
gender = "male"
intro= """ Myself Dronzon, I am your virtual assistant created by ashish. I can do more then 70 things for you. My functionlity is divided into three category first OS functions
second web functions or online functions third related to me.
OS functions are on system functions that can perform on created pc only to perform on another pc you have to change into the code.
web functions are thoughs which can perform online or on web browser.
related to me function, such as who are you , what you can do for me , etc...
"""

##################################################################### Main Function ########################################################################

if __name__ =="__main__":
  
    wishme()
    if gender =="male":
        res= "sir"
    else:
        res ="mam"
    while True:
        query = takecommand().lower()

################################################################## related to me #######################################################################################

        if "change my name" in query:
            speak("what's your name")
            user_name=takecommand()
            speak("What's your gender")
            gender =takecommand()
            speak("welcome"+user_name)

        elif "who am i" in query:
            speak(user_name)
        elif "hello" in query or "hey" in query:
            speak("Hello"+res)
            
        elif "how are you" in query:
            speak("I am fine. How are you")
            feel = takecommand()
            if "fine" in query or "good" in query:
                speak("good to know that")

        elif "don't listen" in query or "stop listing" in query:
            speak("For how much time, I don't have to listen")
            t= int(takecommand())
            time.sleep(t)
            speak("i am back")

        elif "good night" in query:
            speak("Good Night"+res)
            sys.exit()

        elif "exit" in query or "bye" in query :
            speak("bye"+res)
            sys.exit()

        elif "who created you" in query:
            speak("my creater is Ashish Saini")

        elif "when you are created" in query:
            speak("starting date of my creation is 12 june 2020")

        elif "who are you" in query:
            speak(intro)

#################################################################### Os functions ################################################################################# 
        elif "open cisco" in query or "open meeting app" in query:
            os.startfile("C:/Users/Public/Desktop/Cisco Webex Meetings.lnk")
        elif "open your code" in query:
            os.startfile("E:/Ashish Saini/Dronzon/dronzon.py")

        elif "open control panel" in query:
            os.startfile("C:/Users/ASHISH SAINI/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Control Panel.lnk")
        elif "take a pic" in query or "take a photo" in query:
            take_pic()
            speak("pic has been taken")

        elif "shutdown system" in query:
            subprocess.call('shutdown /p /f')

        elif "restart pc" in query:
            os.system("shutdown /r /t 1");

        elif "hibernate" in query:
            subprocess.call(["shutdown", "/h"])

        elif "log off" in query or "signout" in query:
            os.system("shutdown -l") 

        elif "write a note" in query or "write for me" in query:
            speak("what should i write"+res)
            note= takecommand()
            file= open("E:/Ashish Saini/Dronzon/Dronzon Notes/Dronzon.txt", "w")
            speak("should i include date and time")
            rep=takecommand()
            if "yes" in rep or "sure" in rep:
                strTime= datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(note)
                file.close()
                
            else:
                file.write(note)
                file.close()
            speak("note has been written"+res)
            
        elif "open note" in query:
            speak("here your note"+res)
            file= open("E:/Ashish Saini/Dronzon/Dronzon Notes/Dronzon.txt", "r")
            a=file.read()
            print(a)
            speak(a)
            file.close()

        elif "clear note" in query:
            file = open("E:/Ashish Saini/Dronzon/Dronzon Notes/Dronzon.txt","r+")
            file.truncate(0)
            speak("note has been clear"+res)
            file.close()

        elif "empty recycle bin" in query:
            winshell.recycle_bin().empty(confirm= False, show_progress= False, sound = True)
            speak("Recycle bin is empty")

        elif "change name" in query:
            speak("What whould you want to call me"+res)
            my_name=takecommand()
            speak("Thanks for changing for name")

        elif "play music" in query:
            music_dir ="C:/Users/ASHISH SAINI/Desktop/New folder"
            song = os.listdir(music_dir)
            speak("enjoy"+res)
            os.startfile(os.path.join(music_dir, song[0]))

        elif "play movie" in query:#yo bhi naa kaam kr rho 
            movie_dir="C:/Users/ravina sheoran/Desktop/Music/Telegram Desktop"
            movie = os.listdir(movie_dir)
            speak("enjoy"+res)
            os.startfile(os.path.join(movie_dir, movie[0]))

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)

        elif "open power point presentation" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft PowerPoint 2010.lnk")

        elif "open ms word" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Word 2010.lnk")

        elif "open execel" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Excel 2010.lnk")

        elif "open ms paint" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft PowerPoint 2010.lnk")

        elif "open python idle" in query:
            os.startfile("C:/Users/ASHISH SAINI/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/IDLE (Python 3.8 32-bit).lnk")

        elif "open command prompt" in query:
            subprocess.Popen("cmd")

        elif "open notepad" in query:
            subprocess.Popen("notepad")

        elif "open chrome" in query:
            os.startfile("C:/Users/Public/Desktop/Google Chrome.lnk")

        elif "open vlc" in query:
            os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")

        elif "open notepad ++" in query:
            os.startfile("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")

        elif "open firefox" in query:
            os.starfile("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

        elif "open adobe reader" in query:
            os.startfile("C:\\Program Files (x86)\\Adobe\\Reader 9.0\\Reader\\AcroRd32.exe")

        elif "open winamp" in query:
            os.startfile("C:\\Program Files (x86)\\Winamp\\winamp.exe")

        elif "are you online"in query:
            ip = socket.gethostbyname(socket.gethostname())
            if ip =="127.0.0.1":
                speak("no"+res)
                
            else:
                speak("yes"+res)
            
        elif "take a screenshot" in query:
            img = pyautogui.screenshot()
            img.save("E:\\Ashish Saini\\Dronzon\\Dronzon screenshot\\"+str(time.time())+".jpg")
            speak("screenshot takken")

        elif "create folder" in query:
            create_dir()
            speak("new folder has been created")
            
        elif "delete folder" in query:
            delete_dir()
            speak("folder has been deleted")
            
        elif "close window" in query:
            speak("which window you want to close")
            name= takecommand()
            os.system("TASKKILL /F /IM "+name+".exe")

        elif "open vs code"in query or "open visual studio" in query:
            os.startfile("C:/Users/ASHISH SAINI/Desktop/Visual Studio Code.lnk")

        elif "open teamviewer" in query:
            os.startfile("C:/Users/Public/Desktop/TeamViewer.lnk")

        elif "search on pc" in query:
            speak("Name the you want to search")
            name=takecommand()
            a= find(name)
            speak(find(name))

        elif "copy" in query:
            shutil.copy("C:/Users/ravina sheoran/Desktop/New folder/dronzon.py", "C:/Users/ravina sheoran/Desktop/New folder (2)")

        elif "cut" in query:
            shutil.move("C:/Users/ravina sheoran/Desktop/New folder/dronzon.py", "C:/Users/ravina sheoran/Desktop/New folder (2)")

        elif "start video recording " in query or "chat video recording" in query:
            filename = 'C:/Users/ravina sheoran/Desktop/Dronzon/Videos/video'+str(time.time())+'.avi'
            frames_per_second = 24.0
            res = '720p'
            def change_res(cap, width, height):
                cap.set(3, width)
                cap.set(4, height)
            STD_DIMENSIONS =  {
                "480p": (640, 480),
                "720p": (1280, 720),
                "1080p": (1920, 1080),
                "4k": (3840, 2160),
            }
            def get_dims(cap, res='1080p'):
                width, height = STD_DIMENSIONS["480p"]
                if res in STD_DIMENSIONS:
                    width,height = STD_DIMENSIONS[res]
                change_res(cap, width, height)
                return width, height
            VIDEO_TYPE = {
                'avi': cv2.VideoWriter_fourcc(*'XVID'),
                'mp4': cv2.VideoWriter_fourcc(*'XVID'),
            }

            def get_video_type(filename):
                filename, ext = os.path.splitext(filename)
                if ext in VIDEO_TYPE:
                  return  VIDEO_TYPE[ext]
                return VIDEO_TYPE['avi']



            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

            while True:
                ret, frame = cap.read()
                out.write(frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


            cap.release()
            out.release()
            cv2.destroyAllWindows()

            
        elif "start voice recording" in query:
            speak("what you want to record")
            query = takecommand()
            myobj = gTTS(text = query, lang ='en', slow = False)
            myobj.save("C:/Users/ravina sheoran/Desktop/Dronzon/Audio/DronzonRecorded"+str(time.time())+".mp3")
            os.system("mpg321 DronzonRecorded.mp3")
################################################################# Web functions ###################################################################################
        elif "what is" in query:#####yo na call rho
            res =  client.query(query)
            output= next(res.result).text
            speak(output)
            
        elif "open flipkart" in query:
            webbrowser.open("https://www.flipkart.com/")

        elif "open amazon" in query:
            webbrowser.open("https://www.amazon.com/")

        elif "open paytm" in query:
            
            webbrowser.open("https://paytm.com/")

        elif "login insta" in query or "login instagram" in query:
            pass

        elif "make call" in query:
            make_call()
            
        elif "login facebook" in query:
           
            
            username = "8058450553"
            password ="hloindia"
            url = "https://www.facebook.com/"
            driver = webdriver.Chrome("C:/Users/ASHISH SAINI/Downloads/chromedriver_win32/chromedriver.exe")
            driver.get(url)
            driver.find_element_by_id('email').send_keys(username)
            driver.find_element_by_id('pass').send_keys(password)
            driver.find_element_by_id('loginbutton').click()

        elif "news" in query:#yon bhi kaam naa kr rho
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            # Print news title, url and publish date
            for news in news_list:
              speak(news.title.text)
              #print(news.link.text)
              speak(news.pubDate.text)
              #print("-"*60)
              
        elif "send mail" in query:
            s= smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login("merayaar2h@gmail.com", "jaibhole123")
            message= "ye le mail"
            s.sendmail("merayaar2h@gmail.com","ashish.m.saini999@gmail.com", message)
            
        elif "what's the weather" in query or "what is the weather" in query:#yo bhi kaam naa kr 
            owm = pyowm.OWM("f7c20d7a30fd7b8182bb9846aa310941")
            place = owm.weather_at_place("pilani")
            weth = place.get_weather()
            Speak(weth)
            
        elif "open yahoo" in query:
            
            webbrowser.open("https://in.yahoo.com/")
    
        elif "where is " in query:
            indx= query.split().index("is")
            query = query.split()[indx + 1:]
            webbrowser.open("https://www.google.nl/maps/place"+"+".join(query))

        elif "send sms " in query:
           # speak("to whom you want to sms")
            #name= takecommand()
            #if name in contact_list:
             #   speak("what you want to send")
              #  mess= takecommand()
            message_to()
            speak("message has been sent")
            #else:
               # speak("No such name found in contact list")

        elif "wikipedia" in query:
            speak("Searching on wikipedia")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            
        elif "hindi meaning of" in query:
            indx= query.split().index("of")
            query = query.split()[indx + 1:]
            ranslator = Translator()
            ts= ranslator.translate(str(query), src= 'en', dest = 'hi')
            messagebox.showinfo("Hindi meaning of "+query ,ts.text)
            
        elif "on youtube" in query:
            indx= query.split().index("youtube")
            query = query.split()[indx + 1:]
            webbrowser.open("https://youtube.com/results?search_query="+'+'.join(query))

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "on google" in query:
            indx= query.split().index("google")
            query = query.split()[indx + 1:]
            webbrowser.open("https://google.com/search?q="+'+'.join(query))

        elif "joke" in query:
            a=pyjokes.get_joke()
            speak(a)
            print(a)

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        elif "open insta"in query or "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")

        elif "open photo" in query:
            webbrowser.open("https://www.google.com/photos/about/")

        elif "open gmail" in query:
            webbrowser.open("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

        elif "open map" in query:
            webbrowser.open("https://www.google.com/maps/")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com/")

        elif "open yahoo mail" in query:
            webbrowser.open("https://login.yahoo.com/?.src=ym&lang=en-IN&done=https%3A%2F%2Fmail.yahoo.com%2F%3F.intl%3Din%26.lang%3Den-IN%26.partner%3Dnone%26.src%3Dfp%26guce_referrer%3DaHR0cHM6Ly9pbi55YWhvby5jb20v%26guce_referrer_sig%3DAQAAALbwm6ClOL-GtXbTeygxEMGGK_9vsFtncVEhHL-RZ68wdPrAoiTdqsdcTWGKsSETk4HtoZlMEPZa3BHUryj_0YK7q7EpU7t038vwQqGHsF1lUAQIsSSkW-ibCwuvN6sQuthbR2PqMOqNZsGSOomSNL0GNjCjsN4Rj_hO4RcTZ2up&.partner=none")

        elif "rediff mail" in query:
            webbrowser.open("https://mail.rediff.com/cgi-bin/login.cgi")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        else:
            pass
           # speak("I can't anable to process your request right now. Sorry for that")
