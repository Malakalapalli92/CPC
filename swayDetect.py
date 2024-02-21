import cv2
from matplotlib import pyplot as plt
import pandas as pd

df1=pd.read_csv("E:\\CPC data\\20_12_22\\Left1.csv")
df2=pd.read_csv("E:\\CPC data\\20_12_22\\Right1.csv")

plt.plot(df1)
plt.plot(df2)
plt.show()