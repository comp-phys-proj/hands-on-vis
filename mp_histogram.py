#!/usr/bin/env python3

from read_mp import read_mp_properties
import matplotlib.pyplot as plt

mp_properties = read_mp_properties('mp_data.json')

print("Available properties:",mp_properties.keys())

print([mp_properties[x][0:3] for x in mp_properties])

if "G_Reuss" in mp_properties:
    key = "G_Reuss"
else:
    key = "g_reuss"

plt.hist(mp_properties[key], bins=50)

plt.ylabel('Counts')
plt.xlabel('G_Reuss');

plt.show()
