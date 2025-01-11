import pytest
from MirrorDict import MirrorDict


def test_initialization():
    md = MirrorDict({"a": 1, "b": 2})
    assert md["a"] == 1
    assert md[1] == "a"
    assert md["b"] == 2
    assert md[2] == "b"


def test_empty_initialization():
    md = MirrorDict()
    assert len(md) == 0


def test_add_and_lookup():
    md = MirrorDict()
    md["x"] = 10
    md["y"] = 20
    md["z"] = 30
    assert md["x"] == 10
    assert md[10] == "x"
    assert md["y"] == 20
    assert md[20] == "y"
    assert md["z"] == 30
    assert md[30] == "z"


def test_add_and_update_and_lookup():
    md = MirrorDict()
    md["x"] = 10
    md["y"] = 20
    md["z"] = 30

    assert md["x"] == 10
    assert md["y"] == 20
    assert md["z"] == 30
    assert md[10] == "x"
    assert md[20] == "y"
    assert md[30] == "z"

    md[20] = "a"  # reverses key direction and updates to "a"

    assert md["x"] == 10
    assert md["z"] == 30
    assert md["a"] == 20
    assert md[10] == "x"
    assert md[30] == "z"
    assert md[20] == "a"


def test_key_order():
    md = MirrorDict()
    md["x"] = 10
    md["y"] = 20
    md["z"] = 30

    assert md["x"] == 10
    assert md["y"] == 20
    assert md["z"] == 30
    assert md[10] == "x"
    assert md[20] == "y"
    assert md[30] == "z"

    md[20] = "a"  # reverses key direction and updates to "a"

    assert md["x"] == 10
    assert md["z"] == 30
    assert md["a"] == 20
    assert md[10] == "x"
    assert md[30] == "z"
    assert md[20] == "a"


def test_update_with_mapping():
    md = MirrorDict({"a": 1})
    md.update({"b": 2, "c": 3})
    assert md["b"] == 2
    assert md["c"] == 3
    assert md[2] == "b"
    assert md[3] == "c"


def test_update_with_iterable():
    md = MirrorDict({"a": 1})
    md.update([("b", 2), ("c", 3)])
    assert md["b"] == 2
    assert md["c"] == 3
    assert md[2] == "b"
    assert md[3] == "c"


def test_update_with_kwargs():
    md = MirrorDict({"a": 1})
    md.update(b=2, c=3)
    assert md["b"] == 2
    assert md["c"] == 3
    assert md[2] == "b"
    assert md[3] == "c"


def test_clear():
    md = MirrorDict({"a": 1, "b": 2})
    md.clear()
    assert len(md) == 0
    assert list(md.keys()) == []
    assert list(md.values()) == []


def test_copy():
    md = MirrorDict({"a": 1, "b": 2})
    md_copy = md.copy()
    assert md_copy == md
    assert id(md_copy) != id(md)


def test_non_hashable_key_or_value():
    md = MirrorDict()
    with pytest.raises(TypeError):
        md[["a"]] = 1
    with pytest.raises(TypeError):
        md["a"] = {"key": "value"}


def test_pop():
    md = MirrorDict({"a": 1, "b": 2})
    assert md.pop("a") == 1
    assert "a" not in md
    assert 1 not in md
    with pytest.raises(KeyError):
        md.pop("c")


def test_pop_with_default():
    md = MirrorDict({"a": 1})
    assert md.pop("b", "default") == "default"


def test_pop_nonexistent_key_raises():
    md = MirrorDict({"a": 1})
    with pytest.raises(KeyError):
        md.pop("b")


def test_popitem():
    md = MirrorDict({"a": 1, "b": 2})
    key, value = md.popitem()
    assert key in ["a", "b"]
    assert value in [1, 2]
    assert key not in md
    assert value not in md


def test_popitem_empty():
    md = MirrorDict()
    with pytest.raises(KeyError):
        md.popitem()


def test_reversed():
    md = MirrorDict({"a": 1, "b": 2})
    assert list(md.reversed()) == ["b", "a"]


def test_setdefault_existing_key():
    md = MirrorDict({"a": 1})
    assert md.setdefault("a", 3) == 1


def test_setdefault_new_key():
    md = MirrorDict({"a": 1})
    assert md.setdefault("b", 2) == 2
    assert md["b"] == 2
    assert md[2] == "b"


