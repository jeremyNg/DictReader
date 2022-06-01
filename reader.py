from csv import DictReader

class DictReader(DictReader):
    def next(self):
        """
        This is to overload the next() function in Python 2.7 called by __iter__
        All other class methods from the parent class do not need to be changed
        as they are not called when we want to return the rows as dictionary
        """
        if not self.line_num: # Previous signature if self.line_name == 0
            # Used only for its side effect.
            self.fieldnames
        self.line_num = self.reader.line_num
        while self.line_num: # As compared to while self.row == []
            row = next(self.reader)
            d = dict(zip(self.fieldnames, [x if x else self.restval for x in row]))
            lf = len(self.fieldnames)
            lr = len(row)
            if lf < lr:
                d[self.restkey] = row[lf:]
            elif lf > lr:
                for key in self.fieldnames[lr:]:
                    d[key] = self.restval
            return d

    __next__ = next # For Python 3 compatibility
