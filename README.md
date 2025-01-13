# MirrorDict Module

<p align="left">
  <img src="https://github.com/ScottBoyce-Python/MirrorDict/actions/workflows/MirrorDict-pytest.yml/badge.svg" alt="Build Status" height="20">
</p>
MirrorDict is a Python module that provides a bi-directional dictionary-like object by maintaining a mirrored relationship between keys and values. This results in an efficient key-index lookup that will return the value for key, and return key for value.

## Features

- **Bi-directional Mapping**: Automatically mirrors `{k:v}` pairs as `{v:k}` pairs.
  - Key-index lookup will return `v` for `k`, and return `k` for `v`. 

- **Standard Dictionary Operations**: Supports operations like `keys`, `items`, `get`, `pop`, ...

- **Hashable and Unique**: Requires both keys and values to be hashable  
  and unique to maintain the mirrored lookup.

- **Order Preservation**: Preserves the order of keys and values based on the order keys are added.

## About

`MirrorDict` is a dictionary-like object that maintains a bi-directional/mirrored mapping between keys and values. A `MirrorDict` object ensures every key-value pair (`{k:v}`) added is mirrored as a value-key pair (`{v:k}`). This means you can look up either by key or by value, and the corresponding value or key will be returned.  Since both the `k` and `v` are hashed, `MirrorDict` requires that both be hashable and unique.

The order of the keys are preserved and the order of values are based on the keys. Methods, such as `keys()` and `values()` method return the items that were set initially as a `k` and `v` respectively (i.e. `md[k]=v` stores `k` in the keys and `v` in the values). Changing either a key or value removes the old mirrored relationship to create the new one. If the key is changed, then the old one is removed and the new added to the end of `keys()`.

For example,  
`md[k] = v`, makes `k` the key and `v` the value, and, `md[k] == v` and `md[v] == k`; and  
`md[k] = v2`, updates the key `k` to the value `v2`;    
`md[v2] = k`, removes `k` in the keys and adds `v2` to the end of keys and adds `k`  to the end of values.

### Simple Use Case

  ```python
  from MirrorDict import MirrorDict
  
  md = MirrorDict() # Empty MirrorDict               ➣ MirrorDict({})
  md['a'] = 1       # Add k='a' associated with v=1  ➣ MirrorDict({'a': 1})
  md['b'] = 2       # Add k='b' associated with v=2  ➣ MirrorDict({'a': 1, 'b': 2})
  md['c'] = 3       # Add k='c' associated with v=3  ➣ MirrorDict({'a': 1, 'b': 2, 'c': 3})
  
  md['b']           # returns 2
  md[2]             # returns 'b'
  
  md.keys()         # ➣ dict_keys(  ['a', 'b', 'c'])
  md.values()       # ➣ dict_values([ 1,   2,   3 ])
  
  md['b'] = 9       # Change k='b' to have v=9        ➣ MirrorDict({'a': 1, 'b': 9, 'c': 3})
  md.keys()         # ➣ dict_keys(  ['a', 'b', 'c'])
  md.values()       # ➣ dict_values([ 1,   9 ,   3])
  
  md['b']           # returns 9
  md[9]             # returns 'b'; note md[2] no longer exists and will raise an exception
  md['c']           # returns 3
  md[3]             # returns 'c'
  
  md[9] = 'b'       # Replace k='b' with k=9 and v='b' ➣ MirrorDict({'a': 1, 'c': 3, 9: 'b'})
  md.keys()         # ➣ dict_keys(  ['a', 'c',  9 ])
  md.values()       # ➣ dict_values([ 1 ,   3, 'b'])
  
  md['b']           # returns 9
  md[9]             # returns 'b'
  ```



## Installation
To install the module

```bash
pip install --upgrade git+https://github.com/ScottBoyce-Python/MirrorDict.git
```

or you can clone the respository with
```bash
git clone https://github.com/ScottBoyce-Python/MirrorDict.git
```
then rename the file `MirrorDict/__init__.py` to  `MirrorDict/MirrorDict.py` and move `MirrorDict.py` to wherever you want to use it.

  

