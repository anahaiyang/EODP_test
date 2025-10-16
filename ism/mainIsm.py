
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\GITHUB_EODP\EODP_test\auxiliary'
indir = r"D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\EODP_TER_2021\EODP-TS-E2E\sgm_out" # small scene
outdir = r"D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\EODP_TER_2021\EODP-TS-E2E\myoutput_ism"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
