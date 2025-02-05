from cProfile import label
from pickle import APPEND
from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def path_square(x,y):
    lx, ly = 1, 1
    xr = float(x) - lx/2
    yr = float(y) - ly/2
    p = patches.Rectangle((xr, yr), lx, ly, linewidth=0, edgecolor="black", facecolor="black")
    return p
def distance_to_cicle(p, q):
    x = np.zeros(len(q[0]))
    y = np.zeros(len(q[0]))
    for i in range(len(q[0])):
        for j in range(len(p[0])):
            d = np.sqrt((p[0][j] - q[0][i])**2 + (p[1][j] - q[1][i])**2)
            if(d <= 2):
                x[i] = q[0][i]
                y[i] = q[1][i]
                break
    return x, y

# SIMU A) s1   20 17
# SIMU B) s18  -2 80
df = pd.read_csv(f'datapose-s1-{21}-{18}-fa0.3-fr0.6.csv', delimiter=',')
x = df['x'].to_numpy()
y = df['y'].to_numpy()
s = df['s'].to_numpy()

pose = [[round(x[0]), round(y[0])], [round(x[-1]), round(y[-1])]]

y_fis = y[s == 1]
x_fis = x[s == 1]

y_fpa = y[s == 0]
x_fpa = x[s == 0]

fig, ax = plt.subplots()

xo = ['2.48639', '4.49723', '7.54201', '1.55461', '5.46835', '10.9623', '15.1737', '17.872', '18.816', '11.0321', '8.25934', '11.6691', '8.91221', '2.94851', '7.19557', '13.0949', '12.4967']
yo = ['2.52913', '-0.544255', '2.47525', '7.46992', '7.49662', '5.51946', '6.91589', '4.03057', '11.4136', '8.92808', '10.5307', '2.13023', '-2.90968', '12.3713', '14.9949', '12.2376', '16.9632']
xo = np.float_(xo)
yo = np.float_(yo)

pilar = []
for i in range(len(xo)):
    pilar.append(path_square(float(xo[i]), float(yo[i])))

for p in pilar:
    ax.add_patch(p)



# PLOT

plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")
plt.xticks(np.arange(-5, 22, 5))
plt.yticks(np.arange(-5, 25, 5))
# plt.grid()
lw = 2
k = 0.7

# plt.xlim([min([pose[0][0], pose[1][0]]) - 2, max([pose[0][0], pose[1][0]]) + 2])
# plt.ylim([min([pose[0][1], pose[1][1]]) - 2, max([pose[0][1], pose[1][1]]) + 2])
plt.xlim([-3, 22])
plt.ylim([-4, 21])


s_size = 5
# plt.plot(x,y)
plt.scatter(x_fpa, y_fpa, s=s_size, label="APF-A")
plt.scatter(x_fis, y_fis, s=s_size, label="FIS-M")
plt.scatter(pose[0][0], pose[0][1], c="black", s=100)
plt.scatter(pose[1][0], pose[1][1], c="black", s=100)

ptext = 0.6
plt.text(pose[0][0] - ptext, pose[0][1] - 2*ptext, "INICIO", fontsize=9)
plt.text(pose[1][0]-ptext, pose[1][1] - 2.2*ptext, "FIM", fontsize=9)
plt.legend(markerscale=2.5, scatterpoints=1, fontsize=10, loc="upper left")


plt.rcParams["figure.figsize"] = (6,6)
plt.subplots_adjust(left=0.1, right=0.9, top=0.98, bottom=0.1)
plt.savefig(f'simu({pose[1][0]}:{pose[1][1]}).png', format='png')
plt.show()
# plt.gcf().autofmt_xdate()


