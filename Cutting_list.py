"""
Author: Brother Kovacs
Summary: Tesla Joiner program Individual project
Operation: This module performs string manipulation to generate a standardized, 
uppercase workshop label that identifies the wood species and exact 
cutting dimensions for the shop floor.
"""

def generate_label(w, h, t, material):
    """Formats a standardized workshop label string.
    Parameters:
        w, h, t: Dimensions in mm.
        material: Wood species name.
    Return: A formatted uppercase string.
    """
    return f"{material.upper()}: {w}x{h}x{t}mm"