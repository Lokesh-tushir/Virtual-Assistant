import pywhatkit as kit


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message, tab_close=15)