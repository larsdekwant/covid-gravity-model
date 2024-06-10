# ----------------------------------------------------------------- #
# About script
# ----------------------------------------------------------------- #

# ----------------------------------------------------------------- #
# Preambule
# ----------------------------------------------------------------- #

import numpy as np
import sys
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

# some parameters
initial_loc = int(sys.argv[1])
latent = 4.6
incub = 100
infect = 5

for interv in ['ref']:
    for seed in [11]:
        for demo_group in [3]:
            for run in range(0, 10):
                params_input = {'savename': 'High',
                                'intervention': interv,
                                'Ndays': 21 * 24,
                                'seed': seed}
                ClassT = ModelT(params_input)
                ClassT.read_model_data(initial_loc, demo_group)
                ClassT.read_empirical_data(initial_loc, n_infected=10)
                ClassT.set_parameters(latent, incub, infect)
                ClassT.initialise(demo_group)
                ClassT.simulate_new()
                ClassT.save(run, demo_group, initial_loc)
                del ClassT