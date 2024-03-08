import requests
import wikipedia
import pywhatkit as kit
from time import sleep
from bs4 import BeautifulSoup
    
#def send_whatsapp_group_message(group, message):
#    kit.sendwhatmsg_to_group_instantly(group_id= group, message, tab_close=2)
    
def find_temperature(query):
    url = f"https://www.google.com/search?q={query}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    data.find("div",class_="BNeawe").text
    
def switch_the_window():
    kit.keyDown("alt")
    kit.press("tab")
    sleep(1)
    kit.keyUp("alt")
    kit.keyUp("tab")
    
def open_run():
    kit.keyDown("win")
    kit.press("r")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("r")

def window_button():
    kit.keyDown("win")
    kit.keyUp("win")
    
def clipboard():
    kit.keyDown("win")
    kit.press("v")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("c")
    
def copy_text():
    kit.keyDown("ctrl")
    kit.press("c")
    sleep(1)
    kit.keyUp("ctrl")
    kit.keyUp("c")
    
def paste_text():
    kit.keyDown("ctrl")
    kit.press("v")
    sleep(1)
    kit.keyUp("ctrl")
    kit.keyUp("v")
    
def notification_bar():
    kit.keyDown("win")
    kit.press("n")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("n")
    
def select_all_text():
    kit.keyDown("ctrl")
    kit.press("a")
    sleep(1)
    kit.keyUp("ctrl")
    kit.keyUp("a")
    
def save_file():
    kit.keyDown("ctrl")
    kit.press("s")
    sleep(1)
    kit.keyUp("ctrl")
    kit.keyUp("s")
    
def open_lock():
    kit.keyDown("L")
    kit.keyDown("o")
    kit.keyDown("k")
    kit.keyDown("e")
    kit.keyDown("s")
    kit.keyDown("h")
    kit.keyDown("shift")
    kit.press("@")
    sleep(1)
    kit.keyUp("L")
    kit.keyUp("o")
    kit.keyUp("k")
    kit.keyUp("e")
    kit.keyUp("s")
    kit.keyUp("h")
    kit.keyUp("shift")
    kit.keyUp("@")
    
def show_important_functions():
    kit.keyDown("win")
    kit.press("x")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("x")
    
def open_chat():
    kit.keyDown("win")
    kit.press("c")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("c")
    
def minimise():
    kit.keyDown("win")
    kit.press("z")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("z")
    
def home_screen():
    kit.keyDown("win")
    kit.press("m")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("m")

def widget():
    kit.keyDown("win")
    kit.press("w")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("w")
    
def file_manager():
    kit.keyDown("win")
    kit.press("e")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("e")
    
def accessibility():
    kit.keyDown("win")
    kit.press("u")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("u")
    
def project():
    kit.keyDown("win")
    kit.press("p")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("p")
    
def control_panel():
    kit.keyDown("win")
    kit.press("a")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("a")
    
def controller_bar():
    kit.keyDown("win")
    kit.press("g")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("g")
    
def voice_typing():
    kit.keyDown("win")
    kit.press("h")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("h")
    
def screen_cast():
    kit.keyDown("win")
    kit.press("k")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("k")
    
def switch_language():
    kit.keyDown("win")
    kit.press("b")
    sleep(1)
    kit.keyUp("win")
    kit.keyUp("b")
    
def extra_space():
    kit.keyDown("ctrl")
    kit.press("i")
    sleep(1)
    kit.keyUp("ctrl")
    kit.keyUp("i")
    
def cut_the_text():
    kit.keyDown("ctrl")
    kit.press("x")
    sleep(1)
    kit.keyUp("ctrl")
    kit.keyUp("x")