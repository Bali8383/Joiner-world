"""
Author: Brother Kovacs
Summary: Tesla Joiner program Individual project
Operation: This module performs the mathematical conversion of millimeter 
dimensions into square meters and calculates the total surface area 
for a specific number of wood pieces.
"""

def calculate_total_area(width_mm, height_mm, qty):
    """Calculates total surface area in square meters.
    Parameters:
        width_mm: Width of one piece.
        height_mm: Height of one piece.
        qty: Total number of pieces.
    Return: Total area in m2 rounded to 4 decimals.
    """
    return round((width_mm / 1000) * (height_mm / 1000) * qty, 4)