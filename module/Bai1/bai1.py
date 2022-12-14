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


if __name__ == '__main__':
    # time start
    start = csv.time.time()
    print('start: ', start)

    """ data from 1 -> 150000 """
    data = [i for i in range(0, 150000)]
    """ split data to 3 list """
    data1 = data[0:5000]
    data2 = data[5001:10000]
    data3 = data[10001:15000]

    """ write data to csv file """
    csv1 = csv.ReadFileCSV(filename='data1')
    csv1.write_file_csv(data1, column_name=['STT', 'Create_at'])
    csv2 = csv.ReadFileCSV(filename='data2')
    csv2.write_file_csv(data2, column_name=['STT', 'Create_at'])
    csv3 = csv.ReadFileCSV(filename='data3')
    csv3.write_file_csv(data3, column_name=['STT', 'Create_at'])

    # time end
    end = csv.time.time()
    """ time run to mini second """
    duration = (end - start) * 1000
    print('end: ', end)