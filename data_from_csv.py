import csv
import os
import sys


def parse_from_csv(fname):
    if os.path.exists(fname) and os.stat(fname).st_size != 0 and fname.endswith('.csv'):
        with open(fname) as f:
            data = dict()
            try:
                reader = csv.reader(f, delimiter=',')
                next(reader)  # skip the header row
                for line in reader:
                    data[line[0]] = [line[1], line[2]]
                return data

            except IndexError:
                print("\nError in File: '%s'" % fname)
                sys.exit("IndexError: Must be in this pattern: port name,port mode,port data_type")
    else:
        print("\nError in File: '%s'" % fname)
        sys.exit("File does not exist OR is empty OR wrong extension")




