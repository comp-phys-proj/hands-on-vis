#!/usr/bin/env python3

from read_tmqm import read_tmqm_properties
import matplotlib.pyplot as plt

tmqm_properties = read_tmqm_properties('tmQM_y.csv','tmQM_X.xyz')

print("Available properties:",tmqm_properties.dtype.names)

plt.hist(tmqm_properties["Electronic_E"], bins=50)

plt.ylabel('Counts')
plt.xlabel('Electronic_E');

plt.show()
