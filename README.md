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
From the ```docs``` folder, run ```make html``` in the command line to auto-document existing .py files to generate a webpage with instructions. The current webpage uses the default theme.
To open the html in your web browser, type ```open _build/html/index.html```. If you are using a Windows operating system, you can also open the link through your favorite browser (ex. ```google-chrome index.html```)

To document your code, you will need to do three things:
1. Write comments that can be recognized by Sphinx, as shown in this link: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html.
2. Create a file ```docs/name_of_code_file.rst``` , as shown in this link: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/build-the-docs.html.
3. Add the name of your module to ```docs/modules.rst```.
