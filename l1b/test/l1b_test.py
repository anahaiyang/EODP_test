
from common.io.writeToa import writeToa, readToa
import numpy as np
import matplotlib.pyplot as plt

bands_list = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']

## CHECK FOR ALL BANDS THAT THE DIFFERENCES WITH RESPECT TO THE OUTPUT TOA ARE <0.01% FOR AT LEAST 3-SIGMA OF THE POINTS
for band in bands_list:
    toa_output = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1B\\output", "l1b_toa_"+ band +".nc")
    toa_eq = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1B\\myoutputs", "l1b_toa_"+ band +".nc")

    abs_diff = np.abs((toa_output-toa_eq)/toa_output)
    sigma = np.percentile(abs_diff,99.7)
    print(f"Sigma for {band} = {sigma}")

## FOR THE CENTRAL ALT POSITION, PLOT THE RESTORED SIGNAL (l1b_toa), AND THE TOA AFTER THE ISRF (ism_toa_isrf)
figure = plt.figure(figsize=(9,7))
for band in bands_list:
    toa_eq = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1B\\myoutputs", "l1b_toa_"+ band +".nc")
    toa_ism = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\output", "ism_toa_isrf_"+ band +".nc")
    toa_eq_ALT = toa_eq[50,:]
    toa_ism_ALT = toa_ism[50,:]

    # PLOTS
    plt.subplot(2, 2, bands_list.index(band)+1)
    plt.plot(toa_eq_ALT, color="blue", label="TOA L1B with eq")
    plt.plot(toa_ism_ALT, color="green", label="TOA after the ISRF")
    plt.title("Restored signal vs TOA after ISRF for "+band)
    plt.xlabel("ACT pixel [-]")
    plt.ylabel("TOA [mW/m2/sr]")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

## DO ANOTHER RUN OF THE L1B WITH THE EQUALIZATION ENABLED TO FALSE. PLOT THE RESTORED SIGNAL FOR THIS CASE
## AND FOR THE CASE WITH THE EQUALIZATION SET TO TRUE
figure = plt.figure(figsize=(11,7))
for band in bands_list:
    toa_eq = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1B\\myoutputs", "l1b_toa_"+ band +".nc")
    toa_noeq = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1B\\myoutputs_noeq", "l1b_toa_"+ band +".nc")
    toa_eq_ALT = toa_eq[50, :]
    toa_noeq_ALT = toa_noeq[50, :]

    # PLOTS
    plt.subplot(2, 2, bands_list.index(band) + 1)
    plt.plot(toa_eq_ALT, color="blue", label="TOA L1B with eq")
    plt.plot(toa_noeq_ALT, color="red", label="TOA L1B no eq")
    plt.title("TOA comparison with and without equalization for " + band)
    plt.xlabel("ACT pixel [-]")
    plt.ylabel("TOA [mW/m2/sr]")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()