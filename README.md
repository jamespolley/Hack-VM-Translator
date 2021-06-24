# Hack-VM-Translator
Virtual Machine translator for symbolic Hack assembly code. Project from weeks 1 and 2 of the course, [Build a Modern Computer from First Principles: From Nand to Tetris Part II](https://www.coursera.org/learn/nand2tetris2).
## Description
Hack-VM-Translator converts VM code into symbolic Hack assembly code, which is designed for the Hack computer. Translation of virtual machine code into assembly code is part of a two-tier compilation process (notably used by Java). Virtual machine code is an intermediary step on the journey from high-level language code to machine code that is ultimately run by a computer.

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
### Special Symbols
| Symbol | Usage |
|--------|-------|
| SP     | Predefined symbol that points to the memory address within the host RAM just after the address containing the topmost stack value. |
| LCL, ARG, THIS, THAT | Predefined symbols that point to the base addresses within the host RAM of the virtual segments _local, argument, this,_ and _that_ of the currently running VM function. |
| R13-R15 | Predefined symbols that can be used for any purpose. |
| _Xxx.i_ symbols | Each static variable _i_ in the file _Xxx_ is translated into the assembly variable _j_, where _j_ is incremented each time a new static variable is encountered in the file _Xxx.vm_. In the assembly process, these variables are allocated to RAM by the Hack assembler. |
| _functionName$label_ | [to do] |
| _functionName_ | [to do] |
| _functionName$ret.i_ | [to do] |