import customtkinter as ctk
import library_functions as lf
import user_page as up

def reg(parent):
    def add21():
        name = entry3.get()
        email = entry4.get()
        password = entry5.get()
        root2.destroy()
        parent.destroy()
        lf.register_user(name, email, password)
        lf.login(email, password)
        print(lf.current_user)
        up.user_data()
        lf.list_users()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root2 = ctk.CTkToplevel(parent)
    root2.title("Registration")
    root2.geometry("420x350")
    root2.resizable(False, False)

    root2.lift()
    root2.attributes('-topmost', True)

    frame2 = ctk.CTkFrame(root2, corner_radius=15)
    frame2.pack(expand=True, fill="both", padx=40, pady=40)

    title_label = ctk.CTkLabel(frame2, text="Create Your Account", font=ctk.CTkFont(size=22, weight="bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(10, 25))

    label22 = ctk.CTkLabel(frame2, text="Name:")
    label22.grid(row=1, column=0, sticky="e", padx=10, pady=8)
    entry3 = ctk.CTkEntry(frame2, width=220, placeholder_text="Enter your name")
    entry3.grid(row=1, column=1, padx=10, pady=8)

    label23 = ctk.CTkLabel(frame2, text="Email:")
    label23.grid(row=2, column=0, sticky="e", padx=10, pady=8)
    entry4 = ctk.CTkEntry(frame2, width=220, placeholder_text="Enter your email")
    entry4.grid(row=2, column=1, padx=10, pady=8)

    label24 = ctk.CTkLabel(frame2, text="Password:")
    label24.grid(row=3, column=0, sticky="e", padx=10, pady=8)
    entry5 = ctk.CTkEntry(frame2, width=220, show="*", placeholder_text="Enter your password")
    entry5.grid(row=3, column=1, padx=10, pady=8)

    button21 = ctk.CTkButton(frame2, text="Submit", command=add21, width=140, height=40, corner_radius=8)
    button21.grid(row=4, column=0, columnspan=2, pady=(25, 10))

    frame2.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
    frame2.grid_columnconfigure((0, 1), weight=1)

    root2.mainloop()
