# Exercise SS 2019

## Jupyter Notebooks:

* Only use the Jupyter Instance assigned to you/your team!

* Naming convention: `https://data-analytics.dyndns.lrz.de:[id]/lab?`
    
* Note: We use a self signed certificate for this page. Please, verify fingerprint and allow browser exception!

* Should you prefer the execute the exercises on your local machine, we recommend the [Anaconda Python Distribution](https://www.anaconda.com/distribution/#download-section). A list of packages required is [here](conda-packages.txt).

* Fallback is to access Jupyter Notebooks is via SSH portforward - You need to have a LRZ Linux Cluster account in order to use this option:
    
        ssh -fND 4223 lxlogin10.lrz.de
       
* Set SSH Proxy in your Browser Configuration!
    
    ![socks_firefox.png](socks_firefox.png)

# Other Information

## Needed modules:
	
		module load git
		module load gcc/7
		module load java/1.8
		export TMPDIR=/tmp/$USER

* Use project directory as home is too small


## Anaconda:

* Use Project ( `pn69si`) Anaconda Installation

* Path `/naslx/projects/pn69si/mnmda001/students/software/anaconda3` 

		source /naslx/projects/pn69si/mnmda001/students/software/anaconda3/bin/activate root
## Howto Slurm:

* Show clusters

         sacctmgr list clusters

* Show Info for 1 Cluster

        sinfo --clusters=mpp3

* Show Info for default cluster
            
        sinfo
