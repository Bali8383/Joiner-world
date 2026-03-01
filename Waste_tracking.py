"""
Author: Brother Kovacs
Summary: Tesla Joiner program Individual project
Operation: This module performs an efficiency calculation by comparing 
the net area used in the project against the gross area of the raw 
lumber board to determine the percentage of material waste.
"""

def calculate_waste(net_area, gross_area):
    """Calculates percentage of material wasted.
    Parameters:
        net_area: Used surface area in m2.
        gross_area: Total board surface area in m2.
    Return: Waste percentage rounded to 1 decimal place.
    """
    if gross_area <= 0:
        return 0.0
    waste = ((gross_area - net_area) / gross_area) * 100
    return round(waste, 1)