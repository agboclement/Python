# rw_visual
# Created by JKChang
# 22/01/2018, 13:56
# Tag:
# Description: random walk visualization

import matplotlib.pyplot as plt

from RD_Club.Pro2.random_walk import RandomWalk

# while True:
rw = RandomWalk(2000)
rw.fill_walk()

plt.figure(dpi = 128,figsize=(10,6))
plt.title('Random Walk', fontsize=20)
color = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=color, cmap=plt.cm.Oranges, edgecolors='none', s=10)
# highlight start/ end POINTS

plt.scatter(0, 0, c='green', edgecolors='none', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=30)

# hide the axes
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

plt.savefig('resources/ramdom_walk.png', bbox_inches='tight')
plt.show()

# keep_running = input('Make another walk? (y/n): ')
# if keep_running == 'n' or keep_running == 'N':
#     break
