# Exercise SS 2021

## Software Environment:

You can either use your own laptop or the LRZ cloud for doing the exercises. Software required is Hadoop and Anaconda (incl. several different packages). You are responsible to setup your software environment.

* LRZ Cloud: <https://www.lrz.de/services/compute/cloud_en/>

* Should you prefer the execute the exercises on your local machine, we recommend the [Anaconda Python Distribution](https://www.anaconda.com/distribution/#download-section). A list of packages required is [here](conda-packages.txt).

* You will need to install the following software:

        # Hadoop
        wget https://mirrors.ae-online.de/apache/hadoop/common/hadoop-2.10.1/hadoop-2.10.1.tar.gz
        tar -xzvf hadoop-2.10.1.tar.gz

        # Anaconda Packages
        conda install -c conda-forge pyspark scikit-learn tensorflow 
        conda install torchvision pytorch -c pytorch

        # Packages only available via PyPi
        pip install transformers
        pip install git+https://github.com/facebookresearch/fastText.git # Git Version required





