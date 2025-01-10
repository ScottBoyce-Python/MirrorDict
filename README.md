# MirrorDict: Hashing both key and value

<p align="left">
  <img src="https://github.com/ScottBoyce-Python/MirrorDict/actions/workflows/MirrorDict-pytest.yml/badge.svg" alt="Build Status" height="20">
</p>


## About

MirrorDict is a Python object that hashes both the key and value for bidirectional lookups. That is, `x[key] = value` and `x[value]=key`. Since both the value and key are hashed they must be immutable or have the \__hash__ dunder method set.



## Features

- TBA

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

  

## Result Class

### Initialization

```python

```

### Attributes and Methods

These are select attributes and methods built into `Result` object. For a full listing please see the Result docstr.

#### Attributes

```    

```

#### Methods

``` 

```

  

## Usage

Below are examples showcasing how to create and interact with a `MirrorDict`.

TBA

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
