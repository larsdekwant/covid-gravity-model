# ----------------------------------------------------------------- #
# About script
# ----------------------------------------------------------------- #

# ----------------------------------------------------------------- #
# Preambule
# ----------------------------------------------------------------- #

import numpy as np
from ClassT import ModelT
from tqdm import tqdm
import pandas as pd
import scipy.io
import matplotlib.pyplot as plt
import scipy.sparse

# ----------------------------------------------------------------- #
# Initialize Class
# ----------------------------------------------------------------- #

# Interventions:
    # 'ref'
    # 'working'
    # 'behavior'

    # 'school' 
    # 'schoolisolation'
    # 'schoolparents'
    # 'schoolextreme'

    # 'G4'
    # 'border'
    # 'local'
    # 'brablim'

for interv in ['ref']:
    for seed in [9]:
        for demo_group in range(0, 11):
            for run in range(0, 1):
                for latent in [4.6]:
                    for incub in [100]:
                        for infect in [5]:
                            #for initial_loc in range(0, 380):
                            params_input = {'savename': 'High',
                                            'intervention': interv,
                                            'Ndays': 21 * 24,
                                            'seed': seed}
                            ClassT = ModelT(params_input)
                            ClassT.read_model_data()
                            ClassT.read_empirical_data()
                            ClassT.set_parameters(latent, incub, infect)
                            ClassT.initialise(demo_group)
                            ClassT.simulate_new()
                            ClassT.save(run, demo_group)
                            del ClassT