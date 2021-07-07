# Hack-VM-Translator
Virtual Machine translator for symbolic Hack assembly code. Project from weeks 1 and 2 of the course, [Build a Modern Computer from First Principles: From Nand to Tetris Part II](https://www.coursera.org/learn/nand2tetris2).
## Description
Hack-VM-Translator converts VM code into symbolic Hack assembly code, which is designed for the Hack computer. Translation of virtual machine code into assembly code is part of a two-tier compilation process (notably used by Java). Virtual machine code is an intermediary step on the journey from high-level language code to machine code that is ultimately run by a computer.

This project is separated into the following components:
* __VMTranslator__ - Main class. Handles input, reads the VM file, writes to the assembly file, and drives the VM translation process.
* __Parser__ - Handles traversal and parsing of each line into its lexical components.
* __CodeWriter__ - Generates symbolic Hack assembly code from parsed VM commands.

## Usage
Hack-VM-Translator translates a single _.vm_ file, or all _.vm_ files within a directory, into one _.asm_ file.

Examples:
```bash
$ python VMTranslator.py fileName.vm
```
```bash
$ python VMTranslator.py fileDirectoryName
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
* local
* argument
* this
* that
* constant*
* pointer
* temp
* static

*Note: _constant_ is technically not a segment. In _push_ and _pop_ commands, _constant_ is used as a _segment_ to maintain the command syntax structure and simplify the translation process.

### Special Symbols
| Symbol | Usage |
|--------|-------|
| SP     | Predefined symbol that points to the memory address within the host RAM just after the address containing the topmost stack value. |
| LCL, ARG, THIS, THAT | Predefined symbols that point to the base addresses within the host RAM of the virtual segments _local, argument, this,_ and _that_ of the currently running VM function. |
| R13-R15 | Predefined symbols that can be used for any purpose. |
| _Xxx.i_ symbols | Each static variable _i_ in the file _Xxx.vm_ is translated into the assembly variable _Xxx.j_, where _j_ is incremented each time a new static variable is encountered in the file _Xxx.vm_. These variables are later allocated to RAM by the Hack assembler. |
| _functionName$label_ | Let _foo_ be a function within a VM file _Xxx.vm_. Each _label bar_ command command within _foo_ should generate and insert into the assembly code stream a symbol _Xxx.foo$bar_. When translating _goto bar_ and _if-goto bar_ commands (within _foo_) into assembly, the full label specification _Xxx.foo$bar_ must be used instead of bar. |
| _functionName_ | Each _function foo_ command within a VM file _Xxx.vm_ should generate and insert into the assembly code stream a symbol _Xxx.foo_ that labels the entry point to the function's code. This symbol is later translated by the Hack assembler into the physical memory address where the function's code begins. |
| _functionName$ret.i_ | Let _foo_ be a function within a VM file _Xxx.vm_. Within _foo_, each function _call_ command should generate and insert into the assembly code stream a symbol _Xxx.foo$ret.i_, where _i_ is a running integer (one such symbol should be generated for each _call_ command within _foo_). This symbol serves as the return address to the calling function. This symbol is later translated by the Hack assembler into the physical memory address of the command immediately after the function call command. |