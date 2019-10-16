#/bin/env python3

import os
import sys
import uuid

def main():
    fname = "blob-%s.bin" % uuid.uuid4() 
    with open(fname, 'wb') as fp:
        fp.write(os.urandom(1024*1024*10))

if __name__ == "__main__":
    main()

