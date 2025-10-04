
from common.io.writeToa import writeToa, readToa
import numpy as np
import matplotlib.pyplot as plt

bands_list = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']

## CHECK FOR ALL BANDS THAT THE DIFFERENCES WITH RESPECT TO THE OUTPUT TOA ARE <0.01% FOR AT LEAST 3-SIGMA OF THE POINTS
for band in bands_list:
    toa_output = readToa("D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_"+ band +".nc")
    my_toa = readToa("D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\EODP_TER_2021\EODP-TS-ISM\myoutput", "ism_toa_isrf_"+ band +".nc")

    abs_diff = np.abs((toa_output-my_toa)/toa_output)
    sigma = np.percentile(abs_diff,99.7)
    print(f"Sigma for {band} = {sigma}")