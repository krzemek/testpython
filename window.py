#!/usr/bin/env python


# Zadania do wykonania test.

import os

path, dirs, files = next(os.walk("/usr/lib"))
file_count = len(files)
print("W katalogu /usr/bin jest plików: " + file_count)
