# Structure of the CSV
Place a csv file in the same directory as these 2 files. The csv needs to have columns in the following format (other columns are optional)
| Word_ID | word  | pos  | dep  |
|---------|-------|------|------|
| Word.1.1| cat   | NN   | 2    | 
| word.1.2| sat   | VM   | 0    | 

# Generating pdf files
Run the python script to generate `.dot` files, providing the csv filename as command line input. Then generate the bash script to generate the pdfs.
```bash
python3 generate.py my_file.csv
bash pdf.sh
```
# Error handling
Upon running the python script, some error messages may be printed suggesting that the sentence as an error. 

