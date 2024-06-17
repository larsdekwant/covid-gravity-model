# ----------------------------------------------------------------- #
# About script
# ----------------------------------------------------------------- #

# ----------------------------------------------------------------- #
# Preambule
# ----------------------------------------------------------------- #

from ClassM import ModelM
import sys

# ----------------------------------------------------------------- #
# Initialize Class
# ----------------------------------------------------------------- #

params_input = {'savename': 'High',
                'division': 100 # 5000 - 1000 - 500 - 100
                }

mobility_seed = int(sys.argv[1])

ClassM = ModelM(params_input)
ClassM.read_data()
#ClassM.mobility_matrix()

ClassM.create_people_DF()
ClassM.position_people()
ClassM.create_extra_people_DF(5)
ClassM.position_extraPeople()
#ClassM.count_people()
ClassM.save(mobility_seed)