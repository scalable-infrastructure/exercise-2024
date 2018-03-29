#!/bin/bash
#SBATCH -o myjob.%j.%N.out 
#SBATCH -D .
#SBATCH -J jupyter
#SBATCH --get-user-env 
#SBATCH --clusters=mpp2
#SBATCH --nodes=1-1 
#SBATCH --cpus-per-task=28 
#SBATCH --mail-type=end 
#SBATCH --mail-user=xyz@xyz.de 
#SBATCH --export=NONE 
#SBATCH --time=08:00:00 
source /etc/profile.d/modules.sh

echo $hostname
source $HOME/anaconda2/bin/activate
jupyter-lab --no-browser