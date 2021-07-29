import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time_util import sleep
import sys
from selenium.common.exceptions import NoSuchElementException

#Credenciales
email = str(sys.argv[1]) #input(print('Ingresar email: '))
password = str(sys.argv[2]) #input(print('Ingresar contraseña: '))

#URL del psot
post_url =  str(sys.argv[3])#input(print('Ingresar url del post: '))

#Crear nueva sesion de Chrome
chromedriver_location = "./assets/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.maximize_window()

# log in
driver.get("https://www.facebook.com")
search_field = driver.find_element_by_id("email")
search_field.send_keys(email)
search_field = driver.find_element_by_id("pass")
search_field.send_keys(password)
search_field.submit()

print("Se inicio sesion como " + email)

#Navegar al url del post
driver.get(post_url)
engagement_div = driver.find_element_by_css_selector("a[href*='/ufi/reaction']")
driver.execute_script("arguments[0].click();", engagement_div)

engagement_all = driver.find_element_by_css_selector("a[tabindex*='-1']")
driver.execute_script("arguments[0].click();", engagement_div)

print("Cargando todos los usuarios")

while True:
    try:
        viewMoreButton = driver.find_element_by_css_selector("a[href*='/ufi/reaction/profile/browser/fetch']")
        driver.execute_script("arguments[0].click();", viewMoreButton)
        sleep(2)
    except NoSuchElementException:
        break

#Invitacion a usuarios
print("Invitando a los usuarios")
users = driver.find_elements_by_css_selector("a[ajaxify*='/pages/post_like_invite/send/']")
invitedUsers = 0

for i in users:
    user = driver.find_element_by_css_selector("a[ajaxify*='/pages/post_like_invite/send/']")
    driver.execute_script("arguments[0].click();", user)
    invitedUsers = invitedUsers + 1
    sleep(1)

print('Usuarios invitados: ' + str(invitedUsers))

#Cerrar la ventana del navegador
driver.quit()