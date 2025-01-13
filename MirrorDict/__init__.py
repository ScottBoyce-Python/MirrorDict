"""
MirrorDict Module

This module defines the `MirrorDict` class, a bi-directional dictionary-like object.
It supports all the dict methods and maintains a mirrored relationship between
keys (`k`) and values (`v`) such that `k:v` pairs are also stored as `v:k` pairs.
Requires that both the key and values be hashable and unique.

The order of the keys are preserved and the order of values are based on the keys.
Methods, such as keys() and values() method return the items that were set
initially as a key and value. That is, for a given key, updating its value keeps
the original order of the keys but moves the new value to the end of values.
However, setting an existing `v` as a key, moves the value to the end of the keys,
removes the existing `k` from the keys and adds it to the end of the values.

Classes:
    - `MirrorDict`: Represents a bi-directional dictionary, where each key-value pair
      is mirrored as a value-key pair for efficient reverse lookups.

Key Features:
    - Automatically maintains a bi-directional mapping between keys and values.
        - Key-index lookup will return `value` for `key`, and return `key` for `value`.
    - Ensures all keys and values are hashable.
    - Supports standard dictionary operations (e.g., `keys`, `items`, `get`, `pop`).
    - What is stored initially as a key   is represented as a `dict_keys` and
      what is stored initially as a value is represented as a `dict_values`.
    - Changing either a key or value removes the old mirrored relationship
      to create the new one. If the key is changed, then the old one is
      removed and the new added to the end of keys().

Constructors:
    MirrorDict(*args, **kwargs):
        Initializes the dictionary with mappings, iterables, or keyword arguments.

Example Usage:
    >>> from MirrorDict import MirrorDict
    >>> md = MirrorDict({'a': 1, 'b': 2})
    >>> md['c'] = 3
    >>> print(md[3])
    'c'
    >>> del md['a']
    >>> print(md)
    MirrorDict({'b': 2, 2: 'b', 'c': 3, 3: 'c'})
    >>>
    >>>md = MirrorDict()
    >>>md["a"] = 1                                # Stored as: key="a", value=1
    >>>md["b"] = 2                                # Stored as: key="b", value=2
    >>>md["c"] = 3                                # Stored as: key="c", value=3
    >>>
    >>>print( md["b"] )
    2
    >>>print( md[2] )
    b
    >>>
    >>>print( md.keys(), md.values() )
    dict_keys(['a', 'b', 'c']) dict_values([1, 2, 3])
    >>>
    >>print( md.items() )
    dict_items([('a', 1), ('b', 2), ('c', 3)])
    >>>
    >>>md.update( [("d", 4), ("e", 5)] )
    >>>md["f"] = 6
    >>>
    >>>print( md.keys(), md.values() )
    dict_keys(['a', 'b', 'c', 'd', 'e', 'f']) dict_values([1, 2, 3, 4, 5, 6])
    >>>
    >>print( md.items() )
    dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)])
    >>>
    >>>print( md.pop(3) )  # if 3 is k or v, drop k:v and v:k pairs and return the opposite, otherwise raise KeyError
    c
    >>>del md["e"]         # if "e" is k or v, drop k:v and v:k pairs, otherwise raise KeyError
    >>>
    >>>print( md.keys(), md.values() )
    dict_keys(['a', 'b', 'd', 'f']) dict_values([1, 2, 4, 6])
    >>>
    >>print( md.items() )
    dict_items([('a', 1), ('b', 2), ('d', 4), ('f', 6)])
    >>>
    >>>md[2] = 'b'                               # set changes key=2, value="b"
    >>>
    >>>print( md.keys(), md.values() )
    dict_keys(['a', 'd', 'f', 2]) dict_values([1, 4, 6, 'b'])
    >>>
    >>print( md.items() )
    dict_items([('a', 1), ('d', 4), ('f', 6), (2, 'b')])
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
__description__ = (
    "MirrorDict is a dictionary-like object that maintains a bi-directional mapping between keys and values."
)
__copyright__ = "Copyright (c) 2025 Scott E. Boyce"

__all__ = ["MirrorDict"]


# %% -----------------------------------------------------------------------------------------------


from collections.abc import Hashable, MutableMapping
import inspect


# %% -----------------------------------------------------------------------------------------------


class MirrorDict(MutableMapping):
    """
    A dictionary-like object that maintains a bi-directional/mirrored mapping
    between keys and values.

    A `MirrorDict` object ensures every key-value pair (`k:v`) added is mirrored as
    a value-key pair (`v:k`). This means you can look up either by key or by value,
    and the corresponding value or key will be returned.

    The order of the keys are preserved and the order of values are based on the keys.
    Methods, such as `keys()` and `values()` method return the items that were set
    initially as a key and value. That is, for a given key, updating its value keeps
    the original order of the keys but moves the new value to the end of values.
    However, setting an existing `v` as a key, moves the value to the end of the keys,
    removes the existing `k` from the keys and adds it to the end of the values.

    Key Features:
        - Automatically maintains a bi-directional mapping between keys and values.
            - Key-index lookup will return `value` for `key`, and return `key` for `value`.
        - Ensures all keys and values are hashable.
        - Supports standard dictionary operations (e.g., `keys`, `items`, `get`, `pop`).
        - What is stored initially as a key   is represented as a `dict_keys` and
          what is stored initially as a value is represented as a `dict_values`.
        - Changing either a key or value removes the old mirrored relationship
          to create the new one. If the key is changed, then the old one is
          removed and the new added to the end of keys().
        - Accepts initialization with mappings, iterables of key-value pairs, or keyword arguments.

    Constraints:
        - Keys and values must be hashable and unique.
        - Given a key-value pair, updating to a new key or new value replaces the
          existing key-value with the new one.

    Example Usage:
        >>> md = MirrorDict({'a': 1, 'b': 2})
        >>> print(md)
        MirrorDict({'a': 1, 'b': 2, 1: 'a', 2: 'b'})

        >>> md['c'] = 3
        >>> print(md[3])
        'c'

        >>> del md['a']
        >>> print(md)
        MirrorDict({'b': 2, 2: 'b'})

        >>> md.update({'x': 10}, y=20)
        >>> print(md)
        MirrorDict({'b': 2, 2: 'b', 'x': 10, 'y': 20, 10: 'x', 20: 'y'})

    """

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
            elif hasattr(arg, "__iter__") and not isinstance(arg, str):  # If it's an iterable of key-value pairs
                try:
                    for key, val in arg:
                        self._update(key, val)
                except ValueError as e:
                    raise TypeError(
                        f"MirrorDict.update() expected a dict-like or an iterable of key-value pairs but received: {arg}"
                    ) from e
            else:
                raise TypeError(
                    f"MirrorDict.update() expected a dict-like or an iterable of key-value pairs but received: {arg}"
                )

        for key, val in kwargs.items():
            self._update(key, val)
        return self

    def values(self):
        """
        Return an iterator over the values of the dictionary.
        """
        return self._key.values()

    # def order_values(self):
    #     """
    #     Ensures that the order of the values are one to one with the keys.
    #     """
    #     if self._key.values() != self.values.keys():
    #         self.values = {v: k for k, v in self._key.items()}
    #     return self

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
            key_old = self._val.pop(val_old)
            if key_old != key:
                self._key.pop(key_old)

        if key in self._val:  # key in _val, so need to reverse storage direction
            self._key.pop(self._val.pop(key))

        if val in self._val:  # val already defined, update key to it
            self._key.pop(self._val[val])

        if val in self._key:  # val in _key, so need to reverse storage direction
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

    def __ior__(self, other):  # dict concat with assignment, a |= b
        return self.update(other)

    def __or__(self, other):  # dict concat, a | b
        return MirrorDict(self, other)

    def __ror__(self, other):  # reverse dict concat, b | a
        return MirrorDict(other, self)

    def __eq__(self, other):  # compare self == other.
        if isinstance(other, MirrorDict):
            return self._key == other._key
        return self._key == other

    def __ne__(self, other):  # compare self != other.
        if isinstance(other, MirrorDict):
            return self._key != other._key
        return self._key != other

    def __lt__(self, other):  # compare self < other.
        raise TypeError(f"'<' not supported between instances of 'MirrorDict' and '{type(other)}'")

    def __le__(self, other):  # compare self <= other.
        raise TypeError(f"'<=' not supported between instances of 'MirrorDict' and '{type(other)}'")

    def __gt__(self, other):  # compare self > other.
        raise TypeError(f"'>' not supported between instances of 'MirrorDict' and '{type(other)}'")

    def __ge__(self, other):  # compare self >= other.
        raise TypeError(f"'>=' not supported between instances of 'MirrorDict' and '{type(other)}'")


# %% -----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    md = MirrorDict()  # Empty MirrorDict
    md["a"] = 1
    md["b"] = 2
    md["c"] = 3
    assert md["b"] == 2
    assert md[2] == "b"

    assert list(md.keys()) == ["a", "b", "c"]
    assert list(md.values()) == [1, 2, 3]

    md.update([("d", 4), ("e", 5)])
    md["f"] = 6

    assert list(md.keys()) == ["a", "b", "c", "d", "e", "f"]
    assert list(md.values()) == [1, 2, 3, 4, 5, 6]

    del md[5]
    pop3 = md.pop(3)

    assert pop3 == "c"

    assert list(md.keys()) == ["a", "b", "d", "f"]
    assert list(md.values()) == [1, 2, 4, 6]

    md[2] = "b"  # set command updates key=2 and value="b"

    assert list(md.keys()) == ["a", "d", "f", 2]
    assert list(md.values()) == [1, 4, 6, "b"]

    print("program completed successfully")
