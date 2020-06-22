from data_from_csv import parse_from_csv
from parse_to_file import parse_to_dict


def extract_files(csv_file, verilog_file):
    data_csv = parse_from_csv(csv_file)
    data_verilog = parse_to_dict(verilog_file)
    return data_csv, data_verilog


def dict_diff(left, right):
    diff = dict()
    changes = dict()
    diff['variables only in file-1'] = set(left) - set(right)
    diff['variables only in file-2'] = set(right) - set(left)
    diff['different values in the same variable'] = {k for k in set(left) & set(right) if left[k] != right[k]}
    if any(v for v in diff if diff[v] != set()):
        if diff['variables only in file-1'] == set():
            diff['variables only in file-1'] = "None"
        if diff['variables only in file-2'] == set():
            diff['variables only in file-2'] = "None"
        for value in diff['different values in the same variable']:
            changes[value] = [left.get(value), right.get(value)]
        return [diff, changes]
    else:
        return 0







