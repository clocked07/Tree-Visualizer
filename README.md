# Tree Analyzer

This tool generates dependency trees of sentences from a structure specified in a csv file.


## Dependencies

`generate.py` relies on the following python libraries to run:

- pandas
- re
- sys


`pdf.sh` needs the following:

- bash 
- graphviz (provides the dot program) [use `apt install graphviz` on linux]


## Usage


### Setting up the source CSV file
Place a csv file in the same directory as these 2 files. The csv needs to have columns in the following format.

| Word_ID | word  | pos  | dep  |
|---------|-------|------|------|
| Word.1.1| cat   | NN   | 2    | 
| word.1.2| sat   | VM   | 0    | 
| word.2.1| bob   | NN   | 0    |

**`dep` of the root word must be set to 0.**
**There can only be one root.**

#### Word_ID Format

`Word_ID` is formatted as `Word.sentence_number.word_index`.

#### Restrictions
- Column headers are case-sensitive.
- `dep` must contain only integers.
- All columns except `pos` are required to have a value for each row. If not, the corresponding row will be skipped.


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

## Example

Let's say we have the sentence मेरी अमी जान कहती थी.

Our csv looks like this

| Word_ID | word  | pos  | dep  |
|---------|-------|------|------|
Word.1.1|	मेरी|	Det|	2
Word.1.2|	अमी	|N	|4
Word.1.3|	जान	|Adj	|2
Word.1.4|	कहती|	V	|5
Word.1.5|	थी	|Aux|	0

Here थी is the root so it's `dep` is 0.

Our output after running `generate.py` and `pdf.sh` is:

![](img/corrected-pdf.png?raw=true)

## Error handling
Upon running the python script, some error messages may be printed suggesting that the csv file has an error. 

### Incorrect rendering of special characters
An output with "tofu boxes" like this indicates that your system's default font does not support the special characters in your text.


![tofu box](img/error-pdf.png?raw=true)

To resolve this issue, install [Noto Sans by Google](https://fonts.google.com/noto/specimen/Noto+Sans). This font supports almost every script in the world.

Running the program again will give you a properly rendered pdf.

![corrected pdf](img/corrected-pdf.png?raw=true)


