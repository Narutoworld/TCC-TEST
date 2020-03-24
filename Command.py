import subprocess, threading
import os

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self):
        env_variable = []
        def target():
            self.process = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE)
            for line in self.process.stdout:
                env_variable.append(str(line))
            self.process.communicate()

        thread = threading.Thread(target=target)
        thread.start()

        thread.join()
        if thread.is_alive():
            self.process.terminate()
            thread.join()
        if (self.process.returncode):
            print("FAIL: ", self.cmd)


        return env_variable

# command = Command("sh emsdk/emsdk install latest")
# command.run()