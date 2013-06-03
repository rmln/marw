This folder holds text files used to create the corpus.

HUNSPELL

Most of the words come from hunspell-sr project. You can find
it here:

https://gitorious.org/dict-sr

Download the file sr.dic and place it in ../data folder.

OTHER TEXTS

I extracted words from Serbian literature books located at
antologijasrpskeknjizevnosti.rs. I cannot distribute them with
this code due to the licensing.

Download them manually and place into ../texts in textual
format.

The database is here: 
http://srmorph.languagebits.com/database

FOLDER "PARSED"

This folder holds already parsed texts, and functions like
a cache (if not overridden by settings).

CORPUS CREATION

To create corpus, go to tools folder and issue:

$ python3 createcorpus.py

By default it will be exported to your home folder (see
PATH_EXPORT_TAR in conf.py).

Parsing logs will be saved in this folder.
