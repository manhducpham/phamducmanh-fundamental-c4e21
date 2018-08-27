# third party library => outsources
import pyexcel
from collections import OrderedDict

# 1. Prepare data

data = [
    OrderedDict({
        'name': 'Huy',
        'age': 29,    
    }),
    OrderedDict({
        'name': 'Manh',
        'age': 24,
    }),
    OrderedDict({
        'name': 'Nam',
        'age': 24,
    }),
]

# 2. Save
# check ordereddict function
pyexcel.save_as(records = data, dest_file_name = "sample.xlsx")