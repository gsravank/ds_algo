class Date:
    def __init__(self, yyyy, mm, dd):
        self.year = yyyy
        self.month = mm
        self.date = dd

    def __str__(self):
        return f"{self.year}{'' if self.month >= 10 else '0'}{self.month}{'' if self.date >= 10 else '0'}{self.date}"

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.date == other.date

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False

        if self.month < other.month:
            return True
        elif self.month > other.month:
            return False

        if self.date < other.date:
            return True
        else:
            return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)