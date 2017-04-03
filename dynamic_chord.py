import numpy as np
import pandas as pd
import datetime
import collections
import json

# Read data
file_in = 'D:\\WorkingDocuments\\ISM\\PycharmProjects\\DashBoard\\ServiceDesk\\trails.csv'
cols = ['TICKETID', 'CHANGEDATE_TK', 'OWNERGROUP_TK']
names = ['TICKETID', 'CHANGEDATE_TK', 'OWNERGROUP_TK']
dtypes = {'TICKETID':'str', 'CHANGEDATE_TK':'str', 'OWNERGROUP_TK':'str'}
raw = pd.read_csv(file_in, encoding='cp1252', usecols=cols, dtype=dtypes, index_col=['CHANGEDATE_TK'], parse_dates=True)


# Cleaning plan
# 1. Sort data frame by CHANGEDATE_TK
raw.index = raw.index[::-1]
print(raw[1:100])


# 2. Remove datapoint row where OWNERGROUP_TK is ''
