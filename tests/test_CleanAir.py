import pytest
import CleanAir

@pytest.fixture
def my_clean_air():
  return CleanAir = CleanAir()

def test_C1():
  assert my_clean_air.C1 == 10
