import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=10 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey i am raavan how can i help you sir  I do stuf like ")
    print(" 1.open youtube  2.open google  3.open facebook  4.open instagram  5.play music  6.what is the time  and many more")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sr4cr7cr8@gmail.com','Aniket1021998')
    server.sendmail('aniket.sudke10@gmail.com', to, content)
    server.close()



def takeCommand():
    #it takes microphone input from the user and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #curser on listen and press ctr to see info about listen.
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language='en-in')
        print("User said:", query )

    except Exception:
        #print(e)
        print("Say that again please ..")
        #here None is not python None it is only string we want to return
        
        return "None"

    return query





if __name__=="__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        # logi for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir = 'E:\\Video song'
            songs = os.listdir(music_dir)
            print(songs)
            i = random.randint(1,10)
            os.startfile(os.path.join(music_dir,songs[i]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'sublime' in query:
            paths="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(paths)

        elif 'send mail to ram' in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = "aniket.sudke10@gmail.com"
                sendEmail(to ,content)
                speak("Successful!")

            except Exception as e:
                print(e)
                print("Sorry")


        


        