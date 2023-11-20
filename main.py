def display_tasks_from_file():
    file = open("task-list.txt", 'r+', encoding='utf-8')
    lines = file.readlines()
    if len(lines) != 0:
        print("Усі завдання з файлу:")
        print("_____________________")
        for line in lines:
            print(line.strip())
    else:
        print("Файл порожній!")


def write_task_in_file(task):
    file = open("task-list.txt", 'r+', encoding='utf-8')
    lines = file.readlines()
    if len(lines) == 0 or not any(line.strip()[4:] == task for line in lines):
        lines.append(f"{len(lines) + 1} - {task}\n")
        file.seek(0)
        file.writelines(lines)
        print("Завдання було успішно додане!")
    else:
        print("Таке завдання вже існує в списку!")


def update_task_from_file(task, updated_task):
    file = open("task-list.txt", "r", encoding='utf-8')
    lines = file.readlines()
    file = open("task-list.txt", "w", encoding='utf-8')
    if len(task) != 0 and len(updated_task) != 0:
        for index, line in enumerate(lines, start=1):
            if line.strip()[4:] == task:
                file.write(f"{index} - {updated_task}\n")
                print("Файл було поновлено!")
            else:
                file.write(line)
    else:
        print("Одне або обидва з вводимих значень - порожні!")


def delete_task_from_file(task):
    file = open("task-list.txt", "r", encoding='utf-8')
    lines = file.readlines()
    file = open("task-list.txt", "w", encoding='utf-8')
    index = 1
    for line in lines:
        if line.strip()[4:] == task or line.strip()[:1] == task:
            print(f"Завдання: '{task}' видалено.")
        else:
            file.write(f"{index} - {line.strip()[4:]}\n")
            index += 1


def delete_all_tasks():
    file = open("task-list.txt", "w", encoding='utf-8')
    file.write('')
    print("Всі завдання, видалено з файлу!")


print('Вас вітає система запису нотаток!')
print('\n===============================================')
print('Правила користування:')
print("Введіть: \n'1' - для перегляду файлу, \n'2' - для додавання завдання у файл, \n'3' - для видалення завдання "
      "з файлу, \n'4' - для оновлення завдання, \n'5' - для видалення всіх завдань, \n'завершити' - для завершення "
      "виконання програми")
print('===============================================')
while True:
    input_value = input("Введіть показник того, що ви хочете зробити: ")
    if input_value.isdigit() or input_value.lower() == 'завершити' or input_value.lower() == 'продовжити':
        if input_value == '1':
            display_tasks_from_file()
        elif input_value == '2':
            new_task = input("Введіть нове завдання: ")
            write_task_in_file(new_task)
        elif input_value == '3':
            task_for_delete = input("Введіть завдання, яке хочете видалити, або його індекс: ")
            delete_task_from_file(task_for_delete)
        elif input_value == '4':
            want_to_update_task = input("Введіть завдання, яке хочете поновити: ")
            updated_task = input("Введіть оновлене завдання: ")
            update_task_from_file(want_to_update_task, updated_task)
        elif input_value == '5':
            delete_all_tasks()
        elif input_value.lower() == 'завершити':
            print('Ви успішно завершили  виконання програми, вітаю!')
            break
    else:
        print("Введено некоректне значення!")
        continue
