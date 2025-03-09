import pytest
from src.temperatura import Temperatura

@pytest.fixture
def temperatura_0_celcius():
    return Temperatura(0, "Celsius")

@pytest.fixture
def temperatura_32_celcius():
    return Temperatura(32, "Celsius")

@pytest.fixture
def temperatura_0_fahrenheit():
    return Temperatura(0, "Fahrenheit")

@pytest.fixture
def temperatura_32_fahrenheit():
    return Temperatura(32, "Fahrenheit")

def test_temperatura_e_classe(temperatura_0_celcius):
    assert type(temperatura_0_celcius) == Temperatura

def test_temperatura_0_celcius_para_fahrenheit(temperatura_0_celcius):
    assert temperatura_0_celcius.em_fahrenheit() == 32

def test_temperatura_32_celcius_para_89_6_fahrenheit(temperatura_32_celcius):
    assert temperatura_32_celcius.em_fahrenheit() == 89.6

def test_temperatura_0_fahrenheit_para_0_fahrenheit(temperatura_0_fahrenheit):
    assert temperatura_0_fahrenheit.em_fahrenheit() == 0


def test_temperatura_0_fahrenheit_para_17_8celsius(temperatura_0_fahrenheit):
    assert temperatura_0_fahrenheit.em_celsius() == -17.8


def test_temperatura_32_fahrenheit_para_0_celsius(temperatura_32_fahrenheit):
    assert temperatura_32_fahrenheit.em_celsius() == 0