## MirrorDict Class

### Initialization

The MirrorDict class supports the same initialization that `dict` supports. In addition to this, it can also support more than one argument to define multiple groups of `k:v` pairs (`dict` only allows at most one argument). The order keys are stored in the order that `k:v` pairs are added, with the last duplicate `k` or `v`, superseding the previous ones.

```python
from MirrorDict import MirrorDict

# initialize an empty MirrorDict
md0 = MirrorDict()  # = MirrorDict({})

# initialize 3 pairs as list of tuples.
# keys  =  ['a','b','c']
# values = [ 1,  2,  3 ]
md1 = MirrorDict([('a', 1), ('b', 2), ('c', 3)])  # = MirrorDict({'a': 1, 'b': 2, 'c': 3})

# initialize two lists containing pairs as tuples.
md2 = MirrorDict( [('a', 1), ('b', 2), ('c', 3)], [('d', 4), ('e', 5)] )  
#   = MirrorDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

# initialize with zip to get list of tuples.
md3 = MirrorDict(zip(['d','e','f'], [4, 5, 6]))  # = MirrorDict({'d': 4, 'e': 5, 'f': 6})

# initialize with a dict and/or another MirrorDict
d = {'a': 1, 'b': 2, 'c': 3}

md4 = MirrorDict(d)      # = MirrorDict({'a': 1, 'b': 2, 'c': 3})
md5 = MirrorDict(md3)    # = MirrorDict({'d': 4, 'e': 5, 'f': 6})
md6 = MirrorDict(d, md3) # = MirrorDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
md7 = d | md5            # = MirrorDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
```

### Attributes and Methods

All the methods and attributes that are part of `dict` are also part of `MirrorDict`. Internally MirrorDict uses two dict attributes to hold the key-value (`{k:v}`) and value-key (`{v:k}`) mirrored relationship. `{k:v}` is stored in the `_key` attribute and `{v:k}` is stored in the `_val` attribute .

## Usage

Below are examples showcasing how to create and interact with a `MirrorDict`.

```python
from MirrorDict import MirrorDict

md = MirrorDict()    # Empty MirrorDict
md["a"] = 1          # = MirrorDict({'a': 1})
md["b"] = 2          # = MirrorDict({'a': 1, 'b': 2})
md["c"] = 3          # = MirrorDict({'a': 1, 'b': 2, 'c': 3})
assert md["b"] == 2 
assert md[2]   == "b"

assert list(md.keys()  ) == ["a", "b", "c"]
assert list(md.values()) == [ 1,   2,   3 ]

md.update([("d", 4), ("e", 5)])  # = MirrorDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
md["f"] = 6                      # = MirrorDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

assert list(md.keys()  ) == ["a", "b", "c", "d", "e", "f"]
assert list(md.values()) == [ 1,   2,   3,   4,   5,   6 ]

del md[5]
pop3 = md.pop(3)

assert pop3 == "c"

assert list(md.keys()  ) == ["a", "b", "d", "f"]
assert list(md.values()) == [ 1,   2,   4,   6 ]

md[2] = "b"  # set command updates key=2 and value="b"

assert list(md.keys()  ) == ["a", "d", "f",  2 ]
assert list(md.values()) == [ 1,   4,   6,  "b"]

for k in md:
    print(k)  # prints: 'a', 'd', 'f', then 2

for k, v in md.items():
    print(f"{k}:{v}")  # prints: 'a':1, 'd':4, 'f':6, then 2:'b'
```

  

## Testing

This project uses `pytest` and `pytest-xdist` for testing. Tests are located in the `tests` folder. To run tests, install the required packages and execute the following command:

```bash
pip install pytest pytest-xdist

pytest  # run all tests, note options are set in the pyproject.toml file
```

&nbsp; 

Note, that the [pyproject.toml](pyproject.toml) contains the flags used for pytest.

  

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author
Scott E. Boyce
