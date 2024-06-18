# ----------------------------------------------------------------- #
# About script
# ----------------------------------------------------------------- #

# ----------------------------------------------------------------- #
# Preambule
# ----------------------------------------------------------------- #

import sys
import resource
from ClassT import ModelT

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
n_initial_infect = 5

for interv in ['ref']:
    for seed in range(0, 20):
        for demo_group in [3]:
            for run in [0]:
                params_input = {'savename': 'High',
                                'intervention': interv,
                                'Ndays': 21 * 24,
                                'seed': seed}
                ClassT = ModelT(params_input)
                ClassT.read_model_data(initial_loc, demo_group, n_initial_infect)
                ClassT.read_empirical_data()
                ClassT.set_parameters(latent, incub, infect)
                ClassT.initialise(demo_group)
                ClassT.simulate_new()
                ClassT.save(run, demo_group, initial_loc)
                del ClassT

print('Max memory usage (in KB): ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
