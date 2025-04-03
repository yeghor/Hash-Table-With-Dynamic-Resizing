class Node:
    def __init__(self, key, value):
        self.next = None
        self.value = value
        self.key = key

class HashMap:

    @staticmethod
    def __add_internal(node: Node, actual_array):
        node_index = HashMap.__calculate_key_index(node.key, actual_array)
        if actual_array[node_index]:
            current_node = actual_array[node_index]
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        else:
            actual_array[node_index] = node

    @staticmethod
    def __calculate_key_index(key, array):
        return hash(key) % len(array)
    
    def get(self, key):
        key_index = self.__calculate_key_index(key, self.array)
        current = self.array[key_index]

        while current:
            if current.key == key:
                return current.value
            current = current.next            
        return None       


    class HashMapIterator:
        def __init__(self, array, return_node=False):
            self.array = array
            self.bucket_index: int = 0
            self.bucket_node_current: Node = None
            self.return_node = return_node

        def __iter__(self):
            return self

        def __next__(self) -> Node | tuple:
            while self.bucket_index < len(self.array) and not self.array[self.bucket_index]:
                self.bucket_index += 1

            if self.bucket_index == len(self.array):
                raise StopIteration
            
            if self.bucket_node_current:
                if self.bucket_node_current.next:
                    self.bucket_node_current = self.bucket_node_current.next
                    return self.bucket_node_current if self.return_node else (self.bucket_node_current.key, self.bucket_node_current.value)
                else:
                    self.bucket_index += 1
                    self.bucket_node_current = None
                    return self.__next__()
            else:
                self.bucket_node_current = self.array[self.bucket_index]
                return self.bucket_node_current if self.return_node else (self.bucket_node_current.key, self.bucket_node_current.value)
            

    def __init__(self, start_capacity=10,  expand_factor=2):
        self.capacity = start_capacity
        self.array = [None] * self.capacity
        self.counter: int = 0
        self.expand_factor = expand_factor


    def __iter__(self):
        iterator = self.HashMapIterator(array=self.array)
        return iterator


    def __str__(self) -> str:
        string = ""
        for item in self.array:
            if not item:
                continue
            if item.next:
                while item:
                    string += f"[{item.key} : {item.value}] -> "
                    item = item.next
            else:
                string += f"[{item.key} : {item.value}]\n"
        return string


    def delete_by_key(self, key) -> bool:
        key_index = self.__calculate_key_index(key, self.array)
        current: Node = self.array[key_index]
        parent: Node = None

        while current:
            if current.key == key:
                if parent:
                    parent.next = current.next
                else:
                    self.array[key_index] = None
                current = None
                return True
            
            parent = current
            current = current.next
        return False


    def add(self, key, value):
        self.__capacity_logic()
        node = Node(key, value)
        self.__add_internal(node=node, actual_array=self.array)
        self.counter += 1


    def __capacity_logic(self):
        if self.__check_capacity():
            self.__increase_capacity()


    def __check_capacity(self) -> bool:
        load_factor = self.counter / self.capacity
        if load_factor >= 0.75:
            return True
        else:
            return False


    def __increase_capacity(self):
        self.counter = 0
        new_array = [None] * len(self.array) * self.expand_factor
        self.capacity = len(new_array)
        iterator = self.HashMapIterator(array=self.array, return_node=True)
        for node in iterator:
            self.__add_internal(node=Node(key=node.key, value=node.value), actual_array=new_array)
            self.counter += 1

        self.array = new_array