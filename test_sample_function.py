import pytest
from unittest import mock
from sample_function import padding

@mock.patch("sample_function.randint",
return_value=7,
autospec=True)
def test_padding(mock_randint):
  assert padding(5) == 12

# make sure you are importing the method you want mock 
# make sure at patch you are calling the library patch 
# return_value will be returned output of library that you are mocking 
# and will be passed when ever library called in the function 
