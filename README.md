# VM-Hack-Translator
Virtual Machine translator for Hack symbolic assembly code. Week 1 and 2 of the course, [Build a Modern Computer from First Principles: From Nand to Tetris Part II](https://www.coursera.org/learn/nand2tetris2).
## Description
NOTE: This project is in progress, and currently does not work.

This project is separated into the following components:
* __VMTranslator__ - Main class. Handles the input file. Drives the VM translation process.
* __Parser__ - Handles reading of the input file. Formats and parses each line into its lexical components.
* __CodeWriter__ - Generates symbolic Hack assembly code from parsed VM commands.

## Usage
```bash
$ python VMTranslator.py file.vm
```
## Specifications
