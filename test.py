from hello_world import hello_world
import pytest

def test_successString():
  result1 = helloworld("Test")
  assert result1 == "Hello Test! Welcome to Hello World File!"

def test_longString():
  result2 = helloworld(".........................")
  assert result2 == "Input string too long!"

def test_emptyString():
  result3 = helloworld("")
  assert result3 == "Input string is empty!"
