#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import isbn_validator
from isbn_validator import isbn_validator as iv


# Tests =======================================================================
def test_clean_isbn():
    assert iv._clean_isbn("asdfg80-86-0-56-31-7asd") == [8,0,8,6,0,5,6,3,1,7]
    assert iv._clean_isbn("a80-86-0-56-31-7asdx") == [8,0,8,6,0,5,6,3,1,7,10]
    assert iv._clean_isbn("X") == [10]


def test_get_isbn10_checksum():
    assert isbn_validator.get_isbn10_checksum("80-86056-31") == 7
    assert isbn_validator.get_isbn10_checksum("80-904248-2") == 1

    assert isbn_validator.get_isbn10_checksum("80-904248-3") != 1
    assert isbn_validator.get_isbn10_checksum("80-904248-6") != 1


def test_is_isbn10_valid():
    assert isbn_validator.is_isbn10_valid("80-85892-15-4")
    assert isbn_validator.is_isbn10_valid("80-86056-31-7")
    assert isbn_validator.is_isbn10_valid("80-251-0225-4")

    assert not isbn_validator.is_isbn10_valid("80-251-0225-x")
    assert not isbn_validator.is_isbn10_valid("80-85892-25-4")
    assert not isbn_validator.is_isbn10_valid("80-85892-25-416456")
    assert not isbn_validator.is_isbn10_valid("80-8589")


def test_get_isbn13_checksum():
    assert isbn_validator.get_isbn13_checksum("978-80-86056-31") == 9
    assert isbn_validator.get_isbn13_checksum("978-80-904248-2") == 1

    assert isbn_validator.get_isbn13_checksum("978-80-904248-3") != 1
    assert isbn_validator.get_isbn13_checksum("978-80-904248-6") != 1


def test_is_isbn13_valid():
    assert isbn_validator.is_isbn13_valid("978-80-86056-31-9")
    assert isbn_validator.is_isbn13_valid("978-80-904248-2-1")

    assert not isbn_validator.is_isbn13_valid("978-80-86056-31-5")
    assert not isbn_validator.is_isbn13_valid("978-80-904248-2-7")
    assert not isbn_validator.is_isbn13_valid("978-80-934248-2-7")
    assert not isbn_validator.is_isbn13_valid("978-80-9345644248-2-7")
    assert not isbn_validator.is_isbn13_valid("978-80-9")


def test_is_valid_isbn():
    assert isbn_validator.is_valid_isbn("80-85892-15-4")
    assert isbn_validator.is_valid_isbn("80-86056-31-7")
    assert isbn_validator.is_valid_isbn("80-251-0225-4")
    assert isbn_validator.is_valid_isbn("978-80-86056-31-9")
    assert isbn_validator.is_valid_isbn("978-80-904248-2-1")

    assert not isbn_validator.is_valid_isbn("978-80-86056-31-5")
    assert not isbn_validator.is_valid_isbn("978-80-904248-2-7")
    assert not isbn_validator.is_valid_isbn("978-80-934248-2-7")
    assert not isbn_validator.is_valid_isbn("978-80-9345644248-2-7")
    assert not isbn_validator.is_valid_isbn("978-80-9")
    assert not isbn_validator.is_valid_isbn("80-251-0225-x")
    assert not isbn_validator.is_valid_isbn("80-85892-25-4")
    assert not isbn_validator.is_valid_isbn("80-85892-25-416456")
    assert not isbn_validator.is_valid_isbn("80-8589")
