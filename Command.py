import subprocess, threading

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self):
        def target():
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()

        thread = threading.Thread(target=target)
        thread.start()

        thread.join()
        if thread.is_alive():
            self.process.terminate()
            thread.join()
        if (self.process.returncode):
            print("FAIL: ", self.cmd)

# command = Command("sh emsdk/emsdk install latest")
# command.run()