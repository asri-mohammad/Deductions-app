from tkinter import filedialog as fd
import tkinter as tk
import os


class GUIUtil:

    @staticmethod
    def clear_write_text_widget(widget, text):
        """clear the text widget contents and writs the given text to it"""
        widget.delete("1.0", "end")
        widget.insert(tk.END, text)

    @staticmethod
    def clear_write_entry_widget(widget, text):
        """clear the entry widget contents and writs the given text to it"""
        widget.delete(0, tk.END)
        widget.insert(0, text)

    @staticmethod
    def clear_write_label_widget(widget, text):
        widget.config(text=text)

    @staticmethod
    def ask_open_file_name(initial_dir=os.path.abspath(os.sep), document_type="excel"):
        """open a file explore and returns the path to the chosen file"""
        if document_type == "excel":
            filetypes = [("Excel file", ".xlsx .xlsm")]
        elif document_type == "sqlite_db":
            filetypes = [("Sqlite DB", ".db")]
        path = fd.askopenfilename(filetypes=filetypes, initialdir=initial_dir)
        return path

    @staticmethod
    def ask_save_file_name(initial_file_name, file_type="excel", initial_dir=os.path.abspath(os.sep)):
        """returns a full path indicating file directory and name for the file that needs to  be saved """
        filetypes = None
        defaultextension = None

        if file_type == "excel":
            filetypes = (("Excel", "*.xlsx"), ("Macro enabled Excel", "*.xlsm"))
            defaultextension = "*.xlsx"
        elif file_type == "word":
            filetypes = [("MS Word", "*.docx")]
            defaultextension = "*.docx"
        elif file_type == "sqlite_db":
            filetypes = [("Sqlite DB", "*.db")]
            defaultextension = "*.db"

        path = fd.asksaveasfilename(initialfile=initial_file_name, initialdir=initial_dir,
                                    filetypes=filetypes, defaultextension=defaultextension)
        return path

    @staticmethod
    def ask_directory(initial_dir=os.path.abspath(os.sep)):
        """Opens a file explorer so user can select a directory"""
        path = fd.askdirectory(mustexist=True, initialdir=initial_dir)
        return path

    @staticmethod
    def read_entry(entry_widget):
        """returns text value of the entry widget"""
        text = entry_widget.get()
        return text

    @staticmethod
    def read_textbox(textbox_widget):
        """returns text value of the textbox widget"""

        text = textbox_widget.get("1.0", tk.END)
        return text

    @staticmethod
    def divide_container_equally(container, row_number, column_number):
        """divides the given widget into same size uniform column_number * row_number area"""
        for i in range(0, row_number):
            container.rowconfigure(i, weight=1, uniform="a")

        for j in range(0, column_number):
            container.columnconfigure(j, weight=1, uniform="a")

    @staticmethod
    def divide_container_equally_custom_weight(container, row_number, column_number, row_weight_list, column_wight_lst):
        """divides the given widget into same size uniform column_number * row_number area with
        given list of weights for each row and column"""
        for i in range(0, row_number):
            container.rowconfigure(i, weight=row_weight_list[i])

        for j in range(0, column_number):
            container.columnconfigure(j, weight=column_wight_lst[j])

