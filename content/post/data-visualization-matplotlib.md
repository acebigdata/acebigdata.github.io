---
title: "Data Visualization Matplotlib"
date: "2017-11-02"
tags: ["data-visualization","python", "matplotlib"]
categories: ["visualization"]
menu:
  main:
    parent: Visualization
---


Following a review of basic plotting with Matplotlib, this chapter delves into
customizing plots using Matplotlib. This includes overlaying plots, making
subplots, controlling axes, adding legends and annotations, and using different
plot styles.
```ipython
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dry =[0.33,0.27,0.32,0.41,0.42,0.45,0.57,0.52,0.45,0.39,0.37,0.37]
wet = [0.66,0.72,0.67,0.58,0.57,0.54,0.42,0.47,0.54,0.60,0.62,0.62]
t = np.arange(1,13)

plt.plot(t, dry, "red")         
plt.plot(t, wet, "blue")        # Appear on the same axes

plt.xlabel("Date")

plt.title("dry vs. wet")

plt.show()
```

![](./obipy-resources/29089yax.png)
