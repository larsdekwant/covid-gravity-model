# ----------------------------------------------------------------- #
# About script
# ----------------------------------------------------------------- #

# ----------------------------------------------------------------- #
# Preambule
# ----------------------------------------------------------------- #

from ClassM import ModelM

# ----------------------------------------------------------------- #
# Initialize Class
# ----------------------------------------------------------------- #

params_input = {'savename': 'High',
                'division': 100 # 5000 - 1000 - 500 - 100
                }
ClassM = ModelM(params_input)
ClassM.read_data()
#ClassM.mobility_matrix()
for mc in [0]:
    ClassM.create_people_DF()
    ClassM.position_people()
    ClassM.create_extra_people_DF(5)
    ClassM.position_extraPeople()
    #ClassM.count_people()
    ClassM.save(mc) 