#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

file = open('french.txt')
prov = file.readlines()

prov1 = random.choice(prov)
prov2 = random.choice(prov)
begin = prov1.split('@')[0].strip()
end = prov2.split('@')[1].strip()
print(begin + ' ' + end)
