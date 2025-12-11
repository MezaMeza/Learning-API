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
global questions, question_search, respuesta_encontrada

with open(f"{base_path}/mooc.json", "r", encoding="utf-8") as file:
    questions = json.load(file)
    print(len(questions))

# question_search = "Seleccione la respuesta correcta: ¿Qué tipo de abuso sufrían los pueblos originarios en el contexto del repartimiento?"
#
# questions_selection = """
#     questions = document.querySelectorAll('[id^="question"]')
#     questions.forEach(element => {
#     const qtextDiv = element.querySelector('.qtext');
#
#     if (qtextDiv) {
#         console.log(qtextDiv.textContent);
#     }
#     });
# """
#
# """
# question.forEach(element => {
#   const qtextDiv = element.querySelector('.qtext');
#   if (qtextDiv) {
#     console.log(qtextDiv.textContent);
#   }
# });
# """
#
# radio_buttons_selection = \
# """
# radioButtons = question.querySelectorAll('input[type="radio"]')
# radioButtons = question[0].querySelectorAll('input[type="radio"]')
# radioButtons.forEach(radio => {
#   const labelId = radio.getAttribute('aria-labelledby');
#   const labelDiv = document.getElementById(labelId);
#   if (labelDiv) { // <--- ¡Esta es la verificación clave!
#             // Extrae el texto y elimina el prefijo
#             const respuestaTexto = labelDiv.textContent.trim().substring(3).trim();
#
#             // Compara y selecciona el radio button correcto
#             if (respuestaTexto === "Se les obligaba a trabajar sin remuneración y a suministrar los materiales de construcción, herramientas.") {
#                 radio.checked = true;
#             }
#         }
#     });
# """
# """
#
# """
#
#
# for question in questions:
#     if question_search in question["pregunta"]:
#         respuesta_encontrada = question["respuesta"]
#         break
#
# if respuesta_encontrada:
#     print(f"Respuesta encontrada: {respuesta_encontrada}")
# else:
#     print("No se encontró la pregunta.")


