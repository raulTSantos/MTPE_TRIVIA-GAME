import random
import time
import os

#=================================================================================
# LISTAS DE PREGUNTAS, OPCIONES , RESPUESTAS (cuerpo humano)
#El primer elemento de la lista de preguntas coincide con el primer elemento de la lista de opciones y de la lista de respuestas correctas.
human_body_questions = [
    "¿Cómo se llaman las células nerviosas?",
    "¿Cómo se llama la ciencia que estudia la sangre?",
    "¿Cuántos huesos tiene un ser humano adulto?",
    "¿Cuál es el único órgano que puede regenerarse?"
]
human_body_options = [
    ["Leucocitos", "Fibroblastos", "Neuronas", "Epiteleales"],
    ["Hemología", "Cardiología", "Psicología", "Hematología"],
    ["208", "207", "206", "205"],
    ["El estómago", "El hígado", "Los intestinos", "El pancreas"]
]

human_body_answer = ["Neuronas", "Hematología", "206", "El hígado"]
#=================================================================================
# LISTAS DE PREGUNTAS, OPCIONES , RESPUESTAS (historia del Peru)
history_questions = [
    "¿Quién fue el primer Inca?", "¿Qué Inca mandó construir Machu Picchu?",
    "¿Quién fue el primer Virrey del Perú?",
    "¿Cuándo y quién proclamó la Independencia del Perú?"
]
history_options = [["Pachacútec", "Manco Cápac", "Wiracocha", "Sinchi Roca"],
                   ["Atahualpa", "Manco Inca", "Pachacútec", "Huascar"],
                   [
                       "José de la Serna de Hinojosa", "Carlos V",
                       "Blasco Núñez de Vela", "Antonio de Mendoza"
                   ],
                   [
                       "18/07/1821 Don José de San Martin",
                       "15/08/1824 Simón Bolivar",
                       "28/07/1821 Don José de San Martin",
                       "08/07/1821 Simón Bolivar"
                   ]]
history_answer = [
    "Manco Cápac", "Pachacútec", "Blasco Núñez de Vela",
    "28/07/1821 Don José de San Martin"
]
#=================================================================================
# LISTAS DE PREGUNTAS, OPCIONES , RESPUESTAS (Deporte)

deports_questions = [
    "¿Qué pieza de ajedrez puede hacer un movimiento en forma de L?",
    "¿Cuántos jugadores tiene un equipo de voleibol?",
    "¿Cuánto dura un partido de fútbol?", ""
]
deports_options = [["Caballo", "Alfil", "Reina", "Torre"],
                   ["5", "6", "7", "8"],
                   ["100 min", "95 min", "90 min", "89 min"],
                   [
                       "Azul, rojo, amarillo, verde y negro",
                       "Azul, rojo, maramja, verde y violeta",
                       "Azul, rojo, amarillo, verde y violeta",
                       "Azul, rojo, amarillo, verde y violeta"
                   ]]

deports_answer = [
    "Caballo", "6", "90 min", "Azul, rojo, amarillo, verde y negro"
]

#====================================================

#Puntaje inicial
score = 0
#Cantidad de vidas inicial
hp = 2

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


#Metodo que permite ordenar de forma aleatoria los elementos de una lista anidada y retornar una nueva lista
def random_option(options_list, index):
    random_list = []
    random.shuffle(options_list[index])
    random_list = options_list
    return random_list


#Metodo para mostrar pregunta y las respuestas en consola
def show_question(index, quiz, options):

    print(quiz[index])
    print("A.", options[index][0])
    print("B.", options[index][1])
    print("C.", options[index][2])
    print("D.", options[index][3])
    print("============================================")


#Captura de la respusta ingresada por el usuario condicionada por una lista valida
#Retorna el indice de la lista valida ["A", "B", "C", "D"]
def catch_question_alternative():
    data_input = input(YELLOW + "Ingrese (A, B, C, o D):  " +
                       RESET).upper().strip()
    valid_data = ["A", "B", "C", "D"]
    while data_input not in valid_data:
        print(RED + "La respuesta ingresada no es valida " + RESET)
        data_input = input(YELLOW + "Ingrese (A, B, C, o D):  " +
                           RESET).upper().strip()

    return valid_data.index(data_input)


