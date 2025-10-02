import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from labellines import labelLines

low_rpm = 10
high_rpm = 2000

low_diameter = 10
high_diameter = 200

surf_speeds = np.array([50, 100, 150, 200, 250, 300])

spindle_rpm = np.linspace(low_rpm, high_rpm, 100)
fig, ax = plt.subplots(figsize=((297 - 20) / 25.4, (210 - 20) / 25.4))

ax.set_xlim(0, high_rpm)
ax.set_ylim(0, high_diameter)

ax.xaxis.set_major_locator(MultipleLocator(200))
ax.xaxis.set_minor_locator(MultipleLocator(50))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.tick_params(which="major", direction="inout", length=10, width=1.5)
ax.tick_params(which="minor", direction="out", length=3, width=0.75)

ax.grid(True, linewidth=1.5)
ax.grid(True, which="minor", linewidth=0.75)

ax.set_xlabel(r"RPM [$min^{-1}$]")
ax.set_ylabel(r"Diameter [$mm$]")

for speed in surf_speeds:
    diameter = speed * 1000 / (spindle_rpm * np.pi)
    ax.plot(spindle_rpm, diameter, color="black", label=speed)

labelLines(ax.get_lines(), zorder=50)

plt.figtext(0.25, 0.06, "Recommended speeds:", wrap=True, horizontalalignment="left", fontsize=10)
plt.figtext(0.43, 0.06, "Aluminium 150-250 m/min", wrap=True, horizontalalignment="left", fontsize=10)
plt.figtext(0.63, 0.06, "Steel 90-150 m/min", wrap=True, horizontalalignment="left", fontsize=10)
plt.figtext(0.43, 0.04, "Stainless steel 45-75 m/min", wrap=True, horizontalalignment="left", fontsize=10)
plt.figtext(0.63, 0.04, "Brass 120-250 m/min", wrap=True, horizontalalignment="left", fontsize=10)

plt.tight_layout(rect=(0, 0.06, 1, 1))
# plt.show()
plt.savefig("graph.pdf")
