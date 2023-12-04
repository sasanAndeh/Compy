enum_cunter=0;
from enum import Enum
import subprocess , os
import sys
def NewEnum(reset=False):
    global enum_cunter;
    if reset:
        enum_cunter = 0
    result = enum_cunter 
    enum_cunter += 1
    return result

OP_PUSH   = NewEnum(True)
OP_PLUS   = NewEnum()
OP_MINUS  = NewEnum() 
OP_DUMP   = NewEnum()
COUNT_OPS = NewEnum()

def push(x):
     return (OP_PUSH ,x)
def plus():
    return(OP_PLUS, )
def dump():
    return(OP_DUMP, )
def minus():
    return(OP_MINUS,)
def simulate_program(program):
    stack = []
    for op in program:
        assert COUNT_OPS == 4, "Exhastive handling of operations in simulation"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif op[0] == OP_DUMP: 
            a = stack.pop()
            print(a)
        else:
            assert False,"Unreachable"

def compile_program(program,out_file_path):
    with open(out_file_path,"w") as output:
            output.write("""
segment .text
global _start
_start:
    mov rax,60
    mov rdi,69
    syscall
                """)

# TODO : UnhardCode Program
program = [
    push(34),
    push(35),
    plus(),
    dump(),
    push(500),
    push(80),
    minus(),
    dump(),
]

def usage():
    print("Usage : Compy <SUBCOMMAND> [ARGS] ")
    print("""
SUBCOMMANDS :
              sim   Simulate the Program
              com   Compile the Program
              """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        print('Error  : No subcommand is provided')
        exit(1)
    subcommand = sys.argv[1]
    if subcommand == 'sim':
        simulate_program(program)
    elif subcommand == 'com':
        compile_program(program,r"bin/output.asm");
        os.system("nasm -fwin64 bin/output.asm -o bin/output.o")
        os.system("ld -s -o bin/output.exe bin/output.o")

    else:
        usage()
        print(f"Error : Unknown subcommand {subcommand}")
        exit(1)
