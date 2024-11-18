from dict import calc_base


def calc():
    """Калькулятор."""
    while True:
        start = input(calc_base["calc_welc"])

        match start:
            case "1":
                print("Загрузка...")
                while True:
                    first = int(input("Калькулятор успешно загрузился, введите первое число: "))
                    second = int(input("Отлично, теперь введите второе число: "))
                    choice = input(calc_base["choice_base"]["choice_one"])
                    match choice:
                        case "1":
                            addition = first + second
                            print("Ответ: ", addition)
                            continue
                        case "2":
                            addition = first - second
                            print("Ответ: ", addition)
                            continue
                        case "3":
                            addition = first * second
                            print("Ответ: ", addition)
                            continue
                        case "4":
                            addition = first / second
                            print("Ответ: ", addition)
                            if first == 0:
                                print("Делить на ноль нельзя!")
                                continue
                            continue

            case "2":
                print("Выход из программы.")
                exit()
            case _:
                print("Я не понял что вы ввели. Поэтому программа будет перезапущена")
                continue