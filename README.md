# Hack-VM-Translator
Virtual Machine translator for symbolic Hack assembly code. Project from weeks 1 and 2 of the course, [Build a Modern Computer from First Principles: From Nand to Tetris Part II](https://www.coursera.org/learn/nand2tetris2).
## Description
NOTE: This project is in progress, and currently does not work.

This project is separated into the following components:
* __VMTranslator__ - Main class. Handles input, reads the VM file, writes to the assembly file, and drives the VM translation process.
* __Parser__ - Handles traversal and parsing of each line into its lexical components.
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
    * and
    * or
    * neg
    * not
    * lt
    * eq
    * gt
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