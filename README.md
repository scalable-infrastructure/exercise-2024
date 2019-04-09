# Exercise SS 2019

## Jupyter Notebooks:

* Only use the Jupyter Instance assigned to you/your team!

* Naming convention: `https://data-analytics.dyndns.lrz.de:17[id]/lab?`
    
* Note: We use a self signed certificate for this page. Please, verify fingerprint and allow browser exception!

![fingerprint.png](fingerprint.png)
    


* Fallback is to access Jupyter Notebooks is via SSH portforward:
    
        ssh -fND 4223 lxlogin8.lrz.de
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