#Verificar si la respuesta ingresada coincide con la respuesta correcta de la pregutna
#Mientras la cantidad de intentos sea mayor a 0 recibira puntaje , de lo contrario no.
#Recibe argumentos de tipo lista que son: pregunta ,opciones de pregunta ,y respuesta de la prengunta.el index es comun para todos
def check_answer(index, options, answer, questions):

    #altera variables globales
    global score, hp
    while hp > 0:

        if (answer[index] == options[index][catch_question_alternative()]):

            if hp == 2:
                score += 500

            elif hp == 1:
                score += 350
            print("MUY BIEN, ES CORRECTO!")
            time.sleep(2)
            clear_console()
            break
        else:
            hp -= 1  #disminuir la vidas disponibles para poder escapar del bucle

            print(f"INCORRECTO!, Te quedan {hp} vidas para esta pregunta :-(")
            time.sleep(2)
            clear_console()
            score_head()
            show_question(index, questions, options)

    else:
        clear_console()
        print(BLUE + "LO SENTIMOS, LA RESPUESTA ERA!: " + answer[index] +
              RESET)
        print(BLUE + "NO ACUMULASTE PUNTAJE! ..." + RESET)
        time.sleep(5)
        clear_console()
    #Reseteo de numero de intentos
    hp = 2


def game():

    clear_console()
    show_categories_head()
    category = selected_category()
    clear_console()
    if category == "1":
        for x in range(len(human_body_questions)):
            options = random_option(human_body_options, x)
            score_head()
            show_question(x, human_body_questions, options)
            check_answer(x, options, human_body_answer, human_body_questions)

    if category == "2":
        for x in range(len(history_questions)):
            options = random_option(history_options, x)
            score_head()
            show_question(x, history_questions, options)
            check_answer(x, options, history_answer, history_questions)
    if category == "3":
        for x in range(len(deports_questions)):
            options = random_option(deports_options, x)
            score_head()
            show_question(x, deports_questions, options)
            check_answer(x, options, deports_answer, deports_questions)


def score_head():
    score_format = "{:<13}".format(str(score))
    print(GREEN + "********************************************")
    print(f"* VIDAS: {hp}   | PUNTAJE TOTAL: {score_format}*")
    print("********************************************" + RESET)


def show_categories_head():
    print(GREEN + "*********CATEGORIAS DISPONIBLES PARA JUGAR*********")
    print("---------------------------------------------------")
    print("1.Cuerpo Humano | 2.Historia del Peru | 3. Deportes", end="")
    print("\n---------------------------------------------------" + RESET)


def selected_category():
    selected_category = input(YELLOW +
                              "Ingrese numero de categoria a jugar: " +
                              RESET).upper().strip()
    while selected_category not in ["1", "2", "3"]:
        print(RED + "La respuesta ingresada no es valida " + RESET)
        selected_category = input(YELLOW +
                                  "Ingrese numero de categoria a jugar: " +
                                  RESET).upper().strip()

    return selected_category


def play_again():
    response = input("¿Quieres jugar de nuevo? (si o no): ")
    response = response.upper()

    if response == "SI":
        return True
    else:
        return False


def play_game():
    print(CYAN + "***** BIENVENIDO A MI JUEGO DE TRIVIA *****")
    name = input("Por favor ingrese un nombre :").upper()
    print(
        GREEN +
        f"Estimad@ {name},  este es un juego sencillo de preguntas,\nsolo debes ingresar las alternativas correspendientes y presionar Enter para confirmar tu respuesta.\nSUERTE ☘☘☘ Y A DIVERTIRSE 😊 !"
        + RESET)
    time.sleep(5)
    game()
    while play_again():

        print(CYAN + f"Bienvenido de vuelta {name} ..." + RESET)
        print(CYAN + "Ya conoces las reglas del juego" + RESET)
        print(GREEN + "SUERTE ☘☘☘ Y A DIVERTIRSE 😊 !" + RESET)
        time.sleep(5)
        game()
    print(f"Gracias por participar {name} , te eperamos pronto!!")


play_game()
