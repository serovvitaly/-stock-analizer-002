import csv
from collections import OrderedDict


class loader:

   
    def __init__(self, file_name):
        self.data = self.load_data_from_file(file_name)


    def load_data(self, share_train=70, bars_on_chunk=10):
        items = self.load_all_data(bars_on_chunk)
        train_slice_len = int(len(items[0]) * share_train / 100)
        train_x = items[0][0:train_slice_len]
        train_y = items[1][0:train_slice_len]
        test_x  = items[0][train_slice_len:]
        test_y  = items[1][train_slice_len:]
        return (train_x, train_y), (test_x, test_y)


    def load_all_data(self, bars_on_chunk=10):
        X = []
        y = []
        chunk = []
        for bar_dt, item in self.data.items():
            chunk.append(item[0]) # open
            chunk.append(item[1]) # high
            chunk.append(item[2]) # low
            chunk.append(item[3]) # close
            chunk.append(item[4]) # vol
            if len(chunk) >= bars_on_chunk * 5:
                X.append(chunk)
                y.append([self.get_y(bar_dt, chunk)])
                chunk = []
        return X, y


    def load_data_from_file(self, file_name):
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader, None)
            by_dates = {}
            # open1,high1,low1,close1,vol1, ... openN,highN,lowN,closeN,volN,class
            for row in csv_reader:
                datetime = row[0] + row[1]
                by_dates[datetime] = (
                    float(row[2]), # open
                    float(row[3]), # high
                    float(row[4]), # low
                    float(row[5]), # close
                    int(row[6]),   # vol
                )
            by_dates = OrderedDict(sorted(by_dates.items()))
            return by_dates


    def get_y(self, bar_key, chunk):
        return 1
