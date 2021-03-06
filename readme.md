# PropertySuggester-Python
Contains scripts for PropertySuggester to preprocess the wikidata dump

## usage 
- use dumpconverter.py to convert a wikidata dump to csv
- use analyzer.py to create a csv file with the suggestion data that can be loaded into a sql table
- the PropertySuggester extension provides a maintenance script (maintenance/UpdateTable.php) that allows to load the csv into the database

```
python dumpconverter.py wikidatawiki-20140226-pages-articles.xml.bz2 dump.csv
python analyzer.py dump.csv wbs_propertypairs.csv
php extensions/PropertySuggester/maintenance/UpdateTable.php wbs_propertypairs.csv
```


### install
```
sudo apt-get install build-essential python-pip python-dev
pip install -r requirements.txt
```

### run tests
```
nosetests
```

[![Build Status](https://travis-ci.org/Wikidata-lib/PropertySuggester-Python.png?branch=master)](https://travis-ci.org/Wikidata-lib/PropertySuggester-Python)
[![Coverage Status](https://coveralls.io/repos/Wikidata-lib/PropertySuggester-Python/badge.png?branch=master)](https://coveralls.io/r/Wikidata-lib/PropertySuggester-Python)


## Release Notes

### 2.0.0
* Consider classifying Properties
* use Json dumps for analysis

### 1.1
* Generate associationrules for qualifier and references
* Improve ranking to avoid suggestions of human properties
* remove very unlikely rules (<1%)

### 1.0
* Converts a wikidata dump to a csv file with associationrules between properties
