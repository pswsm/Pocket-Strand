# Pocket Strand
Mini command line toolkit for anyone who need to look up quickly variations of DNA sequences.

Works with 3.6 -> 3.10 versions of Python.
(Older versions haven't been tested yet.)
Has been written and tested on Pop-Os! and Ubuntu distros.
Hasn't been tested on MacOS or Windows.

NOTE: The code only works with .txt for now. 

## How to run the code
1. Download the code.
2. Make sure You have a python 3.6 or newer interpreter installed. [I recommend (no advert..) Anaconda package manager.]
3. Enter to the directory of the code and run "python main.py" command.

## How to use Pocket Strands
1. Use the number of the menu options to navigate.
2. Importing data for analysis must give the file path (for example: "./saved_results/dna2.txt").
3. When saving the output, a new directory("saved_results") will be created in the current directory of the code, to where the result is going to be saved with .txt extension.

## Features
- Randomize sequences (nucleotides or amino acids)
    - User defines the desired length and the chosen type of sequence will be returned.

- Count nucleotides, GC content, approximate mass
    - User imports or manually inputs the sequence 
      and the mentioned details will be returned.

- DNA Transcription / Translation / Complement / Reverse complement
    - User imports or manually inputs the sequence 
      and the result of the chosen process fill be returned.

- Display both data
    -When the ouput is a strand, the code will offer the user the option 
     to display the original data and the result in a more readable/comparable manner.

- Save outputs in text.
    - User inputs the desired file name without the extension
      and the code will save the output into a subdirectory(saved) of its own directory.
      (Code will create one, if 'saved' doesn't exist.)

## Future features
- Pocket Strand will be able to fully function with FASTA / FASTAQ extensions.
- More general analysis options.
