#!/bin/bash

#exit the job if there is something wrong with /scratch
cd /scratch || exit
mkdir -p 6958680 || exit
cd 6958680 || exit

echo "Copying model to /scratch..."

#recursively copy all the project files from homedir to node /scratch/solisid
rsync -r --info=progress2 /nethome/6958680/src .
cd src/TransmissionModel

echo "Installing requirements"
pip install -r requirements.txt


echo "Running models..."
for i in {96..111} ; do
  python3 __MainT__.py $i &
done

wait

echo "Completed models, copying results to /nethome/solisid..."

cd ..
cd Data
rsync -r --info=progress2 ./Model_V1/Data/High /nethome/6958680/results/1

echo "Done..."
#end of job