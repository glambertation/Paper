# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt
import numpy 
import collections
import time
import json

# 读数据
with open('small_data.json', 'r') as f:
        data = json.load(f)
core_data = data["dps"]
print core_data

# sort
a = collections.OrderedDict()
for k,v in core_data.items():
    k = int (k)
    a[k] = v
a = collections.OrderedDict(sorted(a.items(), key=lambda t: t[0]))

# 绘制图形
x_plot = []
y_plot = []
for k,v in a.items():
    x_plot.append(k)
    y_plot.append(v)

print x_plot
print y_plot
plt.plot(x_plot, y_plot)
plt.show()


