class Computer:
    def __init__(self,size,model,ram,storage):
        self.size = size
        self.model = model
        self.ram = ram
        self.storage = storage

my_computer = Computer("Small", "Dell", 8 , 256)
print(my_computer.model)