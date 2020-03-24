class Pychram:
    def execute(self):
        print("compiling")
        print("Running")
class MyEditor:
    def execute(self):    #method
        print("spell check")
        print("compiling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = Pychram()

lap1 = Laptop()
lap1.code(ide)

