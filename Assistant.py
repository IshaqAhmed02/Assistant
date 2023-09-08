import pyttsx3                          # pip install pyttsx3
import speech_recognition as sr         # pip install speechRecognition
import datetime
import wikipedia                        # pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes                          # pip install pyjokes
import pywhatkit                        # pip install pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!")

    elif 12 <= hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("Hi Sir. Please tell me how may I help you")


def takeCommand():
    # this command takes mic input and gives speach output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        Speach = r.recognize_google(audio, language='en-in')
        print(f"User said: {Speach}\n")

    except Exception as e:
        print(e)
        print("can you repeat that please...")
        return "None"
    return Speach


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        Speach = takeCommand().lower()

        # Logic for executing tasks based on Speach
        if 'who is' in Speach:
            speak('Searching Wikipedia...')
            Speach = Speach.replace("wikipedia", "")
            results = wikipedia.summary(Speach, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in Speach:
            webbrowser.open("youtube.com")

        elif 'open google' in Speach:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in Speach:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in Speach:
            webbrowser.open("github.com")

         #you can add anything if you want

        if 'search' in Speach:
            song = Speach.replace('play', '')
            speak('playing....')
            pywhatkit.playonyt(song)

        elif 'the time' in Speach:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in Speach:
            pycharm = "Add your path"
            os.startfile(pycharm)

        elif 'joke' in Speach:
            speak(pyjokes.get_joke())

        elif 'email to' in Speach:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry iam unable send this email")

        elif 'close' in Speach:
            exit()
        else:
            speak("can you repeat that please")
