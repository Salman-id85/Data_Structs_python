class PersistentList:
    def __init__(self, data=None, previous=None):
        self.data = data if data is not None else []
        self.previous = previous

    def append(self, value):
        return PersistentList(self.data + [value], self)

    def pop(self):
        if not self.data:
            raise IndexError("pop from empty list")
        return self.data[:-1], PersistentList(self.data[:-1], self.previous)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

# Example usage:
initial_list = PersistentList()
new_list = initial_list.append(1).append(2).append(3)
print("New list:", new_list.data)
print("Previous list:", new_list.previous.data)
