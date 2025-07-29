import os
class Server:
    def __init__(self, name, model):
        self.model = model
    def run_command(self):
        command = input("Enter the command: ")
        print("You have entered is: ", command)
        print(os.system(command))

    def run_log_file(self):
        command1 = input("Enter the command: ")
        print("You have entered is: ", command1)
        print(os.system(command1))
        # return run_command
sobj = Server("poweredge", "rack")
sobj.run_command()
sobj.run_log_file()