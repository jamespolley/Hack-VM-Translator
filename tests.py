from VMTranslator import VMTranslator


vm_files = [
    "assets\MemoryAccess\BasicTest\BasicTest.vm",
    "assets\MemoryAccess\PointerTest\PointerTest.vm",
    "assets\MemoryAccess\StaticTest\StaticTest.vm",
    "assets\StackArithmetic\SimpleAdd\SimpleAdd.vm",
    "assets\StackArithmetic\StackTest\StackTest.vm"
]

for f in vm_files:
    vmt = VMTranslator(f)
    print("VMTranslator read the file at: ", f)
    vmt.translate()
    print("VMTranslator wrote to the file at:", vmt.asm_file_path, "\n")