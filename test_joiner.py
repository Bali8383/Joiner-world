"""
Author: Brother Kovacs
Summary: Tesla Joiner program Individual project
Operation: This program performs automated unit testing for the Tesla Joiner 
suite. it uses the pytest framework to execute multiple test cases against 
each logic module (Cost, Area, Label, and Waste) to ensure mathematical 
accuracy and prevent coding regressions.
"""
import pytest
import Area_calculator
import Material_cost
import Cutting_list
import Waste_tracking

def test_calculate_total_area():
    assert Area_calculator.calculate_total_area(1000, 1000, 1) == 1.0
    assert Area_calculator.calculate_total_area(500, 500, 4) == 1.0

def test_calculate_cost():
    assert Material_cost.calculate_cost(50, 1000, 1000, 1) == 50.0
    assert Material_cost.calculate_cost(20, 500, 500, 2) == 10.0

def test_generate_label():
    assert "OAK" in Cutting_list.generate_label(1000, 500, 18, "Oak")
    assert "PINE" in Cutting_list.generate_label(800, 400, 12, "Pine")

def test_calculate_waste():
    assert Waste_tracking.calculate_waste(1.5, 3.0) == 50.0
    assert Waste_tracking.calculate_waste(2.0, 2.0) == 0.0

if __name__ == "__main__":
    # Allows the test to run via the "Run" button
    pytest.main(["-v", __file__])