# Config file: options for signal fitting

_year = '2022postEE'

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/afs/cern.ch/user/t/ticao/higgsdna_new/HiggsDNA/output_bbgg_M-1000/root/GluGlutoRadiontoHHto2B2G_M-1000/ws_gghh',
  'procs':'gghh', # if auto: inferred automatically from filenames
  'cats':'boosted', # if auto: inferred automatically from (0) workspace
  'ext':'%s_boosted_M1000_test'%_year,
  'analysis':'STXS', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  'massPoints':'125',

  #Photon shape systematics  
  'scales':'', # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'', # affect all processes equally, correlated across years
  'smears':'', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'hep.q'
  #'batch':'condor', # ['condor','SGE','IC','local']
  #'queue':'espresso',

}
