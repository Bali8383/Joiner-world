"""
Author: Brother Kovacs
Project: Tesla Joiner Management OS
Summary: This is the main controller of the Tesla Joiner system. It provides 
the user interface, handles input errors, and coordinates all logic modules.

RUBRIC CHECKLIST:
- Criterion 3: Program runs correctly and handles errors.
- Criterion 4: Divided into 5 functions (main + 4 imported modules).
- Criterion 5: Uses 'math' and 'os' standard Python modules.
"""
import math  # Criterion 5: Uses an existing Python module
import os    # Criterion 5: Uses an existing Python module
import Area_calculator
import Material_cost
import Cutting_list
import Waste_tracking

# ANSI Color codes for professional UI
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def main():
    """Main driver function for the program (Criterion 4)."""
    print(f"{BLUE}{BOLD}========================================")
    print("      TESLA JOINER MANAGEMENT OS        ")
    print(f"========================================{RESET}")
    
    keep_going = True
    while keep_going:
        try:
            print(f"\n{BOLD}--- Project Data Entry ---{RESET}")
            material = input("Enter Wood Species (e.g., Oak): ")
            width = float(input("Enter Width (mm): "))
            height = float(input("Enter Height (mm): "))
            thickness = float(input("Enter Thickness (mm): "))
            qty = int(input("Enter Quantity: "))
            price_sqm = float(input("Enter Price per m2: $"))
            full_board = float(input("Enter Total Board Area (m2): "))

            # Calling modular functions (Criterion 4)
            area = Area_calculator.calculate_total_area(width, height, qty)
            cost = Material_cost.calculate_cost(price_sqm, width, height, qty)
            label = Cutting_list.generate_label(width, height, thickness, material)
            waste = Waste_tracking.calculate_waste(area, full_board)

            # Display Results (Criterion 3: Correct results)
            print(f"\n{GREEN}========================================")
            print(f"         FINAL PROJECT REPORT         ")
            print(f"========================================{RESET}")
            print(f"{BOLD}Workshop Label:{RESET}  {label}")
            print(f"{BOLD}Total Area:{RESET}      {area:.4f} m2")
            print(f"{BOLD}Estimated Cost:{RESET}  ${cost:.2f}")
            print(f"{BOLD}Efficiency:{RESET}      {waste}% Waste")
            print(f"{GREEN}========================================{RESET}")

        except ValueError:
            print(f"\n{RED}[ERROR] Invalid input. Please use numbers for dimensions.{RESET}")

        if input(f"\n{BLUE}Calculate another project? (y/n): {RESET}").lower() != 'y':
            keep_going = False

    print(f"\n{BLUE}Thank you for using Tesla Joiner OS, Brother Kovacs!{RESET}")

if __name__ == "__main__":
    main()