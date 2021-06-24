from VMTranslator import VMTranslator

# To check if tests passed, the CPU emulator is required. It can be
# downloaded at https://www.nand2tetris.org/software.

# ALL TESTS PASSED!

# Nand 2 Tetris Pt.2 Week 1 Test Files
vmt = VMTranslator(
    "assets\MemoryAccess\BasicTest\BasicTest.vm",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED

vmt = VMTranslator(
    "assets\MemoryAccess\PointerTest\PointerTest.vm",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED

vmt = VMTranslator(
    "assets\MemoryAccess\StaticTest\StaticTest.vm",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED

vmt = VMTranslator(
    "assets\StackArithmetic\SimpleAdd\SimpleAdd.vm",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED

vmt = VMTranslator(
    "assets\StackArithmetic\StackTest\StackTest.vm",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED

# Nand 2 Tetris Pt.2 Week 2 Test Files
vmt = VMTranslator("assets\FunctionCalls\FibonacciElement")
vmt.translate() # Test PASSED

vmt = VMTranslator("assets\\FunctionCalls\\NestedCall")
vmt.translate() # Test PASSED

vmt = VMTranslator(
    "assets\FunctionCalls\SimpleFunction",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED

vmt = VMTranslator("assets\FunctionCalls\StaticsTest")
vmt.translate() # Test PASSED

vmt = VMTranslator(
    "assets\ProgramFlow\BasicLoop",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED

vmt = VMTranslator(
    "assets\ProgramFlow\FibonacciSeries",
    include_init_code=False) # init done by .tst file
vmt.translate() # Test PASSED