import customtkinter as ctk
import books as bk
import issue_log as ig
import library_functions as lf

def user_data():
    def book_available():
        root4.destroy()
        bk.books()

    def issue_log():
        root4.destroy()
        ig.issue_log()

    def logout():
        lf.current_user = None
        for window in root4.winfo_children():
            window.destroy()
        root4.destroy()
        exit(0)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root4 = ctk.CTk()
    root4.title("User Dashboard")
    root4.geometry("400x250")
    root4.resizable(False, False)

    frame4 = ctk.CTkFrame(root4, corner_radius=15)
    frame4.pack(expand=True, fill="both", padx=40, pady=40)

    title_label = ctk.CTkLabel(frame4, text="User Dashboard", font=ctk.CTkFont(size=24, weight="bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(5, 25))

    label41 = ctk.CTkLabel(frame4, text="Books Available:")
    label41.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    button41 = ctk.CTkButton(frame4, text="Show", command=book_available, width=120, height=35)
    button41.grid(row=1, column=1, padx=10, pady=10)

    label42 = ctk.CTkLabel(frame4, text="Return Books:")
    label42.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    button42 = ctk.CTkButton(frame4, text="Show", command=issue_log, width=120, height=35)
    button42.grid(row=2, column=1, padx=10, pady=10)

    logout_button = ctk.CTkButton(root4,text="Exit",fg_color="#d9534f",hover_color="#c9302c",width = 60,command=logout)
    logout_button.place(relx=0.95, rely=0.95, anchor="se")

    frame4.grid_rowconfigure((0, 1, 2), weight=1)
    frame4.grid_columnconfigure((0, 1), weight=1)

    root4.mainloop()
