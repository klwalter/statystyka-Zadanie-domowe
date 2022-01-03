import json as js
import matplotlib.pyplot as plt
import numpy as np


results = js.load(open('results.js', mode='r'))
print(results[5][0])
