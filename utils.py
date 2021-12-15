import time

import smtplib, ssl

import pyautogui
from pyautogui import press, typewrite, hotkey, click
import pyperclip

def send_email(information):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com" #"outlook.office365.com"
    sender_email = "realvcla@gmail.com"
    receiver_email_1 = "yizhou_zhao@berkeley.edu"
    receiver_email_2 = "va0817@g.ucla.edu"
    password = "97654321abc" #input("Type your password and press enter:")
    message = 'Subject: {}\n\n{}'.format("!!!GRAPHIC CARD NOTIFICATION!!!", information)

    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email_1, message)
    server.quit()

def get_selling_info(config):
    # resolve config
    chrome_position = config["chrome_position"]
    search_bar_position = config["search_bar_position"]
    sold_out_start = config["sold_out_start"]
    sold_out_end = config["sold_out_end"]
    close_position = config["close_position"]
    url = str(config["url"].encode().decode())
    
    pyperclip.copy(url)

    # open chrome
    click(chrome_position)    
    time.sleep(3) 

    # go to url
    click(search_bar_position)
    
    pyautogui.hotkey('ctrl', 'v')
    #pyautogui.typewrite(url)
    press('Enter')
    time.sleep(3)

    # get selling information
    click(sold_out_start)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(sold_out_end[0], sold_out_end[1], 1)
    pyautogui.mouseUp(button='left')
    pyautogui.hotkey('ctrl', 'c') 
    time.sleep(1) 

    # close chrome
    click(close_position)

    # get selling information
    return pyperclip.paste()