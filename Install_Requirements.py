import os
from time import sleep


def install():
  os.system("clear")
  os.system("pip install art==5.9")
  os.system("clear")
  print("Quitting")
  sleep(1)
  quit()


i = input("Install Requirements? (y/n)")

if i.capitalize() == "Y":
  install()
else:
  print("Quitting")
  sleep(1)
  quit()
