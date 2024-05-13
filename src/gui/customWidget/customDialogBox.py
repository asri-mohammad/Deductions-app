from tkinter import *
from tkinter import simpledialog
from tkinter.simpledialog import Dialog


class CustomDialogBox(Dialog):
    def __init__(self, title, label_1, label_2, date_init_value=None, amount_init_value=None,
                 parent=None):

        self.label_1 = label_1
        self.label_2 = label_2
        self.date_init_value = date_init_value
        self.amount_init_value = amount_init_value
        Dialog.__init__(self, parent, title)

    def destroy(self):
        # self.entry = None
        simpledialog.Dialog.destroy(self)

    def body(self, master):

        lbl_date = Label(master, text=self.label_1, justify=LEFT)
        lbl_date.grid(row=0, column=0, columnspan=1, padx=5, sticky=W)
        lbl_amount = Label(master, text=self.label_2, justify=LEFT)
        lbl_amount.grid(row=1, column=0, columnspan=1, padx=5, sticky=W)

        self.entry_one = Entry(master, name="entry_one")
        self.entry_one.grid(row=0, column=1, columnspan=1, padx=5, sticky=W + E)
        self.entry_two = Entry(master, name="entry_two")
        self.entry_two.grid(row=1, column=1, columnspan=1, padx=5, sticky=W + E)

        if self.date_init_value is not None:
            self.entry_one.insert(0, self.date_init_value)
            self.entry_one.select_range(0, END)

        if self.amount_init_value is not None:
            self.entry_two.insert(0, self.amount_init_value)
            self.entry_two.select_range(0, END)

        return None

    def validate(self):
        result_lst = [self.entry_one.get(), self.entry_two.get()]
        self.result = result_lst

        return 1

    @staticmethod
    def askstring(title, label_1, label_2, date_init_value=None, amount_init_value=None):
        d = CustomDialogBox(title, label_1, label_2, date_init_value=date_init_value, amount_init_value=amount_init_value)
        return d.result





