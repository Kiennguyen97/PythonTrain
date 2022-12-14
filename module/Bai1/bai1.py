"""
"Bài 1: Có 1 dãy số từ 1 -> 150000
Cần chia dãy số trên thành 3 file csv như sau:
CSV1: có dãy số từ 1->5000
CSV2: có dãy số từ 5001->10000
CSV3: có dãy số từ 10001->15000
Sử dụng python thread pool để tách các file csv trên
Python version: 3.8 trở lên

Cấu trúc của file csv như sau:
STT	Create_at
Số theo dãy số	Thời gian hiện tại
"
"""

from model import readfilecsv as csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps, update_wrapper


def split_no_thread(data, column_name, number_of_file):
    """
    It takes a dataframe, a column name, and a number of files to split the dataframe into, and returns a list of dataframes

    :param data: the dataframe that you want to split
    :param column_name: the name of the column that you want to split the data by
    :param number_of_file: the number of files you want to split the data into
    """
    start = datetime.now()
    print('start: ', start)
    [csv.ReadFileCSV(f"data{i+1}").
         write_file_csv
     (data[i*len(data)//number_of_file:(i+1)*len(data)//number_of_file], column_name)
     for i in range(number_of_file)]
    # time end
    end = datetime.now()
    print('end: ', end)


def split_with_thread(data, column_name, number_of_file):
    """
    It takes a dataframe, a column name, and a number of files to split the dataframe into, and returns a list of dataframes

    :param data: the dataframe that you want to split
    :param column_name: the name of the column that you want to split the data by
    :param number_of_file: the number of files you want to split the data into
    """
    start = datetime.now()
    print('start: ', start)
    with ThreadPoolExecutor(max_workers=number_of_file) as executor:
        futures = [executor.submit(csv.ReadFileCSV(f"data{i+1}").write_file_csv,
                                   data[i*len(data)//number_of_file:(i+1)*len(data)//number_of_file], column_name)
                   for i in range(number_of_file)]

    # time end
    end = datetime.now()
    print('end: ', end)

def bai1():
    """
    bai1
    """
    data = list(range(0, 150000))
    column_name = ['STT', 'Create_at']
    number_of_file = 3
    # split_no_thread(data, column_name, number_of_file)
    split_with_thread(data, column_name, number_of_file)





if __name__ == '__main__':
    # bai1()
    # bai2()



    # partial functions
    pow2 = partial(power, b=2)
    pow4 = partial(power, b=4)
    power_of_5 = partial(power, 5)

    print(power(2, 3))
    print(pow2(4))
    print(pow4(3))
    print(power_of_5(2))
