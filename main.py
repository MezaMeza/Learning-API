from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json

base_path = os.path.dirname(os.path.abspath(__file__))
project_driver_dir = os.path.join(os.getcwd(), "driver")
URL_BASE = "https://learningenglish.tecnacional.edu.ni/api/app/v1/courses"

def getCookies(cookies):
    cookie = []
    for item in cookies:
        title = item['name']
        value = item['value']
        cookie.append(f"{title}={value}")

    return '; '.join(cookie)

try:
  options = Options()
  driver = webdriver.Chrome(service=Service(f"{project_driver_dir}\chromedriver.exe"), options=options)

  print(project_driver_dir)
  # Abrir navegador
  driver.get("https://learningenglish.tecnacional.edu.ni/welcome/login")

  sleep(3)

  cooks_ = driver.get_cookies()
  cookie = getCookies(cooks_)

  js_script_1 = """
      document.querySelector('#mail').value = "reyna.franco@tecnacional.edu.ni"
      document.querySelector('#password').value = "reyna.franco@tecnacional.edu.ni"
      document.querySelector("button[type='submit']").click()
      """

  js_script_2 = """
      token_ = document.querySelector('#FBtoken').value
      return token_
      """
  driver.execute_script(js_script_1)
  sleep(3)
  token = driver.execute_script(js_script_2)
  print("Token obtenido:", token)

  headers = {
      "Host": "learningenglish.tecnacional.edu.ni",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
      "Accept": "application/json, text/plain, */*",
      "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
      "Accept-Encoding": "gzip, deflate, br",
      "Content-Type": "application/json;charset=utf-8",
      "Authorization": f"{token}",
      "cookie": cookie,
      "Origin": "https://learningenglish.tecnacional.edu.ni",
      "Referer": "https://learningenglish.tecnacional.edu.ni/exercises/task/578",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Priority": "u=0",
      "Connection": "keep-alive"
  }
  #! REEMPLAZAR A1 o A2 SEGUN CORRESPONDA
  Learning_A2 = f"{base_path}/A2"
  print(os.listdir(Learning_A2))
  for unit in os.listdir(Learning_A2):
    Lessons = os.listdir(f"{Learning_A2}/{unit}")
    print(Lessons)
    for lesson in Lessons:
      print(f"Enviando: {lesson}")
      with open(f"{Learning_A2}/{unit}/{lesson}", "r", encoding="utf-8") as file:
        payload = json.load(file)
        # print(f"Contenido del archivo JSON: {data}")
        response = requests.request("POST", URL_BASE, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())

  driver.quit()
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

