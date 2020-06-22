import hdlparse.verilog_parser as vlog  # Hdlparse is a simple package implementing a parser for VHDL and Verilog.
import csv
import os
import sys

# Parsing a Verilog file and extracting its ports to a dictionary database
# Dictionary build like so: key - port , value - mode and data_type


def parse_to_dict(fname):
    if os.path.exists(fname) and os.stat(fname).st_size != 0 and fname.endswith('.v'):
        vlog_ex = vlog.VerilogExtractor()
        with open(fname, 'r') as fh:
            code = fh.read()
        vlog_mods = vlog_ex.extract_objects_from_source(code)
        dict_ports = dict()
        for m in vlog_mods:
            for p in m.ports:
                dict_ports[p.name] = [p.mode, p.data_type]
        return dict_ports
    else:
        print("\nError in File: '%s'" % fname)
        sys.exit("File does not exist OR is empty OR wrong extension")


def dict_to_file(dict, fname):
    with open(fname, mode='w') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerow(['port name', 'port mode', 'port data_type'])
        for key, value in dict.items():
            writer.writerow([key] + value)

