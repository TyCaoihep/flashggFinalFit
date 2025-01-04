# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/afs/cern.ch/user/t/ticao/higgsdna_new/HiggsDNA/output_data/root/Data/ws', # location of 'allData.root' file
  #'inputWS':'/afs/cern.ch/user/t/ticao/higgsdna_new/HiggsDNA/output_data/root/Data/ws/allData_2022postEE.root', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'data_test', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'hep.q' # for condor e.g. microcentury
  
}
