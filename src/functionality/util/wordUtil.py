class WordUtil:
    @staticmethod
    def reverse_slashed_string(s):
        """convert strings like ab/cd to cd/ab"""
        arr = s.split("/")
        arr.reverse()
        return "/".join(arr)

