# ╔═══╗╔═══╗╔══╗╔═══╗╔══╗─╔══╗╔════╗
# ║╔═╗║║╔═╗║║╔╗║║╔══╝║╔╗║─║╔╗║╚═╗╔═╝
# ║╚═╝║║╚═╝║║║║║║║╔═╗║╚╝╚╗║║║║──║║──
# ║╔══╝║╔╗╔╝║║║║║║╚╗║║╔═╗║║║║║──║║──
# ║║───║║║║─║╚╝║║╚═╝║║╚═╝║║╚╝║──║║──
# ╚╝───╚╝╚╝─╚══╝╚═══╝╚═══╝╚══╝──╚╝──
import random
import os
import hashlib

from dict import *
from knb import knb
from calculator import calc


version_prog = "1.02"
print(f"Ver {version_prog}")


def load_users(filename):
    """Загружает пользователей из файла."""
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r', encoding='utf-8') as file:
        users = {}
        for line in file:
            nickname, password = line.strip().split(',')
            users[nickname] = password
    return users


def save_user(filename, nickname, password):
    """Сохраняет пользователя в файл."""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{nickname},{password}\n")


def get_random_greeting():
    """Возвращает случайное приветствие."""
    return random.choice(welc_word)


def register(users):
    """Регистрация нового пользователя."""
    print("Регистрация нового пользователя")
    nickname = input(reg_word["register"]["nickname"]).lower()

    if nickname in users:
        print(reg_word["register"]["error"])
        return False

    password = input(reg_word["register"]["password"])
    hash_p = hashlib.sha256(password.encode()).hexdigest()

    # Сохранение пользователя.
    save_user('users.txt', nickname, hash_p)

    # Приветствие.
    greeting = get_random_greeting()
    print(f"{greeting} {nickname}! Вы успешно зарегистрированы.")
    return True


def login(users):
    """Авторизация пользователя."""
    print("Авторизация")
    nickname = input(reg_word["login"]["nickname"]).lower()

    if nickname not in users:
        print(reg_word["login"]["error_nickname"])
        return False

    password = input(reg_word["login"]["password"])
    hash_p = hashlib.sha256(password.encode()).hexdigest()

    if users[nickname] == hash_p:
        greeting = get_random_greeting()
        print(f"{greeting} {nickname}! Вы успешно вошли в систему.")
        return True
    else:
        print(reg_word["login"]["error_password"])
        return False


def question():
    """Вопросы боту."""
    while True:
        quast = input(questions_base["quest_base"]["welc_quest"])

        match quast:
            case '1':
                quast_answer = input(questions_base["answer_base"]["message_one"])
                match quast_answer:
                    case '1':
                        quast_answer_two = input(questions_base["answer_base"]["message_two"])
                        if quast_answer_two == '1':
                            knb()
                            break
                        if quast_answer_two == '2':
                            calc()
                            break
                        if quast_answer_two == '3':
                            print("Выход из программы.")
                            break
                    case '2':
                        quast_answer_two = input(questions_base["answer_base"]["message_three"])
                        if quast_answer_two == '1':
                            print("Выход из программы.")
                            break
                    case '3':
                        print("Выход из программы.")
                        break
                    case _:
                        print("Неверный выбор. Пожалуйста, попробуйте снова.")
            case '2':
                quast_answer_two = input(questions_base["answer_base"]["message_two"])
                if quast_answer_two == '1':
                    knb()
                    break
                if quast_answer_two == '2':
                    calc()
                    break
                if quast_answer_two == '3':
                    print("Выход из программы.")
                    break
            case '3':
                print("Выход из программы.")
                break
            case _:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
                continue


def welcome():
    filename = 'users.txt'
    users = load_users(filename)

    while True:
        action = input(reg_word["welcome"])

        match action:
            case '1':
                register(users)
            case '2':
                if login(users):
                    break  # Выход из цикла после успешной авторизации
            case '3':
                print("Выход из программы.")
                break
            case _:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    welcome()
    question()
