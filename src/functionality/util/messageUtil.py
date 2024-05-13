from tkinter import messagebox


class MessageUtil:

    @staticmethod
    def show_message(message_type, message):
        """show a message with selected message box"""

        if message_type == 1:
            messagebox.showinfo("Info", message)
        elif message_type == 2:
            messagebox.showwarning("Oops", message)
        elif message_type == 3:
            messagebox.showerror("Error", message)

    @classmethod
    def show_effected_row(cls, row_count):
        """display an info box to inform user the number of effected rows in DB"""

        cls.show_message(1, f"{row_count} rows were effected.")