from Models import *


class BaseReader(object):

    def __init__(self, rows, model):
        self.rows = rows
        self.model = model
        self.start = -1
        self.end = -1

    def is_title_row(self, row=None) -> bool:
        if row is None:
            return False

        if len(row) < len(self.model.titles):
            return False
        else:
            for idx in range(len(self.model.titles)):
                if self.model.titles[idx] not in row[idx]:
                    return False
            return True

    def locate_begin_pos(self):
        line_num = 0

        for row in self.rows:
            # title的下一行 ，才是数据开始的行数
            line_num += 1
            if self.is_title_row(row):
                self.start = line_num
                return
        self.start = -1

    def locate_finish_pos(self):
        if self.start == -1:
            return -1

        for idx in range(self.start, len(self.rows)):
            if len(self.rows[idx]) < len(self.model.titles):
                self.end = idx
                break

        if -1 == self.end:
            self.end = len(self.rows)

    def to_model(self, row):
        return self.model.create_from_row(row)

    def read(self):

        self.locate_begin_pos()
        self.locate_finish_pos()

        bills = []

        if self.start != -1 and self.end != -1:

            for idx in range(self.start, self.end):
                bill = self.to_model(self.rows[idx])
                bills.append(bill)

        bills.reverse()
        return bills
