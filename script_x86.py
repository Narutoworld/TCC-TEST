import os
import sys
from Command import Command
from shutil import which

note ="""
    Installatio Guide:
        GNU GCC
    You have to first install above environment to run the simulation
    """

def install_x86():
    print(note)

def compile_x86(file):
    print("gcc {} -lm -o x86/{}".format(file, file[:-2]))
    command = Command("gcc {} -lm -o x86/{}".format(file, file[:-2]))
    command.run()

def run_x86(file, output= None):
    if (not which("gcc")):
        print(note)
    else:
        compile_x86(file)
        print('./x86/{}'.format(file[:-2]))
        command = Command('./x86/{}'.format(file[:-2]))
        stdout= command.run()
        for line in stdout:
            print(line[2:-3])


if __name__ == "__main__":
    msg = """
    arg1: < --install | --run >
    arg2: source file name
    """
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    # print ('Argument List:', str(sys.argv))
    if (len(sys.argv) == 1):
        print(msg)
    elif (len(sys.argv) == 2):
        cmd = sys.argv[1]
        if (cmd == "--install"):
            install_x86()
        else:
            print(msg)

    elif (len(sys.argv) == 3):
        cmd = sys.argv[1]
        src = sys.argv[2]

        if (cmd == "--run"):
            run_x86(src)
        else:
            print(msg)
    else:
        print(msg)

