# COVID-19 Risk mapping

This repository contains the code for the two model parts in 'Reducing societal impacts of SARS-CoV-2 interventions through subnational implementation' (https://doi.org/10.1101/2022.03.31.22273222) on the **main** branch, and the improved version for risk mapping on the **contact-heatmap** branch. This code was used for a master thesis at the Utrecht University by Lars de Kwant 'A spatio-temporal network epidemiological agent-based modelling approach for creating risk maps of viruses'.

# Data
All data required to run the model is included in the Data folder.
The data used to create the results can be requested from the authors, or generated yourself by running the model.

# Running the model
The model is made up out of two parts. The first part is run by running the \_\_MainM\_\_.py script in the MobilityModel folder, while the second part is run by running the \_\_MainT\_\_.py script in the TransmissionModel folder.
To run this code on the gemini cluster, the Data and TransmissionModel folder must be uploaded to the server (through for example a `scp` command). After that the scripts provided in the /cluster folder can be used. The `generate-jobs.ipynb` python notebook can be used to generate the job scripts to be run on the cluster. The `queue-jobs.sh` script should be run on the cluster to queue all job files into the `qsub` system on the cluster. Due to the heavy memory load of the model sometimes a job fails to complete fully (seemingly only for jobs that do not get queue'd onto the all.q@science-bs36.soliscom.uu queue), and as a result, some output files may be missing and those jobs have to be rerun.
