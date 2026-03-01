"""
Author: Brother Kovacs
Summary: Tesla Joiner program Individual project
Operation: This module calculates the total financial investment required 
for the wood by multiplying the calculated square meter area by the 
current market price per square meter.
"""

def calculate_cost(sqm_price, width_mm, height_mm, qty):
    """Computes total financial cost of wood panels.
    Parameters:
        sqm_price: Cost per square meter.
        width_mm: Width in mm.
        height_mm: Height in mm.
        qty: Quantity of pieces.
    Return: Total cost rounded to 2 decimal places.
    """
    area_m2 = (width_mm / 1000) * (height_mm / 1000) * qty
    return round(area_m2 * sqm_price, 2)