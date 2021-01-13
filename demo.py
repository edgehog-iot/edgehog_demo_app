import os


def file_check(path):
    print("Checking {}...".format(path), end='')
    if os.path.exists(path) and os.path.isfile(path):
        print("SUCCESS")
    else:
        print("FAIL")
