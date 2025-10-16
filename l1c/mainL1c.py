
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\GITHUB_EODP\\EODP_test\\auxiliary'
# GM dir + L1B dir
indir = r'D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1C\\input\\gm_alt100_act_150,D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1C\\input\\l1b_output'
outdir = r'D:\\MASTER UC3M\\EARTH OBSERVATION DATA PROCESSING\\EODP_TER_2021\\EODP-TS-L1C\\myoutput'

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
