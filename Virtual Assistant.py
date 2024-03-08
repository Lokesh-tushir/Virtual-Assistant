import speech_recognition as sr  # Imports the speech recognition module for voice input
import pyttsx3  # Imports the pyttsx3 module for text-to-speech conversion
import datetime  # Imports the datetime module for time and date-related operations
import os  # Imports the os module for operating system-dependent functionalities
import wikipedia  # Imports the wikipedia module for fetching information from Wikipedia
import pyjokes  # Imports the pyjokes module for generating jokes
import pyautogui  # Imports the pyautogui module for controlling the mouse and keyboard
import ctypes  # Imports the ctypes module for system-level operations
import requests  # Imports the requests module for making HTTP requests
import psutil  # Imports the psutil module for retrieving system information
import operator  # Imports the operator module for mathematical operations
import smtplib  # Imports the smtplib module for sending emails
import phonenumbers  # Imports the phonenumbers module for phone number parsing and handling
import pywhatkit as kit  # Imports the pywhatkit module for WhatsApp-related operations
from search_on_wikipedia import search_on_wikipedia  # Imports the search\_on\_wikipedia function
from send_whatsapp_message import send_whatsapp_message  # Imports the send\_whatsapp\_message function
from find_ip_add import find_ip_add  # Imports the find\_ip\_add function
from latest_news import get_latest_news  # Imports the get\_latest\_news function
from search_on_google import search_on_google  # Imports the search\_on\_google function
from play_on_youtube import play_on_youtube  # Imports the play\_on\_youtube function
from find_temperature import find_temperature  # Imports the find\_temperature function
from online_ops import switch_the_window, open_run, window_button, clipboard, copy_text, paste_text, notification_bar, select_all_text, save_file, open_lock, show_important_functions, open_chat, minimise, home_screen, widget, file_manager, accessibility, project, control_panel, controller_bar, voice_typing, screen_cast, switch_language, extra_space, cut_the_text  # Imports various online operations
from phonenumbers import geocoder, carrier, timezone  # Imports phone number geocoding, carrier, and timezone functions
from time import sleep  # Imports sleep for adding delays
from email.mime.multipart import MIMEMultipart  # Imports MIMEMultipart for email composition
from email.mime.text import MIMEText  # Imports MIMEText for email composition

engine = pyttsx3.init('sapi5')  # Initializes the text-to-speech engine
voices = engine.getProperty('voices')  # Gets the available voices for the text-to-speech engine
engine.setProperty('voice', voices[0].id)  # Sets the voice for the text-to-speech engine
engine.setProperty('rate', 175)  # Sets the speech rate for the text-to-speech engine
engine.setProperty('volume', 1.0)  # Sets the volume for the text-to-speech engine

def wish_me():  # Defines the wish\_me function for greeting the user
            hour = int(datetime.datetime.now().hour)  # Gets the current hour
            if 6 <= hour <= 12:  # If the current hour is between 6 and 12
                speak("Good morning sir!")  # Speak "Good morning sir!"
                time = datetime.datetime.now().strftime("%H:%M")  # Gets the current time
                speak(f"the time is...{time}AM")  # Speak the current time in AM format
                speak("I'm your personal voice assistant kevin, How can I help you, sir?")  # Speak the introduction message
            elif 12 < hour <= 16:  # If the current hour is between 12 and 16
                speak("Good Afternoon sir!")  # Speak "Good Afternoon sir!"
                time = datetime.datetime.now().strftime("%H:%M")  # Gets
                speak(f"the time is...{time}PM")
                speak("I'm your personal voice assistant kevin, How can I help you, sir?")
        
            elif 16 < hour <= 19:
                speak("Good evning sir!")
                time = datetime.datetime.now().strftime("%H:%M")
                speak(f"the time is...{time}PM")
                speak("I'am your personal voice assistant kevin, How can I help you, sir?")    

            else:
                speak("sir, I am Kevin your personal voice assistance")
                time = datetime.datetime.now().strftime("%H:%M")
                speak(f"the time is...{time}")
                speak("please go to your bed? Good night and sleep tight")

