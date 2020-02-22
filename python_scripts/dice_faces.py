import numpy as np
import matplotlib.pylab as plt

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

################################################################################
# Double-slit experiment dice
################################################################################
fig = plt.figure(figsize=(9,6),dpi=100)

axes = []
for i in range(6):
    ax = fig.add_subplot(2,3,i+1)
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    ax.set(aspect="equal")
    if i<3:
        ax.set_facecolor('white')
        ax.text(0.50, 0.50, str(i%3),horizontalalignment='center',verticalalignment='center',fontsize=108, color='black', fontweight='bold')
    else:
        ax.set_facecolor('black')
        ax.text(0.50, 0.50, str(i%3),horizontalalignment='center',verticalalignment='center',fontsize=108, color='white', fontweight='bold')

plt.tight_layout()
fig.subplots_adjust(wspace=0, hspace=0)

plt.savefig('double_slit_dice.png',transparent=True)


plt.show()

