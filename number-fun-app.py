#!/usr/bin/env python3
# Author: Dr. Xu Chen, University of Washington

import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

st.write("""
# Gaming with numbers and controls!
Xu Chen, University of Washington
""")

st.write("""
The modulo operation, denoted as mod, returns the remainder of a division, after one number is divided by another. For example, $3 \pmod 2=1$ and $5 \pmod 3 = 2$.

We create an infinity ring by the following simple mapping starting at 0:
$x \\leftarrow (x+a) \pmod b$. 
""")

st.write("Try increase the base number $b$ and change the addition $a$. See what happens!")

ModBase = st.slider("Enter a base number", 1, 50, 5)
ModAdd = st.slider("Enter an addition number", 1, 30, 2)

st.write("$b=$", ModBase)
st.write("$a=$", ModAdd)

Ntick = ModBase
radius = 0.45

# draw circle
figure, axes = plt.subplots()
draw_circle = plt.Circle((0.5, 0.5), 0.45, fill=False)

# plt.title("Circle")
plt.axis("off")
axes.set_aspect(1)

# draw ticks
theta = np.linspace(2.5 * np.pi, np.pi / 2, Ntick + 1)
a = 0.5 + radius * np.cos(theta)
b = 0.5 + radius * np.sin(theta)
axes.plot(a, b, ".")
axes.set_xlim([0, 1])
axes.set_ylim([0, 1])

ii = 0
while True:
    iiNext = (ii + ModAdd) % ModBase
    # iiNext = (ii % ModBase + ModAdd % ModBase) % ModBase
    plt.arrow(
        a[ii],
        b[ii],
        a[iiNext] - a[ii],
        b[iiNext] - b[ii],
        head_width=0.02,
        length_includes_head="true",
    )
    if iiNext == 0:
        break
    else:
        ii = iiNext

plt.gcf().gca().add_artist(draw_circle)

figure.tight_layout()

st.write(figure)

st.write("""
Here is what happened: starting at $x=0$, the 12 o'clock position on the ring, we draw a line from $x$ (=0) to the remainder of $(x+a)/b$, or ( 0 +
""", ModAdd, ") ( mod", ModBase, ") = ", ModAdd % ModBase, """
. 
""")

st.write("The new number is then assigned to $x$, followed by the iteration: we now draw a line from",
         ModAdd % ModBase, "to (", ModAdd, "+", ModAdd % ModBase, ")  ( mod", ModBase, ")=", (ModAdd % ModBase+ModAdd) % ModBase)

st.write("The process continues until the end point is back at the 12 o'clock position.")

# %%
st.write("""
# From infinity to beyond: same ring, more patterns.
""")

st.write("""
Embracing now multiplications, we create another infinity ring by the mapping:
$y = (x \\times a) \pmod b$, where $x$ ranges from 0 to a chosen maximum. 
""")

st.write("Try increase the multiplier $a$ below and see what happens!")
st.write("As your multiplier increases, increase the base number too to make the resolution higher.")

# ModBase = st.number_input('Enter a base', 100, 500, 200)
ModBase = st.slider('Enter a base', 50, 500, 100)
ModMult = st.slider("Enter a multiplier", 1, 10)

st.write("Base", ModBase)
st.write("Multiplier", ModMult)

Ntick = ModBase
radius = 0.45

# draw circle
figure, axes = plt.subplots()
draw_circle = plt.Circle((0.5, 0.5), 0.45, fill=False)

plt.axis("off")
axes.set_aspect(1)

# draw ticks
theta = np.linspace(2.5 * np.pi, np.pi / 2, Ntick + 1)
a = 0.5 + radius * np.cos(theta)
b = 0.5 + radius * np.sin(theta)
axes.plot(a, b, ".")
axes.set_xlim([0, 1])
axes.set_ylim([0, 1])

for x in range(0, ModBase, 1):
    y = (x * ModMult) % ModBase
    plt.arrow(
        a[x],
        b[x],
        a[y] - a[x],
        b[y] - b[x],
        head_width=0.02,
        overhang=0.5,
        length_includes_head="true",
    )
    x = x + 1

plt.gcf().gca().add_artist(draw_circle)

figure.tight_layout()

st.write(figure)
