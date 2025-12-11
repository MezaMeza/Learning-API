from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
import shutil

base_path = os.path.dirname(os.path.abspath(__file__))
project_driver_dir = os.path.join(os.getcwd(), "driver")
URL_BASE = "https://learningenglish.tecnacional.edu.ni/api/app/v1/courses"


def obtener_driver_local():
    print("Verificando y descargando ChromeDriver...")

    # 2. Usamos el Manager para descargar la versión correcta a su caché temporal
    ruta_descarga_manager = ChromeDriverManager().install()

    # 3. Definimos la ruta destino exacta (ej: .../driver/chromedriver.exe)
    nombre_archivo = os.path.basename(ruta_descarga_manager)  # obtiene 'chromedriver.exe'
    ruta_destino_final = os.path.join(project_driver_dir, nombre_archivo)

    # 4. Copiamos el archivo descargado a TU carpeta 'driver'
    # Esto asegura que siempre tengas el driver en tu ruta específica
    if ruta_descarga_manager != ruta_destino_final:
        shutil.copy(ruta_descarga_manager, ruta_destino_final)
        print(f"Driver copiado exitosamente a: {ruta_destino_final}")

    return ruta_destino_final


# --- EJECUCIÓN ---

# Obtener la ruta de tu driver local actualizado
# ruta_driver = obtener_driver_local()

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


  # user= "rosa.salmeron1@tecnacional.edu.ni"
  # user= "macdiel.chavez@tecnacional.edu.ni"
  # user= "martha.calero2@tecnacional.edu.ni"
  # user= "jozem.zeledon@tecnacional.edu.ni"
  # user= "cristiam.avendano1@tecnacional.edu.ni"
  user= "jonathan.montoya1@tecnacional.edu.ni"

  js_script_1 = f"""
      document.querySelector('#mail').value = "{user}"
      document.querySelector('#password').value = "{user}"
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
  # Learning_A = f"{base_path}/A1"
  Learning_A = f"{base_path}/A2"
  print(os.listdir(Learning_A))

  # users = []


  for unit in os.listdir(Learning_A):
    Lessons = os.listdir(f"{Learning_A}/{unit}")
    print(Lessons)
    for lesson in Lessons:
      print(f"Enviando: {lesson}")
      with open(f"{Learning_A}/{unit}/{lesson}", "r", encoding="utf-8") as file:
        payload = json.load(file)
        # print(f"Contenido del archivo JSON: {data}")
        response = requests.request("POST", URL_BASE, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())


  ##** Para enviar una unidad específica, descomentar este bloque y comentar el bloque superior
  # unit = "Unit 10"
  # Lessons = os.listdir(f"{Learning_A2}/{unit}")
  # for lesson in Lessons:
  #     print(f"Enviando: {lesson}")
  #     with open(f"{Learning_A2}/{unit}/{lesson}", "r", encoding="utf-8") as file:
  #         payload = json.load(file)
  #         # print(f"Contenido del archivo JSON: {data}")
  #         response = requests.request("POST", URL_BASE, json=payload, headers=headers)
  #         response.raise_for_status()  # Raise an error for bad responses
  #         print("Response Status Code:", response.status_code)
  #         print("Response JSON:", response.json())


  # for lesson in Lessons:
  #     print(f"Enviando: {lesson}")
  #     with open(f"{Learning_A2}/{unit}/{lesson}", "r", encoding="utf-8") as file:
  #         payload = json.load(file)
  #         # print(f"Contenido del archivo JSON: {data}")
  #         response = requests.request("POST", URL_BASE, json=payload, headers=headers)
  #         response.raise_for_status()  # Raise an error for bad responses
  #         print("Response Status Code:", response.status_code)
  #         print("Response JSON:", response.json())

  driver.quit()
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

