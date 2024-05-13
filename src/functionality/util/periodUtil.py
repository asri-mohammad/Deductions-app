class PeriodUtil:

    @staticmethod
    def next_month_str(period):
        """add one month to the given period, gets string and returns a string"""

        year = int(period[0:4])
        month = int(period[4:6])
        if month != 12:
            return str(year) + str(month+1).zfill(2)
        else:
            return str(year+1) + "01"

    @staticmethod
    def previous_month_str(period):
        """decrease one month to the given period, gets string and returns a string"""

        year = int(period[0:4])
        month = int(period[4:6])
        if month != 1:
            return str(year) + str(month - 1).zfill(2)
        else:
            return str(year - 1) + "12"

    @classmethod
    def next_month_int(cls, period):
        """add one month to the given period, gets int and returns a int"""

        return int(cls.next_month_str(str(period)))

    @classmethod
    def previous_month_int(cls, period):
        """decrease one month to the given period, gets int and returns an int"""

        return int(cls.previous_month_str(str(period)))

    @staticmethod
    def period_subtract(period_a, period_b):
        """two int period and return how many months period_a is ahead of period_b,
            period_a must be bigger than period_b, otherwise it would throw and error
        """
        
        if period_b > period_a:
            raise Exception("first arg must be bigger or equal to second arg")
        else:
            period_a_y = int(str(period_a)[0:4])
            period_a_m = int(str(period_a)[4:6])
            period_b_y = int(str(period_b)[0:4])
            period_b_m = int(str(period_b)[4:6])
            delta_y = period_a_y - period_b_y
            delta_m = period_a_m - period_b_m

            return (delta_y * 12) + delta_m






