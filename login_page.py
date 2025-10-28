import customtkinter as ctk
import library_functions as lf
import user_page as up

def login(parent):
    def call():
        email = entry4.get()
        password = entry5.get()
        root3.destroy()
        parent.destroy()
        lf.login(email, password)
        print(lf.current_user)
        up.user_data()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root3 = ctk.CTkToplevel(parent)
    root3.title("Login")
    root3.geometry("400x300")
    root3.resizable(False, False)

    root3.lift()
    root3.attributes('-topmost', True)

    frame2 = ctk.CTkFrame(root3, corner_radius=15)
    frame2.pack(expand=True, fill="both", padx=40, pady=40)

    title_label = ctk.CTkLabel(frame2, text="Login to Your Account", font=ctk.CTkFont(size=22, weight="bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    label23 = ctk.CTkLabel(frame2, text="Email:")
    label23.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    entry4 = ctk.CTkEntry(frame2, width=200, placeholder_text="Enter your email")
    entry4.grid(row=1, column=1, padx=10, pady=10)

    label24 = ctk.CTkLabel(frame2, text="Password:")
    label24.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    entry5 = ctk.CTkEntry(frame2, width=200, show="*", placeholder_text="Enter your password")
    entry5.grid(row=2, column=1, padx=10, pady=10)

    button21 = ctk.CTkButton(frame2, text="Submit", command=call, width=120, height=35, corner_radius=8)
    button21.grid(row=3, column=0, columnspan=2, pady=(20, 10))

    frame2.grid_rowconfigure((0, 1, 2, 3), weight=1)
    frame2.grid_columnconfigure((0, 1), weight=1)

    root3.mainloop()
