import customtkinter as ctk
from tkinter import messagebox
import library_functions as lf
import user_page as up

def issue_log():
    root6 = ctk.CTk()
    root6.title("Return books")
    root6.geometry("400x400")

    frame6 = ctk.CTkFrame(root6)
    frame6.pack(padx=20, pady=20, fill="both", expand=True)

    title_label = ctk.CTkLabel(
        frame6,
        text="Return books",
        font=ctk.CTkFont(size=20, weight="bold")
    )
    title_label.pack(pady=(10, 15))

    rows = lf.issue_log()

    def confirm_return(book_id, book_name):
        popup = ctk.CTkToplevel(root6)
        popup.title("Confirm Return")
        popup.geometry("300x150")
        popup.grab_set()

        label = ctk.CTkLabel(
            popup,
            text=f"Are you sure you want to return\n'{book_name}'?",
            justify="center",
            font=ctk.CTkFont(size=15)
        )
        label.pack(pady=15)

        def yes_action():
            popup.destroy()
            amount = lf.return_book(book_id)
            messagebox.showinfo(
                "Book Returned",
                f"The book has been returned successfully!\nAmount payable: ₹{amount}"
            )
            root6.destroy()
            issue_log()

        def no_action():
            popup.destroy()

        button_frame = ctk.CTkFrame(popup, fg_color="transparent")
        button_frame.pack(pady=10)

        yes_button = ctk.CTkButton(button_frame, text="Yes", width=80, command=yes_action)
        yes_button.grid(row=0, column=0, padx=10)

        no_button = ctk.CTkButton(button_frame, text="No", width=80, fg_color="gray", command=no_action)
        no_button.grid(row=0, column=1, padx=10)

    for i in rows:
        book_name = str(lf.get_name(i[1]))
        book_button = ctk.CTkButton(
            frame6,
            text=book_name,
            command=lambda book_id=i[1], name=book_name: confirm_return(book_id, name),
            corner_radius=8,
            width=250
        )
        book_button.pack(pady=5)

    root6.mainloop()
    up.user_data()