import os
import sys
from Command import Command

def install_wasm():
    print("git clone https://github.com/emscripten-core/emsdk.git")
    os.system("git clone https://github.com/emscripten-core/emsdk.git")
    print("sh emsdk/emsdk install latest")
    command = Command("sh emsdk/emsdk install latest")
    command.run()
    print("sh ./emsdk activate latest")
    command = Command("sh emsdk/emsdk activate latest")
    command.run()

def env_setup_wasm():
    print("source emsdk/emsdk_env.sh --build=Release")
    command = Command("source emsdk/emsdk_env.sh --build=Release")
    command.run()

def run_wasm(file, browser, output= None):
    env_setup_wasm()
    command = Command("emcc {} -lm -o wasm/{}".format(file, file[:-1]+"html"))
    command.run()
    # print("emcc {} -o wasm/{}".format(file, file[:-1]+"html"))
    command = Command('emrun wasm/{} --browser {} --port 8080 .'.format(file[:-1]+"html", browser))
    command.run()
    # print('emrun wasm/{} --browser {} --port 8080 .'.format(file[:-1]+"html", browser))

if __name__ == "__main__":
    msg = """
    arg1: < --install | --run >
    arg2: source file name
    arg3: [browser] (chrome as default)
    """
    # print ('Number of arguments:', len(sys.argv), 'arguments.')
    # print ('Argument List:', str(sys.argv))
    if (len(sys.argv) == 1):
        print(msg)
    elif (len(sys.argv) == 2):
        cmd = sys.argv[1]
        if (cmd == "--install"):
            install_wasm()
        else:
            print(msg)

    elif (len(sys.argv) == 3):
        cmd = sys.argv[1]
        src = sys.argv[2]
        browser = "chrome"

        if (cmd == "--run"):
            run_wasm(src, browser)
        else:
            print(msg)

    elif (len(sys.argv) == 4):
        cmd = sys.argv[1]
        src = sys.argv[2]
        browser = sys.argv[3]
        if (cmd == "--run"):
            run_wasm(src, browser)
        else:
            print(msg)
    else:
        print(msg)

