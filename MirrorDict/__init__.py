"""
MirrorDict Module

This module defines the `MirrorDict` class.


Classes:
    - `MirrorDict`: 


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


from collections.abc import Hashable, MutableMapping
import inspect


# %% -----------------------------------------------------------------------------------------------


class MirrorDict:
    _key: dict
    _val: dict

    def __init__(self, *args, **kwargs):
        """
        Initialize a MirrorDict instance.

        Args:
            *args: A mapping object (e.g., dictionary) or an iterable of key-value pairs
                   to initialize the MirrorDict.
            **kwargs: Additional key-value pairs to initialize the MirrorDict.
        """
        self._key = {}
        self._val = {}
        self.update(*args, **kwargs)

    def clear(self):
        """
        Remove all items from the MirrorDict instance.
        """
        self._key.clear()
        self._val.clear()
        return self

    def items(self):
        """
        Iterate over key-value pairs from the initial mapping.
        """
        return self._key.items()

    def keys(self):
        """
        Return an iterator over the keys of the dictionary.
        """
        return self._key.keys()

    def update(self, *args, **kwargs):
        """
        Update the MirrorDict with key-value pairs from a mapping, iterable, or keyword arguments.

        This method adds new key-value pairs to the dictionary or updates the value for
        existing keys. Each key-value pair is mirrored such that the value is also mapped
        back to the key.

        Args:
            *args:
                - A mapping object (e.g., another dictionary) containing key-value pairs to add.
                - An iterable of key-value pairs (e.g., a list of tuples).
            **kwargs:
                Additional key-value pairs to add or update.

        Returns:
            MirrorDict: The updated instance of the dictionary
                        (update is done inplace, but returns self for chaining methods).

        Raises:
            TypeError: If an argument is not a mapping or an iterable of key-value pairs.

        Example Usage:
            >>> md = MirrorDict({'a': 1})
            >>> md.update({'b': 2}, c=3)
            MirrorDict({'a': 1, 'b': 2, 'c': 3, 1: 'a', 2: 'b', 3: 'c'})

            >>> md.update([('d', 4), ('e', 5)])
            MirrorDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'})
        """
        for arg in args:
            if isinstance(arg, (MutableMapping, MirrorDict)):
                for key, val in arg.items():
                    self._update(key, val)
            elif hasattr(arg, "__iter__"):  # If it's an iterable of key-value pairs
                try:
                    for key, val in arg:
                        self._update(key, val)
                except ValueError as e:
                    raise TypeError("MirrorDict.update() expected a dict-like or an iterable of key-value pairs") from e
            else:
                raise TypeError("MirrorDict.update() expected a dict-like or an iterable of key-value pairs")

        for key, val in kwargs.items():
            self._update(key, val)
        return self

    def values(self):
        """
        Return an iterator over the values of the dictionary.
        """
        return self._key.values()

    def _update(self, key, val):
        """
        Add or update a key-value pair and maintain the mirrored relationship.

        Args:
            key: The key to add or update.
            val: The value to associate with the key.

        Raises:
            TypeError: If key or value is not hashable.
        """
        if not isinstance(key, Hashable) or not isinstance(val, Hashable):
            caller = inspect.stack()[1].function
            raise TypeError(
                f"MirrorDict.{caller}(): both key and value must be hashable, but received key='{key}' ({type(key)}) "
                f"and value='{val}' ({type(val)})."
            )

        if key in self._key:  # key already defined, check if val is the same or needs to be updated
            val_old = self._key[key]
            if val_old == val:
                return
            self._val.pop(val_old)

        elif val in self._val:  # val already defined, update key to it
            self._key.pop(self._val[val])

        elif key in self._val:  # key in _val, so need to reverse storage direction
            self._key.pop(self._val.pop(key))

        elif val in self._key:  # val in _key, so need to reverse storage direction
            self._val.pop(self._key.pop(val))

        self._key[key] = val
        self._val[val] = key

    def __str__(self):
        return f"MirrorDict({self._key})"

    def __repr__(self):
        return str(self)

    def __hash__(self) -> int:
        return hash(self._key)

    def __len__(self):
        return len(self._key)

    def __iter__(self):
        """
        Iterate only over initial_keys.
        """
        return iter(self._key)


# %% -----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    md = MirrorDict(zip(["a", "b", "c"], [1, 2, 3]))
    md.update([("d", 4), ("e", 5), ("f", 6)])
    print(md)

    print(md.keys())
    print(md.values())
    print(md.items())
    md.clear()
    print(md.items())
