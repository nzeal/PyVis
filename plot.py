import matplotlib.pyplot as plt
import numpy as np
import glob
import math

plt.figure(figsize=(12, 8))
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.yticks(np.arange(0.0, 70.0, 10.0))
plt.title("OSU-benchmark on Marconi 100", loc="left", fontsize=20)
plt.xlabel(r"Message size (bytes)", size=20)
plt.ylabel(r"Bandwidth (GB/s)", size=20)
plt.legend(loc=1, bbox_to_anchor=(1.015, 1.03), prop={"size": 12})
plt.grid(linestyle="--")


for files in glob.glob('*.out'):
	print(files)

	with open(files) as f:
		x, y = np.loadtxt(f, dtype="float", comments="#", skiprows=13, unpack=True)
		plt.semilogx(x, y / 1024.0, "o-")
		plt.legend(['total nodes: 1; tasks per node: 2 cpus per task: 16', 
					'total nodes: 1; tasks per node: 4 cpus per task: 8', 
					'total nodes: 1; tasks per node: 8 cpus per task: 4', 
					'total nodes: 1; tasks per node: 16 cpus per task: 2', 
					'total nodes: 1; tasks per node: 32 cpus per task: 1'])
#plt.show()
plt.savefig("m100_OSU.png")
