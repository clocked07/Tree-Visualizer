# Tree Analyzer

This tool generates dependency trees of sentences from a structure specified in a csv file.


## Dependencies

`generate.py` relies on the following python libraries to run:

- pandas
- re
- sys


`pdf.sh` needs the following:

- bash 
- graphwiz (provides the dot program) [use `apt install graphwiz` on linux]


## Usage


### Setting up the source CSV file
Place a csv file in the same directory as these 2 files. The csv needs to have columns in the following format.

| Word_ID | word  | pos  | dep  |
|---------|-------|------|------|
| Word.1.1| cat   | NN   | 2    | 
| word.1.2| sat   | VM   | 0    | 
| word.2.1| bob   | NN   | 0    |

The column headers are case-sensitive. The data in the Word_ID column can have either capital or small w, it doesn't matter. There is no restriction on the values in any of the other columns.

### Generating dot files
Run `generate.py` to generate `.dot` files, providing the csv filename as command line input. 
```
python3 generate.py my_file.csv
```


The program generates a dot file for each sentence. They can be viewed using an online viewer.


### Generate PDFs from dot files
Run `pdf.sh` to convert each dot file in the directory into a pdf file of the same name containing the dependency tree image.
```
bash pdf.sh
```

# Error handling
Upon running the python script, some error messages may be printed suggesting that the sentence has an error. 

