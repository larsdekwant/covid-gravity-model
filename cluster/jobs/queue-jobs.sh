#!/bin/bash

for i in {0..23} ; do
  # running dos2unix is required if the jobs are created on a Windows system.
  dos2unix job$i.sh
  qsub -q all.q -l h_rt=23:59:00 -l h_vmem=16G -r y -pe mpich 16 job$i.sh
done