def test_contains():
    md = MirrorDict({"a": 1, "b": 2})
    assert "a" in md
    assert 1 in md
    assert "c" not in md
    assert 3 not in md


def test_len():
    md = MirrorDict({"a": 1, "b": 2})
    assert len(md) == 2


def test_iter():
    md = MirrorDict({"a": 1, "b": 2})
    assert list(iter(md)) == ["a", "b"]


def test_eq():
    md1 = MirrorDict({"a": 1, "b": 2})
    md2 = MirrorDict({"a": 1, "b": 2})
    assert md1 == md2


def test_ne():
    md1 = MirrorDict({"a": 1, "b": 2})
    md2 = MirrorDict({"a": 1, "b": 3})
    assert md1 != md2


def test_ior():
    md1 = MirrorDict({"a": 1})
    md2 = MirrorDict({"b": 2})
    md1 |= md2
    assert md1["b"] == 2
    assert md1[2] == "b"


def test_or():
    md1 = MirrorDict({"a": 1})
    md2 = MirrorDict({"b": 2})
    result = md1 | md2
    assert result["b"] == 2
    assert result[2] == "b"


def test_ror():
    md1 = MirrorDict({"b": 2})
    md2 = {"a": 1} | md1
    assert md2["a"] == 1
    assert md2["b"] == 2


def test_bidirectional_mapping():
    md = MirrorDict({"a": 1, "b": 2})
    assert md["a"] == 1
    assert md[1] == "a"
    assert md["b"] == 2
    assert md[2] == "b"


def test_update_and_iterables():
    md = MirrorDict({"a": 1})
    md.update([("b", 2), ("c", 3)])
    assert md["b"] == 2
    assert md[2] == "b"


def test_setdefault():
    md = MirrorDict({"a": 1})
    assert md.setdefault("b", 2) == 2
    assert md["b"] == 2
    assert md.setdefault("a", 3) == 1


def test_clear_empty_dict():
    md = MirrorDict()
    md.clear()
    assert len(md) == 0


def test_copy_independence():
    md = MirrorDict({"a": 1})
    md_copy = md.copy()
    md["b"] = 2
    assert "b" not in md_copy


def test_keys_values_items_consistency():
    md = MirrorDict({"a": 1, "b": 2})
    assert list(md.keys()) == ["a", "b"]
    assert list(md.values()) == [1, 2]
    assert list(md.items()) == [("a", 1), ("b", 2)]


def test_update_with_conflicting_keys():
    md = MirrorDict({"a": 1})
    md.update({"a": 2})  # Changes value for "a"
    assert md["a"] == 2
    assert md[2] == "a"
    assert 1 not in md  # Old mirrored value should be removed


def test_update_with_no_args():
    md = MirrorDict({"a": 1})
    md.update()
    assert md["a"] == 1  # Nothing changes


def test_reversed_empty():
    md = MirrorDict()
    assert list(md.reversed()) == []


def test_popitem_respects_order():
    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    assert md.popitem() == ("c", 3)  # Last added is removed
    assert md.popitem() == ("b", 2)
    assert md.popitem() == ("a", 1)
    assert len(md) == 0


def test_str():
    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    assert str(md) == "MirrorDict({'a': 1, 'b': 2, 'c': 3})"


def test_repr():
    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    assert str(md) == "MirrorDict({'a': 1, 'b': 2, 'c': 3})"


def test_str_pop():
    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.pop(2)
    assert str(md) == "MirrorDict({'a': 1, 'c': 3})"


def test_repr_pop():
    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.pop(2)
    assert repr(md) == "MirrorDict({'a': 1, 'c': 3})"


def test_str_popitem():
    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.popitem()
    assert str(md) == "MirrorDict({'a': 1, 'b': 2})"


def test_repr_popitem():
    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.popitem()
    assert repr(md) == "MirrorDict({'a': 1, 'b': 2})"


def test_str_empty():
    md = MirrorDict()
    assert str(md) == "MirrorDict({})"

    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.clear()
    assert str(md) == "MirrorDict({})"

    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.popitem()
    md.popitem()
    md.popitem()
    assert str(md) == "MirrorDict({})"


def test_repr_empty():
    md = MirrorDict()
    assert repr(md) == "MirrorDict({})"

    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.clear()
    assert repr(md) == "MirrorDict({})"

    md = MirrorDict({"a": 1, "b": 2, "c": 3})
    md.popitem()
    md.popitem()
    md.popitem()
    assert repr(md) == "MirrorDict({})"
