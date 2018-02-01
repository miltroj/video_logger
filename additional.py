import datetime
import time
import os

def date_time_file():
    return str(datetime.datetime.now().strftime("%Y-%m-%d"))

def date_time():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H;%M;%S"))

def split_path(path):
    print "%r" %path.rsplit('/',1)
    return path.rsplit('/',1)

def chose_path(path):
    print "Path przed %r" %path
    path = path.rsplit('/',1)[0]
    print "Path %r" %path
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == "__main__":
    path =  'screens/scr_'

    f1,f2 = split_path(path)

    print f1
    print f2
