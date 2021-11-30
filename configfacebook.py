from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from LoginFace import email, passwd
pyautogui.alert(text='PRONTO PARA COMEÇAR', title='BUSCADOR DE ESTÁGIO', button='OK')

PFacebook = webdriver.Chrome()

PFacebook.get('https://www.facebook.com/')


def LoginFacebook():
    PFacebook.find_element_by_id('email').send_keys(email)
    time.sleep(2)
    PFacebook.find_element_by_id('pass').send_keys(passwd)
    time.sleep(2)
    PFacebook.find_element_by_name('login').click()


LoginFacebook()



