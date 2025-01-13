import pytest
from MirrorDict import MirrorDict


def test_empty_initialization():
    md = MirrorDict()
    assert len(md) == 0
    assert md == MirrorDict()


def test_initialization():
    md = MirrorDict({"a": 1, "b": 2})
    assert md["a"] == 1
    assert md[1] == "a"
    assert md["b"] == 2
    assert md[2] == "b"


def test_initialization_kwargs():
    md = MirrorDict(a=1, b=2, c=3)  # = MirrorDict({'a': 1, 'b': 2, 'c': 3})

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert len(md) == 3
    assert md == MirrorDict(a=1, b=2, c=3)


def test_initialization_zip_lists():
    md = MirrorDict(zip(["a", "b", "c"], [1, 2, 3]))

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert len(md) == 3
    assert md == MirrorDict(a=1, b=2, c=3)


def test_initialization_dict():
    d = {"a": 1, "b": 2, "c": 3}
    md = MirrorDict(d)

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert len(md) == 3
    assert md == MirrorDict(a=1, b=2, c=3)


def test_initialization_mirrordict():
    md1 = MirrorDict(a=1, b=2, c=3)
    md2 = MirrorDict(md1)

    assert md2["a"] == 1
    assert md2["b"] == 2
    assert md2["c"] == 3
    assert md2[1] == "a"
    assert md2[2] == "b"
    assert md2[3] == "c"
    assert len(md1) == 3
    assert md1 == md2


def test_initialization_list_of_tuples():
    # initialize 3 pairs as list of tuples.
    # keys  =  ['a','b','c']
    # values = [ 1,  2,  3 ]
    md = MirrorDict([("a", 1), ("b", 2), ("c", 3)])  # = MirrorDict({'a': 1, 'b': 2, 'c': 3})

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert len(md) == 3
    assert md == MirrorDict(a=1, b=2, c=3)


def test_initialization_multiple_lists_of_tuples():
    md = MirrorDict([("a", 1), ("b", 2), ("c", 3)], [("d", 4), ("e", 5)], [("f", 6), ("g", 7)])

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md["d"] == 4
    assert md["e"] == 5
    assert md["f"] == 6
    assert md["g"] == 7
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert md[4] == "d"
    assert md[5] == "e"
    assert md[6] == "f"
    assert md[7] == "g"
    assert len(md) == 7
    assert md == MirrorDict(a=1, b=2, c=3, d=4, e=5, f=6, g=7)


def test_initialization_multiple_zip_lists():
    md = MirrorDict(zip(["a", "b", "c"], [1, 2, 3]), zip(["d", "e", "f"], [4, 5, 6]))

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md["d"] == 4
    assert md["e"] == 5
    assert md["f"] == 6
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert md[4] == "d"
    assert md[5] == "e"
    assert md[6] == "f"
    assert len(md) == 6
    assert md == MirrorDict(a=1, b=2, c=3, d=4, e=5, f=6)


def test_initialization_input_mixture1():
    md = MirrorDict(zip(["a", "b", "c"], [1, 2, 3]), [("d", 4), ("e", 5)], f=6, g=7)

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md["d"] == 4
    assert md["e"] == 5
    assert md["f"] == 6
    assert md["g"] == 7
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert md[4] == "d"
    assert md[5] == "e"
    assert md[6] == "f"
    assert md[7] == "g"
    assert len(md) == 7
    assert md == MirrorDict(a=1, b=2, c=3, d=4, e=5, f=6, g=7)


def test_initialization_input_mixture2():
    d = {"f": 6, "g": 7, "h": 8}
    md = MirrorDict(zip(["a", "b", "c"], [1, 2, 3]), [("d", 4), ("e", 5)], d, i=9, j=10)

    assert md["a"] == 1
    assert md["b"] == 2
    assert md["c"] == 3
    assert md["d"] == 4
    assert md["e"] == 5
    assert md["f"] == 6
    assert md["g"] == 7
    assert md["h"] == 8
    assert md["i"] == 9
    assert md["j"] == 10
    assert md[1] == "a"
    assert md[2] == "b"
    assert md[3] == "c"
    assert md[4] == "d"
    assert md[5] == "e"
    assert md[6] == "f"
    assert md[7] == "g"
    assert md[8] == "h"
    assert md[9] == "i"
    assert md[10] == "j"
    assert len(md) == 10
    assert md == MirrorDict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)


def test_initialization_input_mixture3():
    md1 = MirrorDict(zip(["a", "b", "c"], [1, 2, 3]))
    d = dict([("d", 4), ("e", 5)])
    md2 = dict([("f", 6), ("g", 7)])

    md3 = MirrorDict(md1, d, md2, [("h", 8), ("i", 9)], j=10, k=11, l=12)

    assert md3["a"] == 1
    assert md3["b"] == 2
    assert md3["c"] == 3
    assert md3["d"] == 4
    assert md3["e"] == 5
    assert md3["f"] == 6
    assert md3["g"] == 7
    assert md3["h"] == 8
    assert md3["i"] == 9
    assert md3["j"] == 10
    assert md3["k"] == 11
    assert md3["l"] == 12
    assert md3[1] == "a"
    assert md3[2] == "b"
    assert md3[3] == "c"
    assert md3[4] == "d"
    assert md3[5] == "e"
    assert md3[6] == "f"
    assert md3[7] == "g"
    assert md3[8] == "h"
    assert md3[9] == "i"
    assert md3[10] == "j"
    assert md3[11] == "k"
    assert md3[12] == "l"
    assert len(md3) == 12
    assert md3 == MirrorDict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12)


def test_initialization_error():
    with pytest.raises(TypeError):
        MirrorDict("a", 1)

    with pytest.raises(TypeError):
        MirrorDict(("a", 1))

    with pytest.raises(TypeError):
        MirrorDict([("a", 1), "b", 2, ("c", 3)])

    with pytest.raises(TypeError):
        MirrorDict([("a", 1), ("b", 2)], "c", 3)


def test_initialization_str_error():
    with pytest.raises(TypeError):
        MirrorDict("ab", 1)

    with pytest.raises(TypeError):
        MirrorDict(("ab", 1))

    with pytest.raises(TypeError):
        MirrorDict([("a", 1), "ab", 2, ("c", 3)])

    with pytest.raises(TypeError):
        MirrorDict([("a", 1), ("b", 2)], "cat", 3)


def test_initialization_or():
    d1 = dict(zip(["a", "b", "c"], [1, 2, 3]))
    d2 = dict(zip(["d", "e", "f", "g"], [4, 5, 6, 7]))
    md1 = MirrorDict(d1)
    md2 = MirrorDict(d2)

    md3 = md1 | md2
    md4 = d1 | md2
    md5 = md1 | d2
    md6 = d1 | d2

    assert md3["a"] == 1
    assert md3["b"] == 2
    assert md3["c"] == 3
    assert md3["d"] == 4
    assert md3["e"] == 5
    assert md3["f"] == 6
    assert md3["g"] == 7
    assert md3[1] == "a"
    assert md3[2] == "b"
    assert md3[3] == "c"
    assert md3[4] == "d"
    assert md3[5] == "e"
    assert md3[6] == "f"
    assert md3[7] == "g"
    assert len(md3) == 7
    assert md3 == MirrorDict(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
    assert md3 == md4
    assert md3 == md5
    assert md3 == md6
