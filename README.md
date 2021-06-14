# VM-Hack-Translator
Virtual Machine translator for Hack symbolic assembly code. Project from week 1 and 2 of the course, [Build a Modern Computer from First Principles: From Nand to Tetris Part II](https://www.coursera.org/learn/nand2tetris2).
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

## VM Language
### Commands
* Arithmetic/Logical
    * add
    * sub
    * neg
    * eq
    * gt
    * lt
    * and
    * or
    * not
* Memory Access
    * push _segment i_
    * pop _segment i_
* Branching
    * label _label_
    * goto _label_
    * if-goto _label_
* Function
    * function _functionName nVars_
    * call _functionName nArgs_
    * return
### Segments
* [To do]