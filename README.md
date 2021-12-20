# XRD/FTIR Data Processing Tool Suite
Created by Alex Pirola, Agnes Robang, Shashank Gupta, Arjun Prihar, Jordan Hamel, and Anita Zhang

## Using this Project

### Setting up the Project

From the top level directory, run `pip install -e .` to install the required python packages.

### Running the Project
The executable has 8 command line arguments: 
'python Code/driver.py -d <data_type> -m <method> -f <strategy_choice> <-t> -c <cutoff> -r <range> -s <threshold> -i <filename>'
1. `<data>` is the type of data being uploaded, either "XRD" or "FTIR".
2. `<method>` is the type of peak fitting method to be applied to the data, either "Rietveld", "Le-Bail", "Pawley", or "polyfit". Currently, only "Rietveld" and "polyfit" are fully implemented.
3. `<transmittance>` is a boolean argument, so including `-t` in the command defines it as `True`, while excluding this tag defines it as `False`. Transmittance is an option for FTIR data. 
4. `<strategy_choice>` determines the strategy in profiling and building composite models. The options for this are "fast", "random", or "best".
5. `<cutoff>` is the cutoff used for fitting (e.g. 0.9).
6. `<range>` is the peak widths range to be used for fitting (e.g. "5,15").
7. `<threshold>` is the threshold for what counts as a peak (e.g. 0.2).
8. `<inputfile>` is the filename of the input within the `Input` folder to be analyzed (e.g. "1-1-4-11_pH0_3-17-2020.csv").

So, for instance, to analyze FTIR data while considering transmittance using the Rietveld method using fast profiling with a peak threshold of 0.2, you run
`python Code/driver.py -d FTIR -m "Rietveld" -f "fast" -t -s 0.2 -i 1-1-4-11_pH0_3-17-2020.csv`

## Contributing to this Project

### Updating the Databases
If you think that either of the databases needs to be updated, run the
appropriate updating script locally on your computer and then create a
commit for the updated database. In your pull request, explain the 
reason for updating the database.

#### Updating the XRD Database
The XRD database (csv file) can be updated by running the following script
from the `/Code/scrape/` directory:
```
python scrape_xrd.py
```

#### Updating the FTIR Database
The FTIR data has to be manually updated due to the lack of the open-source documentation. The FTIR analysis data and the corresponding sample information can be added to the 'ftir_library.csv' and 'ftir_metadata.csv', respectively, in `/Code/ftir_database_generation/'` directory. From the same directory, running the script 'ftir_database.py' will update the FTIR database in '/Code/databases/' directory. 

### Python Packages
If you use a python package in the code you are writing, check `requirements.txt` and `setup.py` to see if the package is
already listed there. If not, add the name of the package to both files.

### Using the Auto-Documentation Script
To document your code, you will need to do three things:
1. Write comments that can be recognized by Sphinx, as shown in this link: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html.
2. Create a file ```docs/name_of_code_file.rst``` , as shown in this link: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/build-the-docs.html.
3. Add the name of your module to ```docs/modules.rst```.

To view the documentation on a webpage, ```cd docs``` to get to the docs directory, and run ```make html``` to auto-document existing .py files to generate a webpage with instructions. The current webpage uses the default theme.
To open the html, ```cd _build``` and type in ```open index.html```. If you are using a Windows operating system, you can also open the link through your favorite browser (ex. ```google-chrome index.html```)

If a PDF format is desired, make sure you have ```pdfTex``` installed on your machine, ```cd docs``` to get to the docs directory, and then type in ```make latexpdf``` in the command line from the docs directory. The generated pdf file will be under ```_build/latex/XRDFTIRAnalysisToolSuite.pdf```.

### Git Workflow
This section of the ReadMe outlines the git workflow that each team member will follow in order to collaboratively work on our project files. The goal is for all of us to be able to refer back to this document to responsibly upload our changes to source files, minimizing version control errors. To summarize, each feature of the project will be worked on in a seaparate branch by a single team member. With the approval of two other teammates, these features will be merged into a development branch and ultimately into the master branch:

1. Use ```git clone``` command to get the collaborative repository locally on your machine
2. Use ```git checkout main``` to make sure you're on the main branch
3. Use ```git checkout -b <your_name-name_of_feature>``` to create AND checkout a new branch
     * You should see the command-line prompt 'Switched to a new branch'
     * You can use the command: ```git log --all --decorate --oneline --graph``` to display the entire DAG and see where you are
     * You can see just the branch you're on with the command: ```git branch --show-current``` to confirm you're in the right place
4. Do your business on your branch. Right now this is only on your local machine, so do what you want. You won't mess anything up for anyone else and no one can judge you for any dum dum things you want to test out not that anyone would anyway ;)
5. When you are ready to send your work upstream:
     * Stage your files with ```git add your_filename```
     * Commit with ```git commit -m <your commit log>```
     * Do your best to make your commit log legible to more than just you :)
     * Finally push your files with ```git push origin your_name-name_of_feature (i.e. the name of the branch you created for your work)```
6. Your push will NOT automatically create a pull request - you do this manually on GitHub. If you go to the github repository in your browser, you will see this under the 'Pull request' tab (between 'Issues' and 'Actions')
     * If you click on the pull request, you should be able to see the commit history, changelogs of all the files you pushed, and a text box that allows you to leave a comment. 
     * On the right side of the webpage, you will see 'Assignees' (between 'Reviewers' and 'Labels'). Assign at least 2 other people to the pull request. These teammates will be responsible for reviewing your code and ultimately merging the changes into 'develop'. Try to make fairly regular pushes, so that the code review for your teammates is more manageable. They will ultimately decide if it is okay to be merged into the development branch. There should be no reason for command-line level merges
     * Once you've completed Step 5b, click the green button 'Create Pull Request'. NOTE: make sure the pull request correctly indicates that you want to merge into 'develop' - there is a drop-down menu in the upper left. 
7. After your pull request is approved, you can make another pull request (directly in GitHub) to merge your work into 'main.' 
8. When you want to update the files on your local machine, for example, to retrieve the work someone else has pushed to the repository, in your command prompt:
     * make sure you first switch to main with ```git checkout main```
     * Type ```git pull origin main```
