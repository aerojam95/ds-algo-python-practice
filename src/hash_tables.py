# =============================================================================
# Classes
# =============================================================================

class HashTable:
    """A hash table implementation with basic operations."""
    def __init__(self, size:int = 7) -> None:
        """
        Initialize a hash table with a given size.

        Args:
            size (int): The size of the hash table.
        """
        self.size = size
        self.data_map = [None] * size
        
    def __hash(self, key:str) -> int:
        """Generate a hash for a given key using a simple hashing algorithm.

        Args:
            key (str): The key to hash.

        Returns:
            int: The computed hash value.
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self) -> None:
        """Prints the current state of the hash table."""
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
            
    def set_item(self, key:str, value:int) -> None:
        """Insert a key-value pair into the hash table.

        If the key hashes to an index that already contains values, 
        it appends the new key-value pair to handle collisions.

        Args:
            key (str): The key to insert.
            value (int): The corresponding value.

        Returns:
            None
        """
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key:str) -> int | None:
        """Retrieve the value associated with a given key.

        Args:
            key (str): The key to search for.

        Returns:
            int: The value associated with the key.
        """
        index = self.__hash(key)
        pair = self.data_map[index]
        
        if pair is not None:
            for stored_key, stored_value in pair:
                if stored_key == key:
                    return stored_value
        return None
    
    def keys(self) -> list[str]:
        """Return all keys in the hash table.

        Returns:
            list[str]: A list of all keys in the hash table.
        """
        keys_list = []
        
        for pair in self.data_map:
            if pair is not None:
                keys_list.extend(key for key, _ in pair)
        return keys_list