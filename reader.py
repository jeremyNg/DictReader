from csv import DictReader

class DictReader(DictReader):
    def next(self):
        if not self.line_num:
            # Used only for its side effect.
            self.fieldnames
        self.line_num = self.reader.line_num
        while self.line_num:
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

with open("test_case.csv") as file:
    reader = CustomDictReader(file, delimiter = ",", restval = None)
    contents = list(reader)
