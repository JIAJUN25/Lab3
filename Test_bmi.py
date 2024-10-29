import pytest
import Lab2.bmi as bmi

def test_bmi_under_weight():
    result_bmi, classification = bmi.calculate_bmi(1.75, 50)
    assert classification == -1  # Classification for underweight
    assert result_bmi < 18.5  # Verify BMI is less than 18.5

def test_bmi_normal_weight():
    result_bmi, classification = bmi.calculate_bmi(1.75, 68)
    assert classification == 0
    assert 18.5 <= result_bmi <= 25.0

def test_bmi_over_weight():
    result_bmi, classification = bmi.calculate_bmi(1.75, 85)
    assert classification == 1
    assert result_bmi > 25.0 
