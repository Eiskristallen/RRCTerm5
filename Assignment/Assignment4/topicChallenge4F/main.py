class MyClass:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.myfile = None

    def __enter__(self):
        self.myfile = open(self.filename, self.mode)
        return self.myfile
# miss args

    def __exit__(self, exc_type, exc_value, exc_trac):
        self.myfile.close()


with MyClass("test.txt", "r") as f:
    print(f.read())
