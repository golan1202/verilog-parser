from compare_csv_verilog import extract_files, dict_diff
from data_from_csv import parse_from_csv
from parse_to_file import parse_to_dict, dict_to_file


# 0.  Important note - The extension of Verilog file should be '.v' and for csv file '.csv'
#     For the tests i am using 3 files:
#     The first exist, the second will be created and the third has taken from the previous with changes
verilog_file = "verilog_files/adder_explicit.v"
csv_file = 'csv_files/ports.csv'
csv_file_changed = 'csv_files/ports_changed.csv'

# 1.  Parse a Verilog file and extract its ports to a dictionary database
data = parse_to_dict(verilog_file)
print(f'Ports of verilog file  "{verilog_file}":\n {data}')

# 2.  Generate an Excel file with the following data per port
dict_to_file(data, csv_file)

# 3.  Extracting data from a CSV file(Excel file) after changes have been made
data = parse_from_csv(csv_file_changed)
print(f'\nThe extract data from file "{csv_file_changed}":\n {data}')

# 4.  Comparing a verilog file to an existing excel and reporting which ports changed
data_csv, data_verilog = extract_files(csv_file_changed, verilog_file)
diff = dict_diff(data_csv, data_verilog)
if diff == 0:
    print("\nThere is no difference. The ports are the same!!!")
else:
    print(f'\nThe difference between the two files:\n "{diff[0]}" \nDifferent values to those ports: \n {diff[1]}')

