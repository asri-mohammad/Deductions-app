import re

from src.functionality.util.commonUtil import CommonUtil
from src.functionality.util.wordUtil import WordUtil


class WordMaker:

    @staticmethod
    def paragraph_replace_text(paragraph, regex, replace_str):
        """Return `paragraph` after replacing all matches for `regex` with `replace_str`.

        `regex` is a compiled regular expression prepared with `re.compile(pattern)`
        according to the Python library documentation for the `re` module.


        the code was copied from
        https://github.com/python-openxml/python-docx/issues/30#issuecomment-879593691
        """
        # --- a paragraph may contain more than one match, loop until all are replaced ---
        while True:
            text = paragraph.text
            match = regex.search(text)
            if not match:
                break

            # --- when there's a match, we need to modify run.text for each run that
            # --- contains any part of the match-string.
            runs = iter(paragraph.runs)
            start, end = match.start(), match.end()

            # --- Skip over any leading runs that do not contain the match ---
            for run in runs:
                run_len = len(run.text)
                if start < run_len:
                    break
                start, end = start - run_len, end - run_len

            # --- Match starts somewhere in the current run. Replace match-str prefix
            # --- occurring in this run with entire replacement str.
            run_text = run.text
            run_len = len(run_text)
            run.text = "%s%s%s" % (run_text[:start], replace_str, run_text[end:])
            end -= run_len  # --- note this is run-len before replacement ---

            for run in runs:  # --- next and remaining runs, uses same iterator ---
                if end <= 0:
                    break
                run_text = run.text
                run_len = len(run_text)
                run.text = run_text[end:]
                end -= run_len
        return paragraph

    @staticmethod
    def en_to_per_string(string):
        """replace English numbers with Persian equivalents"""

        ar_num = '۰١٢٣٤٥٦٧٨٩'
        en_num = '0123456789'
        table = str.maketrans(en_num, ar_num)

        persian_string = string.translate(table)
        return persian_string

    @classmethod
    def make_word_doc(cls, word_doc, placeholder_values_dic):
        """return a Word document where all the placeholders are substitutes with actual value"""

        for p in word_doc.paragraphs:
            regex = re.compile("<date>")
            date = cls.en_to_per_string(placeholder_values_dic["date"])
            date = WordUtil.reverse_slashed_string(date)
            cls.paragraph_replace_text(p, regex, date)

            regex = re.compile("<letter_num>")
            letter_num = cls.en_to_per_string(placeholder_values_dic["letter_num"])
            letter_num = WordUtil.reverse_slashed_string(letter_num)
            cls.paragraph_replace_text(p, regex, letter_num)

            regex = re.compile("<year>")
            year = cls.en_to_per_string(placeholder_values_dic["year"])
            cls.paragraph_replace_text(p, regex, year)

            regex = re.compile("<month>")
            cls.paragraph_replace_text(p, regex, placeholder_values_dic["month"])

            regex = re.compile("<amount>")
            amount = placeholder_values_dic["amount"]
            if amount.isdigit():
                amount = CommonUtil.format_number_comma_separated(amount)
            amount = cls.en_to_per_string(amount)
            cls.paragraph_replace_text(p, regex, amount)

        return word_doc