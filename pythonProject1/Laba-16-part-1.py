# Завдання 1
# Створіть однотабличну базу даних People (ім’я, прізвище, місто, країна, дата народження) з однойменною
# таблицею. Напишіть програму, яка дозволяє користувачеві ввести запит і отримати результати роботи запиту.
# Підтримуйте лише SELECT як запит. Якщо ви спробуєте
# виконати інші запити, потрібно буде генерувати помилку.
# Завдання 2
# Додайте до першого завдання можливість вносити,
# видаляти, оновлювати дані за допомогою запитів INSERT,
# DELETE, UPDATE. Перед виконанням запиту перевіряйте
# правильність назви таблиці. Також забороніть запит на
# видалення та оновлення усіх рядків (UPDATE та DELETE
# без умов).
# Завдання 3
# Модифікуйте перше завдання так, щоб користувач не
# міг вводити запит, а користувався готовими фільтрами.
# Наприклад: відображення усіх людей, відображення усіх
# людей з одного
# Практичне завдання
# 1
# міста (користувач задає з клавіатури як значення), відображення усіх людей з однієї країни (користувач задає з
# клавіатури як параметр).
# Завдання 4
# Модифікуйте третє завдання, щоб фільтр для показу міг бути комплексним. Наприклад, користувач може
# виставити фільтр на країну та місто, після чого відобразяться люди, для яких спрацює цей комплексний
# фільтр. Підтримайте умову АБО.
# Завдання 5
# Додайте до четвертого завдання можливість вносити,
# видаляти, оновлювати дані через інтерфейс додатка. Користувач не може ввести запит INSERT, UPDATE, DELETE
# безпосередньо.
# Завдання 6
# Додайте до додатку можливість зберігати результати
# роботи фільтрів у файл. Наприклад, результат роботи
# фільтра для відображення усіх людей або результат роботи
# фільтра з відображення людей з одного міста.
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import json
# {
#     "database": "Lesson.db"
# }
with open('config.json', 'w') as file:
    data = {'user':'postgres','password':'Andrey36912'}
    json.dump(data,file)
with open('config.json', 'r') as file:
    data = json.load(file)
    db_user = data['user']
    db_password = data['password']
db_ur1 = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Lesson'
engine = create_engine(db_ur1)


import sqlite3


def create_database():
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lesson (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL,
            birth_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def execute_select_query(query):
    if not query.lower().strip().startswith('select'):
        raise ValueError("Only SELECT queries are allowed.")

    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def main():
    create_database()

    while True:
        query = input("Enter your SELECT query: ")
        try:
            results = execute_select_query(query)
            for row in results:
                print(row)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()




def execute_query(query):
    if 'Lesson' not in query:
        raise ValueError("Invalid table name in query.")

    if query.lower().strip().startswith(('delete', 'update')) and 'where' not in query.lower():
        raise ValueError("UPDATE and DELETE queries must have a WHERE clause.")

    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def main():
    create_database()

    while True:
        query = input("Enter your query: ")
        try:
            if query.lower().strip().startswith('select'):
                results = execute_select_query(query)
                for row in results:
                    print(row)
            else:
                execute_query(query)
                print("Query executed successfully.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()



def create_database():
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lesson (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL,
            birth_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def execute_select_query(query):
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def display_menu():
    print("1. Display all Lesson")
    print("2. Display all Lesson from a specific city")
    print("3. Display all Lesson from a specific country")
    print("4. Exit")


def main():
    create_database()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            query = "SELECT * FROM Lesson"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '2':
            city = input("Enter city: ")
            query = f"SELECT * FROM Lesson WHERE city = '{city}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '3':
            country = input("Enter country: ")
            query = f"SELECT * FROM Lesson WHERE country = '{country}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()


def create_database():
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lesson (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL,
            birth_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def execute_select_query(query):
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def display_menu():
    print("1. Display all Lesson")
    print("2. Display all Lesson from a specific city")
    print("3. Display all Lesson from a specific country")
    print("4. Exit")


def main():
    create_database()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            query = "SELECT * FROM Lesson"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '2':
            city = input("Enter city: ")
            query = f"SELECT * FROM Lesson WHERE city = '{city}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '3':
            country = input("Enter country: ")
            query = f"SELECT * FROM Lesson WHERE country = '{country}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

import sqlite3


def create_database():
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lesson (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL,
            birth_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def execute_select_query(query):
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def display_menu():
    print("1. Display all Lesson")
    print("2. Display all Lesson from a specific city")
    print("3. Display all Lesson from a specific country")
    print("4. Exit")


def main():
    create_database()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            query = "SELECT * FROM Lesson"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '2':
            city = input("Enter city: ")
            query = f"SELECT * FROM Lesson WHERE city = '{city}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '3':
            country = input("Enter country: ")
            query = f"SELECT * FROM Lesson WHERE country = '{country}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()


def execute_select_query(query):
    conn = sqlite3.connect('Lesson.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def display_menu():
    print("1. Display all people")
    print("2. Display all people from a specific city")
    print("3. Display all people from a specific country")
    print("4. Display all people from a specific city and country")
    print("5. Save results to a file")
    print("6. Exit")


def save_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Results saved to {file_path}")


def main():
    create_database()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            query = "SELECT * FROM Lesson"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '2':
            city = input("Enter city: ")
            query = f"SELECT * FROM Lesson WHERE city = '{city}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '3':
            country = input("Enter country: ")
            query = f"SELECT * FROM Lesson WHERE country = '{country}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '4':
            city = input("Enter city: ")
            country = input("Enter country: ")
            query = f"SELECT * FROM Lesson WHERE city = '{city}' OR country = '{country}'"
            results = execute_select_query(query)
            for row in results:
                print(row)
        elif choice == '5':
            city = input("Enter city (leave blank to skip): ")
            country = input("Enter country (leave blank to skip): ")
            if city and country:
                query = f"SELECT * FROM Lesson WHERE city = '{city}' OR country = '{country}'"
            elif city:
                query = f"SELECT * FROM Lesson WHERE city = '{city}'"
            elif country:
                query = f"SELECT * FROM Lesson WHERE country = '{country}'"
            else:
                query = "SELECT * FROM Lesson"

            results = execute_select_query(query)
            file_path = input("Enter the file path to save results: ")
            save_results_to_file(results, file_path)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()