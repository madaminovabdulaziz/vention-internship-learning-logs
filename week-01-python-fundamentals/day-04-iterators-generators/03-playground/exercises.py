class ManageFile:
    def __init__(self, name):
        self.name = name


    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    

    def __exit__(self, exc_type, exc, tb):

        if self.file:
            self.file.close()

        


        return False
    

with ManageFile("hello.txt") as f:
    f.write("hello")