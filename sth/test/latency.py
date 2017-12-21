# -*- coding: utf-8 -*- 
import matplotlib.pyplot as plt
import numpy 
import collections
import time
import json
import matplotlib.dates as md
import datetime
from pylab import *

# 读数据
with open('Goquery_lantency_mgetanswer_1day_pct99.json', 'r') as f:
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

# 日期转化
dates=[datetime.datetime.fromtimestamp(ts) for ts in x_plot]
datenums=md.date2num(dates)
ax=plt.gca()
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)

# 绘图
plt.plot(datenums, y_plot,'g-', label='MgetAnswer')
print datenums
xlim(datenums[0]-0.05, datenums[-1]+0.05)
plt.title("Query Service MgetAnswer Latency Pct99")
plt.xlabel("Time")
plt.ylabel("Latency (microsecond)")
plt.legend()
plt.grid(True)

plt.show()
