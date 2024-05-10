# Data Input Modules
### Contributors
- Shashank Kambhatla (Code, research and testing)
- Hannah Smith (Advice, testing)
- Yuanxi Fu (Advice, testing)
- Jodi Schneider (Mentor)

## Environment Setup
Before starting, run the following command in terminal:
```
pip install -r requirements.txt
```
This command will install all neceassry modules into you computational environment.

## File structure overview
- "Results" folder: Folder where results from tests will appear
- "csv-Calcitonin-set-filtered": Default CSV file used in the testing scripts
- "inputmodules.py": Python file with reusable modules as detailed in the "module overview" section
- "testing.py": Python file running programatic tests on the modules in "inputmodules.py"
- "Salt_SRR.bib/.ris": .bib and .ris files used in tests

## Module Overview

### Retrieving DOIs from other metadata
This module retreives metadata records from provided author name and title metadata using Crossref's internal fuzzy matching system. It then cross-references the retreived title with the given title and returns the best one, provided it exceeds a minimum similarity threshold, currently set to '50'.
- Expected input: Auhtor title and name
- Expected output: DOI or "Not Found"

### PubMed to DOI
This module retreived DOIs from a provided PMID using PubMeds eUtils API. 
- Expected input: PubMed PMID
- Expected output: DOI or "Not Found"

<<<<<<< Updated upstream
### RIS and BibTeX Conversion
These modules convert RIS and BibTeX modules to Pandas dataframes.
=======
### RIS and BibTex Conversion
These modules convert RIS and BibTex modules to Pandas dataframes.
- Expected input: .bib or .ris file
- Expected output: Pandas dataframe
>>>>>>> Stashed changes

### Raw Text Parsing
This module fetches DOIs for a given formatted citation using Crossref's API.
- Expected input: Formatted citation as a string (i,e, APA style citation)
- Expected output: DOI or "Not Found"

## Running Testing Code
Run the testing.py file. The output will be 5 separate csv files output into the 'results' folder. Each of these correspond to outputs of the five different functions included in the module.

<<<<<<< Updated upstream
If you would like to test the code with your own dataset, feel free to modify testing.py with the appropriate file names. Please be aware of differences in column names such as 'Author' vs 'Authors', and type differences like strings vs lists.
=======
If you would like to test the code with your own dataset, feel free to modify testing.py with the appropriate file names. Most notably, the current testing file is designed to work with the "first author" column as featured in the testing dataset. Please make sure your dataset has such a column. If your dataset does not, extract the first author in a list of names, or use the singular provided name in your dataset. Please be aware of differences in column names such as 'Author' vs 'Authors', and type differences like strings vs lists.
>>>>>>> Stashed changes
