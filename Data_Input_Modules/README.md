# Data Input Modules

## Environment Setup
Before starting, run the following command in terminal:
```
pip install -r requirements.txt
```
This command will install all neceassry modules into you computational environment.

## Module Overview

### Retrieving DOIs from other metadata
This module retreives metadata records from provided author name and title metadata using Crossref's internal fuzzy matching system. It then cross-references the retreived title with the given title and returns the best one, provided it exceeds a minimum similarity threshold, currently set to '50'.

### PubMed to DOI
This module retreived DOIs from a provided PMID using PubMeds eUtils API. 

### RIS and BibTex Conversion
These modules convert RIS and BibTex modules to Pandas dataframes.

### Raw Text Parsing
This module fetches DOIs for a given formatted citation using Crossref's API.

## Running Testing Code
Run the testing.py file. The output will be 5 separate csv files output into the 'results' folder. Each of these correspond to outputs of the five different functions included in the module.

If you would like to test the code with your own dataset, feel free to modify testing.py with the appropriate file names. Please be aware of differences in column names such as 'Author' vs 'Authors', and type differences like strings vs lists.