from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from time import sleep
print("=============start=============", end='\n')
for id in range(100):
        num = '{0:03}'.format(id)
        print("TD"+num)

