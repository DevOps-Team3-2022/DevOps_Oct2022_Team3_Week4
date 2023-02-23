from helloworld import hello_world
import pytest

def test_test():
  result1 = hello_world("Test")
  assert result1 == "Hello Test! Welcome to Hello World File!"

def test_toolong():
  result2 = hello_world(".........................")
  assert result2 == "Input string too long!"

def test_empty():
  result3 = hello_world("")
  assert result3 == "Input string is empty!"
