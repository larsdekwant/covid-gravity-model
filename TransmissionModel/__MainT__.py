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
    for run in [3, 4, 5, 6, 7, 8, 9, 10]:
        for seed in [2]:
            params_input = {'savename': 'High',
                            'intervention': interv,
                            'Ndays': 120 * 24,
                            'seed': seed}
            ClassT = ModelT(params_input)
            ClassT.read_model_data()
            ClassT.read_empirical_data()
            ClassT.set_parameters(run)
            ClassT.initialise()
            ClassT.simulate_new()
            ClassT.save(run)
            del ClassT