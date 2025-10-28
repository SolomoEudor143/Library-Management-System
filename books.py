import customtkinter as ctk
from tkinter import messagebox
import library_functions as lf
import user_page as up

def books():
    root5 = ctk.CTk()
    root5.title("Books")
    root5.configure(fg_color=("#1e1e1e", "#1e1e1e"))
    root5.geometry("800x400")
    frame5 = ctk.CTkFrame(root5)
    frame5.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
    root5.rowconfigure(0, weight=1)
    root5.columnconfigure(0, weight=1)

    check_vars = {}

    def issue_selected():
        selected_ids = tuple(book_id for book_id, var in check_vars.items() if var.get() == 1)
        num_to_issue = len(selected_ids)
        if not selected_ids:
            messagebox.showwarning("No Selection", "No books selected.")
            return
        try:
            current_count = lf.issue_count()
            if (current_count + num_to_issue) > 3:
                messagebox.showwarning("Limit Reached",
                                       f"You can only issue a maximum of 3 books.\n"
                                       f"You already have {current_count} issued.")
                return
            lf.issue_book(selected_ids)
            messagebox.showinfo("Success", f"Successfully issued {num_to_issue} book(s)!")
            search()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            root5.lift()
            root5.focus_force()

    def render_books(book_list):
        for widget in book_frame.winfo_children():
            widget.destroy()
        check_vars.clear()

        normal_font = ctk.CTkFont(family="Segoe UI", size=13)
        strike_font = ctk.CTkFont(family="Segoe UI", size=13, overstrike=True)

        for c, (book_id, title, author, issued) in enumerate(book_list):
            status = "Available" if issued == 0 else "Issued"

            var = ctk.IntVar(value=0)
            check_vars[book_id] = var

            chk = ctk.CTkCheckBox(
                book_frame,
                text="",
                variable=var,
                onvalue=1,
                offvalue=0
            )
            chk.grid(row=c, column=0, sticky="w", padx=(5, 0))

            if issued:
                chk.configure(state="disabled")

            text_color = "white"
            font_to_use = strike_font if issued else normal_font
            label_text = f"ID: {book_id} | Title: {title} | Author: {author} | Status: {status}"

            label = ctk.CTkLabel(
                book_frame,
                text=label_text,
                text_color=text_color,
                font=font_to_use,
                anchor="w",
            )
            label.grid(row=c, column=1, sticky="w", padx=(0, 5), pady=2)

    def search():
        query = entry51.get().strip().lower()
        all_books = lf.list_books()
        if not query:
            filtered = all_books
        else:
            filtered = [b for b in all_books if query in b[1].lower()]

        if not filtered:
            messagebox.showwarning("Not Found", "No books matched your search.")
        render_books(filtered)

    button_issue = ctk.CTkButton(frame5, text="Issue Selected", command=issue_selected)
    button_issue.grid(row=0, column=0, sticky="w", padx=3, pady=3)

    label51 = ctk.CTkLabel(frame5, text='Search book:')
    label51.grid(row=0, column=1, sticky="e", padx=3)
    entry51 = ctk.CTkEntry(frame5)
    entry51.grid(row=0, column=2, sticky="ew", padx=3)
    button51 = ctk.CTkButton(frame5, text="Search", command=search)
    button51.grid(row=0, column=3, padx=5, pady=5)

    frame5.columnconfigure(2, weight=1)
    frame5.rowconfigure(2, weight=1)

    book_frame = ctk.CTkScrollableFrame(frame5)
    book_frame.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)

    rows = lf.list_books()
    render_books(rows)
    root5.mainloop()
    up.user_data()