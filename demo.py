import os


def file_check(path):
    print("Checking {}...".format(path), end='')
    if os.path.exists(path) and os.path.isfile(path):
        print("SUCCESS")
        with open(path) as fp:
            for line in fp:
                print(line.strip())
    else:
        print("FAIL")
