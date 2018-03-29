#!/bin/bash
#SBATCH -o myjob.%j.%N.out 
#SBATCH -D .
#SBATCH -J hello
#SBATCH --get-user-env 
#SBATCH --clusters=mpp3
#SBATCH --mail-type=end 
#SBATCH --mail-user=xyz@xyz.de 
#SBATCH --export=NONE 
#SBATCH --time=00:05:00 
source /etc/profile.d/modules.sh

