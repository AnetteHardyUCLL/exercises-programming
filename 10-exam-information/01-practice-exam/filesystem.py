from abc import ABC, abstractmethod
import re
from typing import List


class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__block_count = block_count
        self.__block_size = block_size
        self.__available_blocks = set(range(block_count))
        self.__used_blocks = set()

    @property
    def available_block_count(self):
        return len(self.__available_blocks)

    @property
    def used_block_count(self):
        return len(self.__used_blocks)

    @property
    def total_block_count(self):
        return self.__block_count

    @property
    def block_size(self):
        return self.__block_size

    def allocate(self, block_count: int):
        if block_count > len(self.__available_blocks):
            raise RuntimeError("Insufficient available blocks")
        # convert to list
        available_blocks = list(self.__available_blocks)

        allocated_blocks = available_blocks[:block_count]
        self.__available_blocks = set(available_blocks[block_count:])

        # update here because the add method is used to add a single block
        self.__used_blocks.update(allocated_blocks)

        return allocated_blocks

    def free(self, blocks: List[int]):
        if not all(block in self.__used_blocks for block in blocks):
            raise RuntimeError("Attempt to free blocks that are not in use")

        self.__available_blocks.update(blocks)

        self.__used_blocks.difference_update(blocks)


class Entity(ABC):
    def __init__(self, storage: StorageDevice, name: str):
        if not self.is_valid_name(name):
            raise RuntimeError("Invalid name")
        self.__storage = storage
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if not self.is_valid_name(new_name):
            raise RuntimeError("Invalid name")
        self.__name = new_name

    @staticmethod
    def is_valid_name(name: str):
        return re.fullmatch("[a-zA-Z0-9.]{1,16}", name) is not None

    @property
    def storage(self):
        return self.__storage

    @property
    @abstractmethod
    def size_in_blocks(self): ...

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.__storage.block_size

    @abstractmethod
    def clear(self): ...


class File(Entity):
    def __init__(self, storage: StorageDevice, name: str):
        super().__init__(storage, name)
        self.__blocks = []

    def grow(self, block_count):
        self.__blocks.extend(self.storage.allocate(block_count))

    @property
    def size_in_blocks(self):
        return len(self.__blocks)

    def clear(self):
        self.storage.free(self.__blocks)
        self.__blocks = []


class Directory(Entity):
    def __init__(self, storage: StorageDevice, name: str):
        super().__init__(storage, name)
        self.__children = []

    def add(self, entity: Entity):
        self.__children.append(entity)

    @property
    def size_in_blocks(self):
        return sum(child.size_in_blocks for child in self.__children)

    def clear(self):
        for child in self.__children:
            child.clear()
        self.__children = []
