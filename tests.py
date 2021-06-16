from VMTranslator import VMTranslator

files = [
    "assets\MemoryAccess\BasicTest\BasicTest.vm",
    "assets\MemoryAccess\PointerTest\PointerTest.vm",
    "assets\MemoryAccess\StaticTest\StaticTest.vm",
    "assets\StackArithmetic\SimpleAdd\SimpleAdd.vm",
    "assets\StackArithmetic\StackTest\StackTest.vm"
]

for f in files:
    vmt = VMTranslator(f)
    vmt.translate()
    vmt.code_writer.write()