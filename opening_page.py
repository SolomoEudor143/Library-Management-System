import customtkinter as ctk
import register_page as register
import login_page as login

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root1 = ctk.CTk()
root1.title("Login Page")
root1.geometry("400x300")

def Register():
    register.reg(root1)

def Login():
    login.login(root1)

frame1 = ctk.CTkFrame(root1, corner_radius=15)
frame1.pack(expand=True, fill="both", padx=40, pady=40)

title_label = ctk.CTkLabel(frame1, text="Welcome", font=ctk.CTkFont(size=24, weight="bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 30))

button1 = ctk.CTkButton(frame1, text="Register", command=Register, width=120, height=40, corner_radius=8)
button1.grid(row=1, column=0, padx=20, pady=15)

button2 = ctk.CTkButton(frame1, text="Login", command=Login, width=120, height=40, corner_radius=8)
button2.grid(row=1, column=1, padx=20, pady=15)

frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure((0, 1), weight=1)

root1.mainloop()