def take_command():
            r = sr.Recognizer()
            print("Listening...")
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=None)
                r.energy_threshold=300
                r.dynamic_energy_threshold=True
                r.pause_threshold=0.8
                r.operation_timeout=None
                query = r.recognize_google(audio)
                print("Recognition....")
                problem = r.recognize_google(audio, language='en-in')
                print(f"sir, you said:{problem}\n")
                return problem
            return'None'
            query=query.lower()
            return query
        
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
                
    

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    assistant = pyttsx3.init()

    # Define the wake-up phrase.
    wake_up_phrase = "wake up"

    with sr.Microphone() as source:
        print("...")
        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=None)
                recognizer.energy_threshold=300
                recognizer.dynamic_energy_threshold=True
                recognizer.pause_threshold=0.8
                recognizer.operation_timeout=None
                user_input = recognizer.recognize_google(audio, language='en-in')
                user_input=user_input.lower()

                if wake_up_phrase in user_input:
                    print("kevin: Hello! How can I assist you?")
                    assistant.say("yes sir")
                    assistant.runAndWait()
                    while True:
                        query = take_command().lower()
                        try:
                            if"search" in query:
                                try:
                                    print("searching sir...")
                                    query = query.replace("search", '')
                                    search_on_google(query)
                                    info = kit.info("query")
                                    print(info)
                                    speak(info)
                                except:
                                    speak(f"sorry sir no such result is available for {query}") 
                                    
                            elif "kevin" in query:
                                speak("yes sir!")
                                print("yes sir!")
                                    
                            elif "play songs" in query or"play" in query or "play videos" in query or "search on youtube" in query or "youtube" in query:
                                       try:
                                           query = query.replace("search", '') 
                                           query = query.replace("on", '')
                                           query = query.replace("in", '')
                                           query = query.replace("youtube", '')
                                           query = query.replace("play", '')
                                           yt= play_on_youtube(query)
                                           print("enjoy, sir!")
                                           speak("enjoy, sir!")
                                       except:
                                           speak(f"sorry sir no such result is available for {query}")
                                        
                            elif 'wikipedia' in query:
                                try:
                                    speak('searching in wikipedia sir...')
                                    query = query.replace("wikipedia", '')
                                    query = query.replace("in", '')
                                    results = search_on_wikipedia(query)
                                    speak("According to wikipedia")
                                    print(results)
                                    speak(results)
                                except:
                                    speak('sorry sir can not understand, please speak again')
                                    
                            elif "send message on whatsapp" in query or "send a message on whatsapp" in query or "send whatsapp message" in query:
                                try:
                                    speak("sir please tell me the number")
                                    number = take_command()
                                    speak("sir tell me the message")
                                    message = take_command()
                                    send_whatsapp_message(number, message)
                                    speak(f"done sir, I have send the message to {number}")
                                except:
                                    speak(f"done sir, I have not send the message to {number}")
                                    
                            elif "send email" in query:
                                email_address = "your_email_id"
                                app_password = "hnqr wnly akkv niut"
                                speak("sir! tell me the recipient email address before at the rate gamil dot com")
                                add = take_command()
                                recipient_email = f"{add}@gmail.com"
                                message = MIMEMultipart()
                                message["From"] = email_address
                                message["To"] = recipient_email
                                speak("sir,tell the messege")
                                send_mess= take_command()
                                message["Subject"] = send_mess
                                body= "any watermark that you want to add"
                                message.attach(MIMEText(body, "plain"))
                                try:
                                    server = smtplib.SMTP("smtp.gmail.com", 587)
                                    server.starttls()
                                    server.login(email_address, app_password)
                                    server.sendmail(email_address, recipient_email, message.as_string())
                                    print("Email sent successfully!")
                                except Exception as e:
                                    print("An error occurred:", str(e))
                                finally:
                                    # Close the SMTP server
                                    server.quit()
                                    
                            elif "latest news" in query:
                                get_latest_news()
                                    
                            elif "find my ip address" in query or "find ip address" in query or "ip address" in query:
                                ip_Address = find_ip_add()
                                print(ip_Address)
                                speak(ip_Address)
                                    
                            elif "where i am" in query or " tell me where i am" in query or "where am i" in query or "tell me where am i" in query or "tell my exact location" in query or "tell my location" in query or "my excact location" in query or "locate me" in query:
                                speak("wait sir, let me check!")
                                try:
                                    ipAdd = requests.get('http://api.ipify.org/').text
                                    print(ipAdd)
                                    url = 'http://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                                    geo_requests = requests.get(url)
                                    geo_data = geo_requests.json()
                                    city = geo_data['city']
                                    state  = geo_data['state']
                                    country = geo_data['country']
                                    speak(f"sir i am not sure, but i think we are in {city} city of {state} state of {country} country")
                                except Exception as e:
                                    print(e)
                                    speak("sorry sir, Due to network issue i am not able to find where we are")
                                    pass
                                    
                            elif "send message on whatsapp group" in query:
                                speak("sir tell me the group name")
                                group = take_command()
                                if group == 'group_name':
                                    speak("sir tell me the message")
                                    msg = take_command()
                                    kit.sendwhatmsg_to_group_instantly(group_id="any_group", message=msg, tab_close=2)
                                    speak(f"done sir, I have send the message to {group}")

                                elif group=='group_name':
                                    speak("sir tell me the message")
                                    msg = take_command()
                                    kit.sendwhatmsg_to_group_instantly(group_id="any_group", message=msg, tab_close=2)
                                    speak(f"done sir, I have send the message to {group}")
                                  
                            elif "good morning" in query or "good evening" in query or "good night" in query or "good afternoon" in query:
                                speak("ooooh! yes  welcome back sir")

                            elif "thank you" in query:
                                speak("no sir it's my pleasure")

                            elif "temperature" in query:
                                try:
                                    query=query.replace("what",'')
                                    query=query.replace("is",'')
                                    query=query.replace("the",'')
                                    query=query.replace("tell",'')
                                    query=query.replace("me",'')
                                    temperature = find_temperature(query)
                                    print(temperature)
                                    speak(f"sir the {query} is {temperature}")
                                except:
                                    speak("sorry sir due to network issue can not find th temprature")

                            elif "can I change your name?" in query:
                                try:
                                    speak("I'm sorry. I can't change my name. I'm trying my best, but I still have a lot to learn. please bare with me")
                                except:
                                        speak('sorry sir can not understand, please speak again')

                            elif "how many voices you have" in query or "types of voice" in query:
                                print("sir I have five types of voices 1) kevin 42 voice, 2) kevin 32 voice, 3) kevin 22 voice, 4) kevin 12 voice, 5) kevin 52 voice")
                                speak("sir I have five types of voices, first is, kevin 42, second is, kevin 32, third is, kevin 22, fourth is, kevin 12, and fifth is, kevin 52 voice")
                    
                            elif "what's the time" in query or "time" in query or "what about the time" in query or "tell the correct timing" in query or "tell me time" in query or "tell me about the time" in query:
                                try:
                                    time = datetime.datetime.now().strftime("%H:%M:%S")
                                    speak(f"sir the time is...{time}")
                                except:
                                        speak('sorry sir can not understand, please speak again')
                         
                            elif "hello" in query or "hey" in query:
                                try:
                                     speak("hello sir, how are you")
                                except:
                                        speak('sorry sir can not understand, please speak again')
                         
                            elif "goodbye" in query or "bye" in query or "off" in query or "of" in query or "by" in query or "sleep" in query or "exit" in query:
                                try:
                                    speak("Enter in rest mode")
                                    sleep(2)
                                except:
                                    speak('sorry sir can not understand, please speak again')
                                break
                        
                            elif "i am fine" in query or "i am fine" in query or "fine" in query:
                                try:
                                    speak("that's great sir")
                                except:
                                        speak('sorry sir can not understand, please speak again')

                            elif "how are you kevin" in query or "how are you" in query or "kevin how are you" in query or "what's about you" in query:
                                try:
                                    speak("Today has been great, I've been learning about a lot of different things")
                                except:
                                        speak('sorry sir can not understand, please speak again')
                        
                            elif "can you hear me" in query or "will you able to hear me" in query:
                                try:
                                    speak("yes sir I am able to hear you")
                                except:
                                    speak('sorry sir can not understand, please speak again')
                    
                            elif "are you mad" in query:
                                speak("Impossible my friend: you make my code quiver with joy , but I'm curious: what did I do to make you ask that?")
                    
                            elif "you are so funny" in query:
                                speak("you think so? I guess I do like to clown around")
                    
                            elif "can you laugh" in query:
                                speak("yes I can")
                    
                            elif "say meow" in query:
                                speak("sure, I can meow  Meow, meow, meow, meow, meow, meow, meow, meow, meow, meow, meow, meow, meow, meow, meow, meow")
                    
                            elif "what made you sad" in query or "tell me what makes you cry" in query or "when will you cry" in query:
                                speak("I get upset when we disconnect")
                    
                            elif "are you sure" in query:
                                speak("yes, sir I am sure.")
                                
                            elif "tell me a joke" in query or "tell a joke" in query or "can you tell me a joke" in query or "please tell a joke" in query or "please tell me joke" in query:
                                try:
                                    query = pyjokes.get_joke(language='en-in')
                                    print(query)
                                    speak(query)
                                except:
                                        speak('sorry sir can not understand, please speak again')
                         
                            elif "i am feel bored" in query or "i am bored" in query or "bored" in query:
                                try:              
                                    print("I am here to do cool tasks for you they are kind of like tricks: let me show you, do you want me to help you pick something or should I just suprise you?")
                                    speak("I am here to do cool tasks for you they are kind of like tricks: let me show you do you want me to help you pick something or should I just suprise you?")
                                except:              
                                    speak('sorry sir can not understand, please speak again')
                                
                            elif "are you single" in query or " are you single or not" in query or "will you merry me" in query:
                                try:              
                                    speak("I am in a relationship with wifi")
                                except:              
                                    speak('sorry sir can not understand, please speak again')
                                
                            elif "lock my laptop" in query or "lock" in query:
                                ctypes.windll.user32.LockWorkStation()
                                break
             
                            elif "take screenshot" in query or "screenshot" in query:
                                speak("sir, please give a name to screenshot")
                                name = take_command().lower()
                                speak("sir, please hold the screen for 1 second")
                                sleep(3)
                                img = pyautogui.screenshot()
                                img.save(f"{name}.png")
                                speak(f"I am done sir, screenshot is saved with {name} as name")
                                break

                            elif "thankyou" in query:
                                speak("It's my pleasure sir.")
                    
                            elif "tell me battery percentage" in query or "battery percentage" in query or "how much battery we have" in query or "battery level" in query:
                                battery = psutil.sensors_battery()
                                speak(f"Battery percentage is {battery.percent}")
                                if (battery.percent >= 80):
                                    speak("their is a optimum battery level to perform all the remaning tasks")
                                    sleep(1)
                                elif(battery.percent < 80 and battery.percent >= 40):
                                    speak("sufficient battery level to perform all the remaning tasks ")
                                    sleep(1)
                                else:
                                    speak("please connect your laptop to a charger quickely, if you can't then I will dead soon!")
                                    sleep(1)

                            elif "do some calculations" in query or "calculate" in query or "can you calculate" in query:
                                try:
                                    speak("sir! tell me what do you want to calculate")
                                    my_string = take_command()
                                    print(my_string)
                                    def get_operator_fn(op):
                                        return {
                                                '+' : operator.add,
                                                '-' : operator.sub,
                                                '*' : operator.mul,
                                                'divide' : operator.__truediv__,
                                                 }[op]
                                    def eval_binary_expr(op1, oper, op2):
                                        op1,op2 = int(op1) ,int(op2)
                                        return get_operator_fn(oper)(op1, op2)
                                    speak("your result is:")
                                    speak(eval_binary_expr(*(my_string.split())))
                                except:
                                        speak("can't listen properly. can you, please speak again")

                            elif "tell network speed" in query or "network speed" in query or "internet speed" in query or "tell me the network speed" in query or "tell me the network speed" in query or "tell me the internet speed" in query or "what is the network speed" in query:
                                os.system('cmd /k "speedtest')
                                continue

                            elif "kevin trace number" in query or "track the phone number" in query  or "track" in query or "track my phone" in query or "track phone" in query or "trace my phone" in query or "trace" in query or "trace the number" in query:
                                number = take_command()
                                pepnumber = phonenumbers.parse(f"+91{number}")
                                location = geocoder.description_for_number(pepnumber, "en")
                                print(location)
                                speak("sir the number is from the country")
                                speak(location)

                                time = timezone.time_zones_for_number(pepnumber)
                                print(time)
                                speak("the time zone of this number is ")
                                speak(time)

                                service_provider = phonenumbers.parse(number)
                                print(carrier.name_for_number(service_provider, "en"))
                                speak("and the service provider of this phone number is")
                                speak(carrier.name_for_number(service_provider, "en"))
                                
                            elif "change voice" in query or "change the voice" in query or "change your voice" in query:
                                try :
                                    print("sir I have five types of voices 1) kevin 42 voice, 2) kevin 32 voice, 3) kevin 22 voice, 4) kevin 12 voice, 5) kevin 52 voice")
                                    speak("sir I have five types of voices, first is, kevin 42, second is, kevin 32, third is, kevin 22, fourth is, kevin 12, and fifth is, kevin 52 voice")
                                    speak("please tell me which voice did you choose")
                                    choice = take_command()
                                    if choice == "Kevin 42" or choice == "Kevin 42 voice":
                                        engine.setProperty('voice',voices[0].id)
                                        speak("hello sir this voice is of kevin 42")
                                    elif choice == "Kevin 52" or choice == "Kevin 52 voice":
                                        engine.setProperty('voice',voices[1].id)
                                        speak("hello sir this voice is of kevin 52")
                                    elif choice == "kevin 12" or choice == "Kevin 12 voice": 
                                        engine.setProperty('voice',voices[2].id)
                                        speak("hello sir this voice is of kevin 12")
                                    elif choice == "Kevin 22" or choice == "Kevin 22 voice":
                                        engine.setProperty('voice',voices[3].id)
                                        speak("hello sir this voice is of kevin 22")
                                    elif choice == "Kevin 32" or choice == "Kevin 32 voice":
                                        engine.setProperty('voice',voices[6].id)
                                        speak("hello sir this voice is of kevin 32")
                                    else:
                                        speak("sorry sir you give wrong name please speak again")
                                except:
                                    speak("sorry sir due to no network connection you can't change the voice")

                                
                            elif "cancel shutdown" in query or "stop shutdown" in query or "wait" in query:
                                kit.cancel_shutdown()
                    
                            else:
                                try:
                                    info = kit.info(query)
                                    print(info)
                                except:           
                                    speak("sorry sir can not match any query, please speak again")
                                
                        except sr.WaitTimeoutError:
                            pass
                        except sr.UnknownValueError:
                            pass
                        except sr.RequestError as e:
                            print(f"kevin: Error with the speech recognition service; {e}")
                            speak("Error with the speech recognition service")
                            speak("or check your network connection")
                        except sr.URLError as e:
                            print("sorry sir their is an URL error")
                            speak("sorry sir their is an URL error")
                        except sr.WaitTimeoutError as e:
                            print("sir your time limit is exceeded, please try again")
                            speak("sir your time limit is exceeded, please try again and speak fast and louder")
                            
                elif "goodbye" in user_input or "goodbye" in user_input or "bye" in user_input or "off" in user_input or "by" in user_input or "sleep" in user_input or "sleep" in user_input or "exit" in user_input:
                        try:
                            break
                        except:
                            speak('sorry sir can not understand, please speak again')
        
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Assistant: Error with the speech recognition service; {e}")
                speak("Error with the speech recognition service")
                speak("or check your network connection")
            except sr.URLError as e:
                print("sorry sir their is an URL error")
                speak("sorry sir their is an URL error")
            except sr.WaitTimeoutError as e:
                print("sir your time limit is exceeded, please try again")
                speak("sir your time limit is exceeded, please try again and speak fast and louder")