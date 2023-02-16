import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image

#importar o arquivo a ser analisado
img_file = Image.open("milho.jpg")
img = img_file.load()


[xs, ys] = img_file.size
max_intensity = 100
hues = {}

for x in range(0, xs):
    for y in range(0, ys):
        [r, g, b] = img[x, y]
        r /= 255.0
        g /= 255.0
        b /= 255.0

        [h, s, v] = colorsys.rgb_to_hsv(r, g, b)

        if h not in hues:
            hues[h] = {}
        if v not in hues[h]:
            hues[h][v] = 1
        else:
            if hues[h][v] < max_intensity:
                hues[h][v] +=1

h_ = []
v_ = []
i = []
colours = []

for h in hues:
  for v in hues[h]:
    h_.append(h)
    v_.append(v)
    i.append(hues[h][v])
    [r, g, b] = colorsys.hsv_to_rgb(h, 1, v)
    colours.append([r, g, b])

fig = plt.figure()
ax = p3.Axes3D(fig)
ax.scatter(h_, v_, i, s=5, c=colours, lw=0)

ax.set_xlabel('Matiz')
ax.set_ylabel('Valor')
ax.set_zlabel('Intensidade')
fig.add_axes(ax)
plt.show()