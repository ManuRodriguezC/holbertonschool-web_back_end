#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth", "password2"]
messages = ["name=egg;email=eggmin@eggsample.com;password2=asasas;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password2=asasas;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))