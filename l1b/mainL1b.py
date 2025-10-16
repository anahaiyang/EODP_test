
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\GITHUB_EODP\EODP_test\auxiliary'
indir = r"D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\EODP_TER_2021\EODP-TS-E2E\myoutput_ism"
outdir = r"D:\MASTER UC3M\EARTH OBSERVATION DATA PROCESSING\EODP_TER_2021\EODP-TS-E2E\myoutputs_noeq_l1b"

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
