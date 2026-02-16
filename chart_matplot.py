import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.array([10, 25, 40, 30, 50])

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)