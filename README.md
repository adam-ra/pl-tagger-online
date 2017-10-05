# Access to Polish tagger via CLARIN webservice

Simple Python3 library that supports:
* posting text to CLARIN webservice
* checking status, waiting until ready (the webservice requires this, it's not as simple as post & get result as response)
* downloading the result
* parsing the output format (CCL)
* simple data structures for holding tokens and sentences
* command-line util `tagpl.py` to parse text files line-by-line and generate simple JSON files with results

