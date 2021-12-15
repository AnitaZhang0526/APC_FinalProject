# APC_FinalProject
XRD/FTIR data processing tool suite. Created by Alex Pirola, Agnes Robang, Shashank Gupta, Arjun Prihar, Jordan Hamel, and Anita Zhang

## Updating the Databases
If you think that either of the databases needs to be updated, run the
appropriate updating script locally on your computer and then create a
commit for the updated database. In your pull request, explain the 
reason for updating the database.

### Updating the XRD Database
The XRD database (csv file) can be updated by running the following script
**from the `/Code/scrape/` directory**:
```
python scrape_xrd.py
```

### Updating the FTIR Database
Coming soon!

## Using the Auto-Documentation Script
Type in ```make html``` in the command line to auto-document existing .py files to generate a webpage with instructions. The current webpage uses the default theme.
To open the html, ```cd _build``` and type in ```open index.html```. If you are using a Windows operating system, you can also open the link through your favorite browser (ex. ```google-chrome index.html```)
To write comments that can be recognized by the Sphinx, follow the instructions in this link: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html.

If a PDF format is desired, make sure you have ```pdfTex``` installed on your machine, and then type in ```make latexpdf``` in the command line. The generated pdf file will be under ```_build/latex/XRDFTIRAnalysisToolSuite.pdf```.
