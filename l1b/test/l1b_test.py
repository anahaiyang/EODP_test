
from common.io.writeToa import writeToa, readToa
import numpy as np
import matplotlib.pyplot as plt

bands_list = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
toa_eq_list = []
toa_noeq_list = []
toa_ism_list = []

for band in bands_list:

    toa_eq = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1B\\myoutputs", "l1b_toa_"+ band +".nc")
    toa_noeq = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1B\\myoutputs_noeq", "l1b_toa_"+ band +".nc")
    toa_ism = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\output", "ism_toa_isrf_"+ band +".nc")

    toa_eq_list.append(toa_eq)
    toa_noeq_list.append(toa_noeq)
    toa_ism_list.append(toa_ism)

## Equalization
# VNIR-0
array0_eq = toa_eq_list[0]
toa_row_eq_0 = array0_eq[0, :]
pixels = np.arange(toa_row_eq_0.shape[0])
# VNIR-1
array1_eq = toa_eq_list[1]
toa_row_eq_1 = array1_eq[1, :]
# VNIR-2
array2_eq = toa_eq_list[2]
toa_row_eq_2 = array2_eq[2, :]
# VNIR-3
array3_eq = toa_eq_list[3]
toa_row_eq_3 = array3_eq[3, :]

# No equalization
# VNIR-0
array0_noeq = toa_noeq_list[0]
toa_row_noeq_0 = array0_noeq[0, :]
# VNIR-1
array1_noeq = toa_noeq_list[1]
toa_row_noeq_1 = array1_noeq[1, :]
# VNIR-2
array2_noeq = toa_noeq_list[2]
toa_row_noeq_2 = array2_noeq[2, :]
# VNIR-3
array3_noeq = toa_noeq_list[3]
toa_row_noeq_3 = array3_noeq[3, :]

# ISM
# VNIR-0
array0_ism = toa_ism_list[0]
toa_row_ism_0 = array0_ism[0, :]
# VNIR-1
array1_ism = toa_ism_list[1]
toa_row_ism_1 = array1_ism[1, :]
# VNIR-2
array2_ism = toa_ism_list[2]
toa_row_ism_2 = array2_ism[2, :]
# VNIR-3
array3_ism = toa_ism_list[3]
toa_row_ism_3 = array3_ism[3, :]

## PLOTS
plt.plot(pixels, toa_row_eq_0, color="blue", label="TOA L1B with eq")
plt.plot(pixels, toa_row_noeq_0, color="red", label="TOA L1B no eq")
plt.plot(pixels, toa_row_ism_0, color="green", label="TOA after the ISRF")
plt.title("Effect of the equalization for VNIR-0")
plt.xlabel("ACT pixel [-]")
plt.ylabel("TOA [mW/m2/sr]")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(pixels, toa_row_eq_1, color="blue", label="TOA L1B with eq")
plt.plot(pixels, toa_row_noeq_1, color="red", label="TOA L1B no eq")
plt.plot(pixels, toa_row_ism_1, color="green", label="TOA after the ISRF")
plt.title("Effect of the equalization for VNIR-1")
plt.xlabel("ACT pixel [-]")
plt.ylabel("TOA [mW/m2/sr]")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(pixels, toa_row_eq_2, color="blue", label="TOA L1B with eq")
plt.plot(pixels, toa_row_noeq_2, color="red", label="TOA L1B no eq")
plt.plot(pixels, toa_row_ism_2, color="green", label="TOA after the ISRF")
plt.title("Effect of the equalization for VNIR-2")
plt.xlabel("ACT pixel [-]")
plt.ylabel("TOA [mW/m2/sr]")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(pixels, toa_row_eq_3, color="blue", label="TOA L1B with eq")
plt.plot(pixels, toa_row_noeq_3, color="red", label="TOA L1B no eq")
plt.plot(pixels, toa_row_ism_3, color="green", label="TOA after the ISRF")
plt.title("Effect of the equalization for VNIR-3")
plt.xlabel("ACT pixel [-]")
plt.ylabel("TOA [mW/m2/sr]")
plt.legend()
plt.grid(True)
plt.show()
