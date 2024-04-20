class PersistentHashMap:
    def __init__(self, data=None, previous=None):
        self.data = data if data is not None else {}
        self.previous = previous

    def insert(self, key, value):
        new_data = self.data.copy()
        new_data[key] = value
        return PersistentHashMap(new_data, self)

    def remove(self, key):
        new_data = self.data.copy()
        del new_data[key]
        return PersistentHashMap(new_data, self)

    def get(self, key):
        return self.data.get(key)

class PersistentHashSet:
    def __init__(self, data=None, previous=None):
        self.data = set(data) if data is not None else set()
        self.previous = previous

    def add(self, value):
        new_data = self.data.copy()
        new_data.add(value)
        return PersistentHashSet(new_data, self)

    def remove(self, value):
        new_data = self.data.copy()
        new_data.remove(value)
        return PersistentHashSet(new_data, self)

    def contains(self, value):
        return value in self.data

# Example usage:
initial_map = PersistentHashMap()
new_map = initial_map.insert("key1", "value1").insert("key2", "value2")
print("New map:", new_map.data)
print("Previous map:", new_map.previous.data)

initial_set = PersistentHashSet()
new_set = initial_set.add(1).add(2).add(3)
print("New set:", new_set.data)
print("Previous set:", new_set.previous.data)
