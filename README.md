# Access to Polish tagger via CLARIN webservice

Simple Python3 library that supports:
* posting text to CLARIN webservice
* checking status, waiting until ready (the webservice requires this, it's not as simple as post & get result as response)
* downloading the result
* parsing the output format (CCL)
* simple data structures for holding tokens and sentences
* command-line util `tagpl.py` to parse text files line-by-line and generate simple JSON files with results

The tool relies on the _tagger_ webservice made available thanks to the [CLARIN PL project](http://clarin-pl.eu/pl/tagger/).
The underlying processing is run by the [WCRFT tagger](http://nlp.pwr.wroc.pl/redmine/projects/wcrft/wiki).

This tool will work as long as the CLARIN PL webservice is on-line and it hasn't change data exchange format or any other significant assumptions.

NOTE: the tool is not suitable for tagging large texts or huge amount of texts/lines. The implementation of the webservice (upload-query-download) is not big-data-friendly.
