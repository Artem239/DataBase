# Автор: Куулар Артём
from tkinter import *
import random
import smtplib


def encrypt(text1):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    alphabetComp = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                    'x', 'c', 'v', 'b', 'n', 'm', 'M', 'N', 'B', 'V', 'C', 'X', 'Z', 'L', 'K', 'J', 'H', 'G', 'F', 'D',
                    'S', 'A', 'P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'W', 'Q', '*', '&', '$', '@', '!', '>', ',', '<',
                    '(', '±', '#']

    text = list(text1)
    for i in range(len(text)):
        if text[i] in alphabet:
            text[i] = alphabetComp[alphabet.index(text[i])]
    return "".join(text)


def decrypt(text1):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    alphabetComp = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                    'x', 'c', 'v', 'b', 'n', 'm', 'M', 'N', 'B', 'V', 'C', 'X', 'Z', 'L', 'K', 'J', 'H', 'G', 'F', 'D',
                    'S', 'A', 'P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'W', 'Q', '*', '&', '$', '@', '!', '>', ',', '<',
                    '(', '±', '#']
    text = list(text1)
    for i in range(len(text)):
        if text[i] in alphabetComp:
            text[i] = alphabet[alphabetComp.index(text[i])]
    return "".join(text)


def reader(n):
    dataBase = open("dataBase.txt", "r")
    text = dataBase.read()
    dataBase.close()
    text1 = text.split("\n")
    text1 = text1[n].split(" ")
    return text1


def reader2(n, text):
    text1 = text.split("\n")
    text1 = text1[n].split(" ")
    return text1


def izmenit(event):
    global lol

    n = lol[0]
    value = lol[1]
    parameter = 2
    dataBase = open("dataBase.txt", "r")
    text = dataBase.read()
    dataBase.close()
    dataBase = open("dataBase.txt", "w")
    line = reader2(n, text)
    line[parameter] = encrypt(value.get())
    text1 = text.split("\n")
    text1[n] = " ".join(line)
    dataBase.write("\n".join(text1))
    dataBase.close()
    l1.config(bg='red')
    l1['text'] = "Необходимо перезайти"
    mb.showinfo("Сообщение", "Баланс изменён")
    mb.showinfo("Сообщение", "Перезайдите в аккаунт")


def sozdat(event):
    dataBase = open("dataBase.txt", "r")
    text = dataBase.read()
    dataBase.close()
    global reg
    for n in range(len(text.split("\n"))):
        if decrypt(reader(n)[0]) == reg[0].get():
            mb.showerror("Сообщение", "Логин занят")
            return

    if reg[3].get() != reg[5]:
        mb.showerror("Сообщение", "Код не правилен")
        return

    mb.showinfo("Сообщение", "Регистрация прошла успешно")

    if reg[1].get() == reg[2].get():
        dataBase = open("dataBase.txt", "r")
        text = dataBase.read()
        dataBase.close()
        dataBase = open("dataBase.txt", "w")
        dataBase.write(text + encrypt("\n" + reg[0].get() + " " + reg[1].get() + " " + "0"))
        dataBase.close()


def registration(event):
    root1 = Tk()
    root1.geometry('600x400+0+0')
    root1.title("Пробная база данных: Регистрация")
    root1.resizable(False, False)
    l4 = Label(root1, text="Ваш логин")
    e3 = Entry(root1, width=50)
    l5 = Label(root1, text="Ваш пароль")
    e4 = Entry(root1, width=50, show='*')
    l6 = Label(root1, text="Подтвердите пароль")
    e5 = Entry(root1, width=50, show='*')
    l7 = Label(root1, text="Ваш email")
    e6 = Entry(root1, width=50)
    b1 = Button(root1, text="Отправить код")
    l8 = Label(root1, text="Ваш код")
    e7 = Entry(root1, width=50)

    b3 = Button(root1, text="Зарегистрироваться")
    global reg
    reg = [e3, e4, e5, e7, e6, 0]
    b1.bind('<Button-1>', send)

    b3.bind('<Button-1>', sozdat)
    l4.pack()
    e3.pack()
    l5.pack()
    e4.pack()
    l6.pack()
    e5.pack()
    l7.pack()
    e6.pack()
    b1.pack()
    l8.pack()
    e7.pack()

    b3.pack()
    root1.mainloop()


def entry(event):
    dataBase = open("dataBase.txt", "r")
    text = dataBase.read()
    dataBase.close()

    for n in range(1, len(text.split("\n"))):
        if decrypt(reader(n)[0]) == e1.get() and decrypt(reader(n)[1]) == e2.get():
            l1.config(bg='green')
            l1['text'] = "Вход выполнен"
            online()
            return
    mb.showerror("Ошибка", "Логин или пароль неправилен")


def send(event):
    a = 1
    b = 9
    s1 = str(random.randint(a, b))
    s2 = str(random.randint(a, b))
    s3 = str(random.randint(a, b))
    s4 = str(random.randint(a, b))
    text = s1 + s2 + s3 + s4
    text1 = "Your code for registration is " + text
    print(text1)
    global reg
    to_email = reg[4].get()
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('databaseworking64@gmail.com', 'Artemsuper2008')

    smtpObj.sendmail("databaseworking64@gmail.com", to_email, text1)
    smtpObj.quit()
    reg[5] = text


def online():
    root2 = Tk()
    root2.geometry('600x400+400+200')
    root2.resizable(False, False)
    root2.title("Canvas: entry")

    dataBase = open("dataBase.txt", "r")
    text = dataBase.read()
    dataBase.close()
    for n in range(len(text.split("\n"))):
        if decrypt(reader(n)[0]) == e1.get():
            balance = decrypt(reader(n)[2])
            break

    l7 = Label(root2, text=("Ваш логин - " + e1.get()))
    l8 = Label(root2, text=("Ваш пароль - " + e2.get()))
    l9 = Label(root2, text=("Ваш баланс - " + balance))
    l10 = Label(root2, text="Изменить баланс: ")
    e = Entry(root2, width=50)
    b = Button(root2, text="Ок")
    global lol
    lol = [n, e, 2]

    b.bind('<Button-1>', izmenit)

    l7.pack()
    l8.pack()
    l9.pack()
    l10.pack()
    e.pack()
    b.pack()
    root2.mainloop()


# Интерфейс


from tkinter import messagebox as mb

root = Tk()

root.geometry('600x400+200+100')
root.resizable(False, False)
root.title("пробная база данных")
l1 = Label(text="Вход не выполнен", bg="red")
l2 = Label(text="Логин")
e1 = Entry(width=50)
l3 = Label(text="Пароль")
e2 = Entry(width=50, show='*')
b1 = Button(text="Войти")
b2 = Button(text="Новый аккаунт")
reg = False
lol = False

b2.bind('<Button-1>', registration)
b1.bind('<Button-1>', entry)

l1.pack()
l2.pack()
e1.pack()
l3.pack()
e2.pack()
b1.pack()
b2.pack()
root.mainloop()
