import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia
import smtplib
import webbrowser as wb
import os
engine=pyttsx3.init()
sentence= "Hi I am your Assistant."

voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #can use 0-5

newvoiceRate=200
engine.setProperty('rate',newvoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time=datetime.datetime.now().strftime("%I: %M :%S")
    speak("Time is")
    speak(Time+ "seconds")

def date():
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("Today is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Sir!")
    hour =datetime.datetime.now().hour
    if hour>=6 and hour <= 12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    elif hour >18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Friday at your service. How can I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 #wait 1 s before start to listen
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en=US")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"  
        
    return query

def sendmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "123test")
    server.sendmail("test@gmail.com", to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query: #what is the current time
            time()
        elif "date" in query:
            date()
        elif "offline" in query: #go offline
            quit()
        elif "wikipedia" in query:  # search on wikipedia university/html/AI/instagram
            speak("Searching in wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2) #return 2nd sentence after searching
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                # sendmail(to, content) #enable less secure app
                speak("Email sent Successfully!")
            except Exception as e:
                print(e)
                speak("Unable to send the message")
        elif "chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("Shutdown /s /t 1")
        elif "restart" in query:
            os.system("Shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir = "C:\Users\DELL\Music\Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[3]))