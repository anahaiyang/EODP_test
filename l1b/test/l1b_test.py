
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

array0_eq = toa_eq_list[0]
toa_row_eq_0 = array0_eq[0, :]
pixels = np.arange(toa_row_eq_0.shape[0])

array0_noeq = toa_noeq_list[0]
toa_row_noeq_0 = array0_noeq[0, :]

array0_ism = toa_ism_list[0]
toa_row_ism_0 = array0_ism[0, :]

plt.plot(pixels, toa_row_eq_0,color="blue")
plt.plot(pixels, toa_row_noeq_0,color="red")
plt.plot(pixels, toa_row_ism_0,color="green")
plt.title("VNIR-0")
plt.xlabel("ACT pixel [-]")
plt.ylabel("TOA [mW/m2/sr]")
plt.grid(True)
plt.show()
