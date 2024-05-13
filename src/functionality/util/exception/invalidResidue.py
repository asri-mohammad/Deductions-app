class InvalidActivUserResidue(Exception):
    msg = "For all active users a valid residue must be provided."

    def __init__(self, msg=msg, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)