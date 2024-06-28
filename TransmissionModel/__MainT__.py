# ----------------------------------------------------------------- #
# About script
# ----------------------------------------------------------------- #

# ----------------------------------------------------------------- #
# Preambule
# ----------------------------------------------------------------- #

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

for interv in ['behavior']:
    for run in [0]:
        for seed in [1]:
            for latent in [4.6]:
                for incub in [3]:
                    for infect in [5]:
                        params_input = {'savename': 'High',
                                        'intervention': interv,
                                        'Ndays': 120 * 24,
                                        'seed': seed}
                        ClassT = ModelT(params_input)
                        ClassT.read_model_data()
                        ClassT.read_empirical_data()
                        ClassT.set_parameters(latent, incub, infect)
                        ClassT.initialise()
                        ClassT.simulate_new()
                        ClassT.save(run)
                        del ClassT