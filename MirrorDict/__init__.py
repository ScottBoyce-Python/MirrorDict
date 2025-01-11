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


class MirrorDict(MutableMapping):
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

    def copy(self):
        """
        Return a shallow copy of the MirrorDict instance.
        """
        return MirrorDict(self)

    def get(self, key, default=None):
        """
        Return the value for key if key is in the dictionary, else default.
        """
        if key in self._key:
            return self._key[key]
        if key in self._val:
            return self._val[key]
        return default

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

    def pop(self, key, default=KeyError):
        """
        Remove a key (or value) and its mirrored counterpart from the dictionary.

        If the key (or value) exists in the dictionary, both it and its mirrored
        counterpart are removed. If the key does not exist, the `default` value
        is returned if provided; otherwise, a `KeyError` is raised.

        Args:
            key: The key (or value) to remove.
            default: The value to return if the key is not found.
                    If not provided, a `KeyError` is raised.

        Returns:
            The removed value if a key is provided, or the removed key if a value is provided.

        Raises:
            KeyError: If the key is not found and no default is provided.

        Example Usage:
            >>> md = MirrorDict({'a': 1, 'b': 2})
            >>> md.pop('a')  # Removes the key 'a' and its mirrored counterpart 1
            1
            >>> md
            MirrorDict({'b': 2, 2: 'b'})

            >>> md.pop(2)  # Removes the value 2 and its mirrored counterpart 'b'
            'b'
            >>> md
            MirrorDict({})

            >>> md.pop('c', 'default')  # Returns 'default' as 'c' does not exist
            'default'

            >>> md.pop('c')  # Raises KeyError as 'c' does not exist and no default is provided
            Traceback (most recent call last):
                ...
            KeyError: 'MirrorDict.pop(key, default): key="c" not found and default=KeyError.'
        """
        if key in self._key:
            val = self._key[key]
            del self._key[key]
            del self._val[val]
            return val
        if key in self._val:
            key, val = self._val[key], key
            del self._key[key]
            del self._val[val]
            return key
        if default is not KeyError:
            return default
        raise KeyError(f'MirrorDict.pop(key, default) key="{key}" not found and default=KeyError.')

    def popitem(self):
        """
        Remove and return an arbitrary key-value pair from the dictionary.

        Removes the last inserted key-value pair and ensures the mirrored relationship
        is updated accordingly. If the dictionary is empty, raises a `KeyError`.

        Returns:
            tuple: A tuple containing the key and value of the removed item.

        Raises:
            KeyError: If the dictionary is empty.

        Example:
            >>> md = MirrorDict(a=1, b=2)
            >>> md.popitem()
            ('b', 2)
            >>> print(md)
            MirrorDict({'a': 1, 1: 'a'})
        """
        if len(self._key) == 0:
            raise KeyError("MirrorDict.popitem() dictionary is empty.")
        key, val = self._key.popitem()
        del self._val[val]
        return key, val

    def __reversed__(self):
        return reversed(self._key.keys())

    def reversed(self):
        """
        Return a reversed iterator over the dictionary's keys.

        This is equivalent to iterating over the keys in reverse order. Note that this
        method affects only the order of keys when iterated; it does not change the
        internal order of storage.

        Returns:
            A reversed iterator over the dictionary's keys.

        Example:
            >>> md = MirrorDict({'a': 1, 'b': 2})
            >>> list(md.reversed())
            ['b', 'a']
        """
        return reversed(self._key.keys())

    def setdefault(self, key, default=None):
        """
        Insert a key-value pair into the dictionary if the key is not already present.

        If the key exists, its associated value is returned. If the key does not exist,
        the `default` value is used as the key's value, and the new key-value pair is
        added to the dictionary.

        Args:
            key: The key to check or insert.
            default: The value to associate with the key if it is not already present.
                     Defaults to `None`.

        Returns:
            The value associated with the key.

        Example:
            >>> md = MirrorDict(a=1)
            >>> md.setdefault('b', 2)
            2
            >>> md.setdefault('a', 3)
            1
        """
        if key in self._key:
            return self._key[key]
        if key in self._val:
            return self._val[key]

        self._update(key, default)
        return default

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
            if isinstance(arg, MutableMapping):
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

    def __contains__(self, key):
        return key in self._key or key in self._val

    def __setitem__(self, key, value):
        """
        Add a new key-value pair while enforcing rules.

        Args:
            key (Any): The key.
            value (Any): The corresponding value, which must be the opposite type of the key.
        """
        self._update(key, value)

    def __getitem__(self, key):
        """
        Retrieve the value associated with a key.
        Args:
            key (Any): The key to look up.

        Returns:
            Any: The corresponding value.

        """
        if key in self._key:
            return self._key[key]
        if key in self._val:
            return self._val[key]
        raise KeyError(f'MirrorDict[key] does not have key="{key}".')

    def __delitem__(self, key):
        """
        Deletes both the key and its bidirectional counterpart (keys ? values).
        """
        if key in self._key:
            val = self._key.pop(key)
            self._val.pop(val)
        elif key in self._val:
            val = key
            key = self._val.pop(val)
            self._key.pop(key)
        else:
            raise KeyError(f'del MirrorDict[key] does not have key="{key}".')


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
