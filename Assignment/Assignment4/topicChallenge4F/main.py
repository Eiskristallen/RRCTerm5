class MyClass:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        with open(self.filename, self.mode) as myfile:
            self.myfile = myfile
        return self.myfile
# miss args

    def __exit__(self, exc_type, exc_value, exc_trac):
        self.myfile.close()


with MyClass('test.txt', 'r') as myfile:
    print(myfile)
