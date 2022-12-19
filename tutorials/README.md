# How to run the PuMA tutorial
This folder contains notebook tutorial that show the basic workings of PuMA and pumapy. 

## Python Tutorials (pumapy)
There are three ways to run the pumapy tutorials: 
1. Running the jupyter notebooks on Binder
1. Running the python tutorial scripts (.py files) locally
1. Running the jupyter notebooks locally


### Run online in Binder
You can run the Jupyter notebook tutorials online on Binder using the link below.  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/jcfergus%2Fpuma-dev/main)


### Run Jupyter Notebooks locally
In order to run the notebooks locally, you must have downloaded the PuMA repository to your computer. 
If you did not install from source, you will have to install the following extra dependencies into the conda environment as: 

    conda activate puma
    conda install -c conda-forge jupyterlab ipympl ipyvtklink

On the other hand, if you installed puma by running "./installer.sh", then these dependencies are already part of the puma environment. 

To follow the tutorial, open a terminal, navigate into the puma/tutorials/python/jupyter_notebooks folder and run:

    conda activate puma
    jupyter lab
    
If you installed the software using conda, then you will have to download the jupyter notebook files
(contained in the puma/tutorials/python/jupyter_notebooks folder) from the puma gitlab or puma github. 


### Run Python Scripts locally
The pumapy tutorials can also be run directly as python scripts. The advantage of this format is that the tutorials can 
serve as templates for creating python scripts for your own simulation needs. 

To run the python tutorials, navigate in a terminal to the puma/tutorials/python/python_scripts folder. 
From here, you can run the tutorials direclty in python (remember to first activate the puma conda environment). 

As an example, execute the following to run the visualization tutorial: 

    conda activate puma
    python visualization_tutorial.py


## C++ PuMA tutorials
The C++ code is typically interfaced using the pumaGUI. To launch the PuMA GUI after installation, 
execute the following in a terminal: 

    conda activate puma
    pumaGUI
    
The C++ code can also be used by importing the C++ library into a project and directly calling the C++ API. 
A starting code snippet already linked to PuMA can be seen in the puma/tutorials/cpp/init_project folder. 
This includes a CMakeLists, a bash script, and a .cpp file, which are the only files needed to compile a project 
linked to the PuMA API. 

Finally, we also included a set of tutorials scripts for the C++ library, which can only be run locally and 
are stored inside puma/tutorials/cpp/examples.
Each of the puma tutorials is run in a similar way: open a terminal, activate the puma conda environment, navigate 
to the puma/tutorials/cpp folder, run the make_run_example.sh script. 
As an example, the following will run the import_export tutorial: 

    conda activate puma
    cd tutorials/cpp
    ./make_run_example.sh import_export

Note that the name of the file after make_run_example.sh should not include the .cpp extension and has to match one of 
the files inside the puma/tutorials/cpp/examples folder.


----------------- Disclaimer: -----------------

THE SOFTWARE AND/OR TECHNICAL DATA ARE PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SOFTWARE AND/OR TECHNICAL DATA WILL CONFORM TO  SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR FREEDOM FROM  INFRINGEMENT, ANY WARRANTY THAT THE SOFTWARE AND/OR TECHNICAL DATA WILL BE ERROR FREE, OR ANY WARRANTY THAT  TECHNICAL DATA, IF PROVIDED, WILL CONFORM TO THE SOFTWARE.  IN NO EVENT SHALL THE UNITED STATES GOVERNMENT, OR ITS  CONTRACTORS OR SUBCONTRACTORS, BE LIABLE FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED TO, DIRECT, INDIRECT, SPECIAL OR  CONSEQUENTIAL DAMAGES, ARISING OUT OF, RESULTING FROM, OR IN ANY WAY CONNECTED WITH THIS SOFTWARE AND/OR TECHNICAL DATA, WHETHER OR NOT BASED UPON WARRANTY, CONTRACT, TORT, OR OTHERWISE, WHETHER OR NOT INJURY WAS SUSTAINED BY PERSONS OR  PROPERTY OR OTHERWISE, AND WHETHER OR NOT LOSS WAS SUSTAINED FROM, OR AROSE OUT OF THE RESULTS OF, OR USE OF, THE SOFTWARE AND/OR TECHNICAL DATA.
THE UNITED STATES GOVERNMENT DISCLAIMS ALL WARRANTIES AND LIABILITIES REGARDING THIRD PARTY COMPUTER SOFTWARE,  DATA, OR DOCUMENTATION, IF  SAID THIRD PARTY COMPUTER SOFTWARE, DATA, OR DOCUMENTATION IS PRESENT IN THE NASA SOFTWARE  AND/OR TECHNICAL DATA, AND DISTRIBUTES IT "AS IS."
RECIPIENT AGREES TO WAIVE ANY AND ALL CLAIMS AGAINST THE UNITED STATES GOVERNMENT AND ITS CONTRACTORS AND  SUBCONTRACTORS, AND SHALL INDEMNIFY AND HOLD HARMLESS THE UNITED STATES GOVERNMENT AND ITS CONTRACTORS AND  SUBCONTRACTORS FOR ANY LIABILITIES, DEMANDS, DAMAGES, EXPENSES OR LOSSES THAT MAY ARISE FROM RECIPIENT'S USE OF THE SOFTWARE AND/OR TECHNICAL DATA, INCLUDING ANY DAMAGES FROM PRODUCTS BASED ON, OR RESULTING FROM, THE USE THEREOF.
IF RECIPIENT FURTHER RELEASES OR DISTRIBUTES THE NASA SOFTWARE AND/OR TECHNICAL DATA, RECIPIENT AGREES TO OBTAIN THIS IDENTICAL WAIVER OF CLAIMS, INDEMNIFICATION AND HOLD HARMLESS AGREEMENT WITH ANY ENTITIES THAT ARE PROVIDED WITH THE SOFTWARE  AND/OR TECHNICAL DATA.
