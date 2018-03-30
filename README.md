# Exercise-2018

1. Needed modules:
	
		module load git
		module load gcc/7
		module load java/1.8
		export TMPDIR=/tmp/$USER

* Use project directory as home is too small


2. Anaconda:

* Use Project ( `pn69si`) Anaconda Installation

    * Path `/home/hpc/pn69si/mnmda001/software/anaconda3` 


3. Jupyter Page for Notebooks:

    * https://data-analytics.dyndns.lrz.de:1001/lab?
    * https://data-analytics.dyndns.lrz.de:1002/lab?
    
    * Note: We use a self signed certificate for this page. Please, verify fingerprint and allow browswer exception
    * [](fingerprint.png)
    
Spark

4. Howto Slurm:

    * Show clusters

             sacctmgr list clusters

    * Show Info for 1 Cluster

            sinfo --clusters=mpp3

    * Show Info for default cluster
            
            sinfo