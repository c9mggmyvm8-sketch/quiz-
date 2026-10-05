import random
import time

users = {}
cards = {}
notes = {}

def is_valid_password(password):
    if len(password) < 5:
        return False
    return password.isalnum()
def register():
    print("register")
    username = input("Username: ")

    if username in users:
        print("username already taken")
        return
    if username == "":
        print("username cannot be empty")
        return

    password = input("Password: ")
    if not is_valid_password(password):
        print("password is invalid")
        return

    users[username] = password
    cards[username] = []
    notes[username] = []

    print("successfully registered")

def login():
    print("login")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print("login successful")
        return username
    else:
        print("login failed")
        return None

def add_card(username):
    print("add card")
    question = input("Question: ")
    answer = input("Answer: ")

    if question == "" or answer == "":
        print("question and answer cannot be empty")
        return
    cards[username].append(question)
    print("successfully added")

def show_random_cards(username):
    user_cards = cards[username]

    if not user_cards:
        print("no cards added")
        return
    card = random.choice(user_cards)
    print("random card")
    print(f"question: {card['question']}")
    input("press enter to show answer")
    print("answer: ", card['answer'])

def run_quiz(username):
    user_cards = cards[username]

    if not user_cards:
        print("no cards added")
        return

    print("running quiz")
    quiz_cards = user_cards.copy()
    random.shuffle(quiz_cards)

    correct = 0

    for i, card in enumerate(quiz_cards):
        print(f"question: {card['question']}")

        start_time = time.time()
        user_answer = input("Answer: ")
        end_time = time.time()-start_time

        if user_answer == card['answer']:
            correct += 1
            print(f"correct, time: {end_time}")
        else:
            print(f"incorrect, right answer: {card["answer"]}, time: {end_time}")
    print(f"total correct: {correct}")

def add_note(username):
    text = input("Note: ")
    if text == "":
        print("note cannot be empty")
    notes[username].append(text)
    print("successfully added")
def show_notes(username):
    notes = notes[username]
    if not notes:
        print("no notes added")
        return

    print("notes: ", notes)
    input("press enter to show notes")
    print("note count: ", len(notes))

def show_note(username):
    user_notes = notes[username]
    if not user_notes:
        print("no notes added")
        return

    print("notes:")

    for i, note in enumerate(user_notes, start=1):
        print(f"{i}: {note}")

def edit_note(username):
    show_notes(username)
    user_notes = notes[username]
    if not user_notes:
        return
    try:
        number = int(input("enter note number: "))
        index = number-1

        if index < 0 or index >= len(user_notes):
            print("note number out of range")
            return

        new_text = input("enter new text: ")
        if new_text == "":
            print("text cannot be empty")
            return
        user_notes[index] = new_text
        print("successfully edited")
    except ValueError:
        print("enter a number")
def delete_note(username):
    show_notes(username)
    user_notes = notes[username]
    if not user_notes:
        print("no notes added")
        return

    try:
        number = int(input("enter note number: "))
        index = number-1

        if index < 0 or index >= len(user_notes):
            print("note number out of range")
            return

        removed = user_notes.pop(index)
        print(f"removed: {removed}")
    except ValueError:
        print("enter a number")

def notes_menu(username):
    while True:
        print("\n --- notes menu ---")
        print("1. add note")
        print("2. show notes")
        print("3. edit note")
        print("4. delete note")
        print("5. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note(username)
        elif choice == "2":
            show_notes(username)
        elif choice == "3":
            edit_note(username)
        elif choice == "4":
            delete_note(username)
        elif choice == "5":
            break

def main_menu(username):
    while True:
        print(f"\n --- main menu {username} ---")
        print("1. add card")
        print("2. random card")
        print("3. start quiz")
        print("4. show notes")
        print("5. log out")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_card(username)
        elif choice == "2":
            show_random_cards(username)
        elif choice == "3":
            run_quiz(username)
        elif choice == "4":
            show_notes(username)
        elif choice == "5":
            break
def start_menu():
    while True:
        print("\n --- app ---")
        print("1. registration")
        print("2. login")
        print("3. log out")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username is not None:
                main_menu(username)
        elif choice == "3":
            break

if __name__ == "__main__":
    start_menu()



