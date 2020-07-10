import matplotlib.pyplot as plt
import numpy as np

import math

files = ["Job_406858.out", "Job_406859.out", "Job_406860.out", "Job_406861.out", "Job_406862.out"]
lab = ["Label1", "Label2", "Label3", "Label4", "Label5"]
#col = ["r", "g", "b", "c", "k"]

plt.figure(figsize=(12, 8))

for fil, label in zip(files, lab):
    print(fil)

    with open(fil) as f:
        x, y = np.loadtxt(f, dtype="float", comments="#", skiprows=13, unpack=True)

    plt.xticks(fontsize=16)
    # plt.xticks(np.arange(0.0, 800.0, 100.0))
    plt.yticks(fontsize=16)
    plt.yticks(np.arange(0.0, 70.0, 10.0))
    plt.plot(x, y / 1024.0, ms=6.0, label=label)

    plt.title("CPU-Stream test at Marconi 100", loc="left", fontsize=20)
    plt.xlabel(r"Message size (bytes)", size=20)
    plt.ylabel(r"Bandwidth (GB/s)", size=20)
    plt.legend(loc=1, bbox_to_anchor=(1.015, 1.03), prop={"size": 12})
    plt.grid(linestyle="--")


plt.show()
# plt.savefig("m100stream_cpu_.png")
