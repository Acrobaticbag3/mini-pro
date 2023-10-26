from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        pass

    # Doubles size of bucket list
    def rehash(self):
        pass

    # Adds a word to set if not already added
    def add(self, word):
        pass

    # Returns a string representation of the set content
    def to_string(self):
        pass

    # Returns current number of elements in set
    def get_size(self):
        pass

    # Returns True if word in set, otherwise False
    def contains(self, word):
        pass

    # Returns current size of bucket list
    def bucket_list_size(self):
        pass

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        pass

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        pass

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        pass

    # Returns a list with all words in the set
    def as_list(self):
        pass
