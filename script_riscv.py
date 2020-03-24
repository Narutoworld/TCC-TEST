import os
import sys
from Command import Command
from shutil import which

note ="""
    WARNING: It takes around an hour to setup the complete environment
    Installatio Guide:
        GNU Tool-chain: https://github.com/riscv/riscv-gnu-toolchain
        spike simulator: https://github.com/riscv/riscv-isa-sim
        pk boot loader: https://github.com/riscv/riscv-pk
    You have to first install above environment to run the simulation
    """

def install_riscv():
    print(note)

def compile_riscv(file):
    command = Command("riscv64-unknown-elf-gcc {} -lm -o riscv/{}".format(file, file[:-2]))
    command.run()

def run_riscv(file, output= None):
    if (not which("spick")) and (not which("riscv64-unknown-elf-gcc") and (not which("dtc"))):
        print(note)
    else:
        compile_riscv(file)
        command = Command('spike pk riscv/{}'.format(file[:-2]))
        command.run()


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
            install_riscv()
        else:
            print(msg)

    elif (len(sys.argv) == 3):
        cmd = sys.argv[1]
        src = sys.argv[2]

        if (cmd == "--run"):
            run_riscv(src)
        else:
            print(msg)
    else:
        print(msg)

