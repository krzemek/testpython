#!/usr/bin/env python


# Zadania do wykonania test.
# Zmiana 1.06
# branch test

import os


loadavg5 = os.getloadavg()[1]
print("hello")
print("Sredni loadavg z 5 min: " + str(loadavg5))

# Dodana funkcjonalnosc tylko w galezi test. Jakis tam kod, bla, bla

print(os.getlogin())