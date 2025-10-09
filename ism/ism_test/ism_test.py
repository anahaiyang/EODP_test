
from common.io.writeToa import writeToa, readToa
import numpy as np
import matplotlib.pyplot as plt

bands_list = ['VNIR-0','VNIR-1','VNIR-2','VNIR-3']
############### OPTICAL PHASE TEST ###############
## CHECK FOR ALL BANDS THAT THE DIFFERENCES WITH RESPECT TO THE OUTPUT TOA (ism_toa_isrf) ARE <0.01% FOR AT LEAST 3-SIGMA OF THE POINTS
sigma_isrf = []
for band in bands_list:
    toa_isrf = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\output", "ism_toa_isrf_"+ band +".nc")
    mytoa_isrf = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\myoutput", "ism_toa_isrf_"+ band +".nc")

    div = toa_isrf != 0 # avoid NaN when dividing by zero
    abs_diff = np.abs((toa_isrf[div] - mytoa_isrf[div]) / toa_isrf[div])
    sigma = np.percentile(abs_diff,99.7)
    sigma_isrf.append(f"ISM_TOA_ISRF Sigma for {band} = {sigma}")
print("\n".join(sigma_isrf))

## CHECK FOR ALL BANDS THAT THE DIFFERENCES WITH RESPECT TO THE OUTPUT TOA (ism_toa_optical) ARE <0.01% FOR AT LEAST 3-SIGMA OF THE POINTS
sigma_optical = []
for band in bands_list:
    toa_optical = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\output", "ism_toa_optical_"+ band +".nc")
    mytoa_optical = readToa("D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\myoutput", "ism_toa_optical_"+ band +".nc")

    div = toa_optical != 0 # avoid NaN when dividing by zero
    abs_diff = np.abs((toa_optical[div] - mytoa_optical[div]) / toa_optical[div])
    sigma = np.percentile(abs_diff,99.7)
    sigma_optical.append(f"ISM_TOA_OPTICAL Sigma for {band} = {sigma}")
print("\n".join(sigma_optical))

## WHAT IS THE RADIANCE TO IRRADIANCE CONVERSION FACTOR FOR EACH BAND. WHAT ARE THE UNITS OF THE TOA AT THIS STAGE

from ism.src.ism import ism

auxdir = "D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\GITHUB_EODP\\EODP_test\\auxiliary"
indir = "D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\input\\gradient_alt100_act150"
outdir = "D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-ISM\\myoutput"

compute_ism = ism(auxdir, indir, outdir)
rad2irrad_factor = compute_ism.processModule()

for band in bands_list:
    print(f"Radiance to irradiance conversion factor for {band} = {rad2irrad_factor[bands_list.index(band)]}")



##############################################

############### VIDEO CHAIN PHASE TEST ###############
## CHECK FOR ALL BANDS THAT THE DIFFERENCES WITH RESPECT TO THE OUTPUT TOA (ism_toa_) ARE <0.01% FOR AT LEAST 3-SIGMA OF THE POINTS

