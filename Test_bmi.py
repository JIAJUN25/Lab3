import pytest
import Lab2.bmi as bmi  # Adjust the import based on your folder structure

def test_calculate_bmi_underweight():
    result_bmi, classification = bmi.calculate_bmi(1.75, 50)
    assert classification == -1  # Underweight
    assert result_bmi < 18.5

def test_calculate_bmi_normal_weight():
    result_bmi, classification = bmi.calculate_bmi(1.75, 68)
    assert classification == 0  # Normal weight
    assert 18.5 <= result_bmi <= 25.0

def test_calculate_bmi_overweight():
    result_bmi, classification = bmi.calculate_bmi(1.75, 85)
    assert classification == 1  # Overweight
    assert result_bmi > 25.0
