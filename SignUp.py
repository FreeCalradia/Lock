import tkinter as tk


def register():
    screen1 = tk.Toplevel()
    screen1.title("Register")
    screen1.geometry("300x250")

    username = StringVar()
    password = StringVar()

    tk.Label(screen1, text="Username * ").pack()
    tk.Entry(screen1, textvariable=username)
    tk.Label(screen1, text="Password * ").pack()
    tk.Entry(screen1, textvariable=password)


def login():
    print("Login session started")


def main_screen():
    screen = tk.Tk()
    screen.geometry("500x350")
    screen.title("Lock 0.1")
    tk.Label(
        text="Lock 0.1", bg="yellow", width="300", height="2", font=("Calibri", 13)
    ).pack()
    tk.Label(text="").pack()
    tk.Button(text="Login", width="20", height="2", command=login).pack()
    tk.Label(text="").pack()
    tk.Button(text="Register", width="20", height="2", command=register).pack()

    screen.mainloop()


main_screen()
