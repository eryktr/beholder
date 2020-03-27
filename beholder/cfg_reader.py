from pathlib import Path
import sys


def usage():
    return ("""Usage:\n python cfg_reader.py -t (positive_number)
    path_to_file/your_config_file""")


def correct_protocol(addr):
    return addr.startswith("https://") or addr.startswith("http://")


def valid_arguments(data):
    return (len(data) == 4 and data[1] == "-t"
            and data[2].isnumeric() and not(data[2].startswith("0")))


def correct_websites(file):
    print("Checking if websites are valid...")
    lines = [line for line in file.read_text().split('\n') if line]
    errors = 0
    for addr in lines:
        if not(correct_protocol(addr)):
            if (errors == 0):
                print("---------------------------")
                print("Invalid websites:")
                print("---------------------------")
            print(addr)
            errors = errors + 1
    if (errors != 0):
        print("---------------------------")
        print("There should be protocol https:// or http://")
        print(f"Total amount of errors: {errors}")
    return errors == 0


def valid_file(config_file):
    return config_file.is_file() and correct_websites(config_file)


def check(data):
    valid = valid_arguments(data) and valid_file(Path(data[3]))
    if (not(valid_arguments(data))):
        print(usage())
    return valid


check(sys.argv)
