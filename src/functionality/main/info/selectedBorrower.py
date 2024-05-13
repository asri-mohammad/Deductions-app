class SelectedBorrower:

    selected_borrower = None

    @classmethod
    def set(cls, employee_id):
        """set the current selected user to the given employee id"""

        cls.selected_borrower = employee_id

    @classmethod
    def get(cls):
        """returns the selected user"""

        return cls.selected_borrower

    @classmethod
    def set_to_none(cls):
        """set the selected user to None"""

        cls.selected_borrower = None
