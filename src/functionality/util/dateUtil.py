import jdatetime


class DateUtil:

    @staticmethod
    def date_year_string():
        """return a string if format like 140203"""

        today = jdatetime.date.today()
        year = today.year
        month = today.month
        return str(year) + str(month).zfill(2)

    @staticmethod
    def today():
        """return today date in format 1402/01/07"""
        return str(jdatetime.date.today()).replace("-", "/")


