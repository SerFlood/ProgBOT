# ╔═══╗╔═══╗╔══╗╔═══╗╔══╗─╔══╗╔════╗
# ║╔═╗║║╔═╗║║╔╗║║╔══╝║╔╗║─║╔╗║╚═╗╔═╝
# ║╚═╝║║╚═╝║║║║║║║╔═╗║╚╝╚╗║║║║──║║──
# ║╔══╝║╔╗╔╝║║║║║║╚╗║║╔═╗║║║║║──║║──
# ║║───║║║║─║╚╝║║╚═╝║║╚═╝║║╚╝║──║║──
# ╚╝───╚╝╚╝─╚══╝╚═══╝╚═══╝╚══╝──╚╝──
import random

from dict import knb_base


def knb():
    """Камень Ножницы Бумага."""
    while True:
        start = input(knb_base["knb_welc"])

        match start:
            case "1":
                print("Загрузка...")
                print("ЗАГРУЗКА ЗАВЕРЕШЕНА!!! НАЧИНАЕЕЕМММ!!!")
                print("""   3...\n   2...\n   1...""")
                print("Если захочешь закончить игру, введи - Закончить.")
                print("Если захочешь узнать счёт введи - Счет.")
                user_ball = 0
                progbot_ball = 0

                while True:
                    user = input("Камень, Ножницы или Бумага?: ").title()
                    list_play = ["Камень", "Ножницы", "Бумага"]
                    if user in list_play:
                        progbot = random.choice(list_play)
                        print(progbot)

                        if progbot == "Камень" and user == "Ножницы":
                            progbot_ball += 1
                            print("Я победил;)")
                        if progbot == "Камень" and user == "Бумага":
                            user_ball += 1
                            print("Ты победил;)")
                        if progbot == "Ножницы" and user == "Камень":
                            user_ball += 1
                            print("Ты победил;)")
                        if progbot == "Ножницы" and user == "Бумага":
                            progbot_ball += 1
                            print("Я победил;)")
                        if progbot == "Бумага" and user == "Ножницы'":
                            user_ball += 1
                            print("Ты победил;)")
                        if progbot == "Бумага" and user == "Камень":
                            progbot_ball += 1
                            print("Я победил;)")
                        if progbot == "Камень" and user == "Камень":
                            print("Ничья;)")
                        if progbot == "Бумага" and user == "Бумага":
                            print("Ничья;)")
                        if progbot == "Ножницы" and user == "Ножницы":
                            print("Ничья;)")

                    elif user == "Счет":
                        print(f"Ваши баллы - {user_ball}. Баллы ProgBOT - {progbot_ball}.")
                    elif user == "Закончить":
                        print(f"Ваши баллы - {user_ball}. Баллы ProgBOT - {progbot_ball}.")
                        print("Конец игры! Заходите ещё!")
                        break
                    else:
                        print("Вводите Камень, Ножницы или Бумага")

            case "2":
                print("Выход из программы.")
                exit()
            case _:
                print("Я не понял что вы ввели. Поэтому программа будет перезапущена")
                continue
            case _:
                print("Я не понял что вы ввели. Поэтому программа будет перезапущена")
                continue
