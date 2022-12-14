"""
read file csv
"""

import csv
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

FOLDER_SAVE = 'data'

class ReadFileCSV:
    """
    read file csv
    """
    """ filename + csv """
    def __init__(self, filename=None):
        if not os.path.exists(FOLDER_SAVE):
            os.mkdir(FOLDER_SAVE)
        if filename:
            self.file_name = filename
        else:
            self.file_name = 'data'
        self._file_path = os.path.join(FOLDER_SAVE, self.file_name + '.csv')


    def read_file_csv(self):
        """
        read file csv
        """
        with open(self._file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def write_file_csv(self, data, column_name=None, name_file=None):
        """
        write file csv
        """
        with open(self._file_path, 'w') as file:
            writer = csv.writer(file)
            if column_name:
                writer.writerow(column_name)
            for row in data:
                writer.writerow([row, time.time()])
                time.sleep(0.001)



