"""
MirrorDict Module

This module defines the `MirrorDict` class.


Classes:
    - `MirrorDict`: Represents the result of an operation, containing either
                an `Ok(value)` for success or an `Err(error)` for failure.


Key Features:
    - TBA

Constructors:
    MirrorDict():
        Main class .

Example Usage:
    >>> from MirrorDict import MirrorDict
    >>>

"""

# %% -----------------------------------------------------------------------------------------------

__version__ = "0.0.1"
__author__ = "Scott E. Boyce"
__credits__ = "Scott E. Boyce"
__maintainer__ = "Scott E. Boyce"
__email__ = "boyce@engineer.com"
__license__ = "MIT"
__status__ = "Development"  # set to "Prototype", "Development", "Production"
__url__ = "https://github.com/ScottBoyce-Python/MirrorDict"
__description__ = "MirrorDict is a ."
__copyright__ = "Copyright (c) 2025 Scott E. Boyce"

__all__ = ["MirrorDict"]


# %% -----------------------------------------------------------------------------------------------


from collections.abc import Sequence, Iterable, KeysView, ValuesView
from copy import deepcopy as _deepcopy


# %% -----------------------------------------------------------------------------------------------


class MirrorDict(dict):
    """
    A custom dictionary that hashes both the key and value.

    Attributes:
        initial_keys (set): Set of items that were initially used as the key component.
        initial_values (set): Set of items that were initially used as the values component.

    Methods:
        keys(): Returns all initial_keys.
        values(): Returns all initial_values.
        items(): Iterates over key-value pairs.
        copy(): Creates a shallow copy of the dictionary.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the dictionary, supporting key-value pairs
        while enforcing the custom rules.
        """
        super().__init__()
        self.initial_keys = set()
        self.initial_values = set()
        # Accept arguments in various forms like dicts, lists, or kwargs
        for key, value in dict(*args, **kwargs).items():
            self[key] = value

    def keys(self):
        """
        Return a dynamic KeysView reflecting initial_keys.
        """
        return KeysView(self.initial_keys)

    def values(self):
        """
        Return a dynamic ValuesView reflecting initial_values.
        """
        return ValuesView(self.initial_values)

    def items(self):
        """
        Iterate over initial_keys and return (key, value) pairs.
        """
        for key in self.initial_keys:
            yield key, self[key]

    def copy(self):
        """
        Return a shallow copy of the MirrorDict instance.
        """
        new_copy = MirrorDict()
        for key, value in self.items():
            new_copy[key] = value
        return new_copy

    def __iter__(self):
        """
        Iterate only over initial_keys.
        """
        return iter(self.initial_keys)

    def pop(self, *args, **kwargs):
        raise NotImplementedError("MirrorDict: Method not supported")

    def popitem(self, *args, **kwargs):
        raise NotImplementedError("MirrorDict: Method not supported")

    def reversed(self, *args, **kwargs):
        raise NotImplementedError("MirrorDict: Method not supported")

    def setdefault(self, *args, **kwargs):
        raise NotImplementedError("MirrorDict: Method not supported")

    def update(self, *args, **kwargs):
        raise NotImplementedError("MirrorDict: Method not supported")

    def __setitem__(self, key, value):
        """
        Add a new key-value pair while enforcing rules.

        Args:
            key (Any): The key.
            value (Any): The corresponding value, which must be the opposite type of the key.
        """

        # Remove previous mappings if they exist
        if key in self:
            old_value = self[key]
            del self[key]
            del self[old_value]
            self._remove(key, old_value)
        if value in self:
            old_key = self[value]
            del self[value]
            del self[old_key]
            self._remove(old_key, value)

        # Add new mappings
        self.initial_keys.add(key)
        self.initial_values.add(value)
        super().__setitem__(key, value)
        super().__setitem__(value, key)

    def __getitem__(self, key):
        """
        Retrieve the value associated with a key.
        Args:
            key (Any): The key to look up.

        Returns:
            Any: The corresponding value.

        """
        return super().__getitem__(key)

    def __delitem__(self, key):
        """
        Deletes both the key and its bidirectional counterpart (keys ↔ values).
        """
        if key in self:
            value = self[key]
            self._remove(key, value)
            super().__delitem__(key)
            super().__delitem__(value)

    def _remove(self, key, value):
        """
        Safely remove key-value pair references from tracking sets.
        """
        self.initial_keys.remove(key)
        self.initial_values.remove(value)


# %% -----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    print("program completed successfully")
