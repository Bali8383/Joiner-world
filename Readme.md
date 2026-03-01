# 🪚 Joiner-world: Tesla Joiner Management OS

## 👨‍💻 Developer Profile
**Balázs Kovács** – *IT Support & System Administration Student (Ensign College)*

### 📝 Overview
An IT student currently developing a specialized, modular Python program for the woodworking industry to automate material, waste, and cutting layout calculations.

While this is a carpentry-focused command-line application, the core objective is to demonstrate **foundational IT Support, scripting, and system administration skills**: modular architecture, automated unit testing, robust error handling, and logical process optimization.

### 🛠️ Technologies & Methodologies
* **Language:** Python 3
* **Quality Assurance:** `pytest` framework for automated unit testing
* **UI/UX:** ANSI escape codes for a clean, professional, and readable command-line interface

### 💡 Key IT & Troubleshooting Skills Demonstrated
1. **Modular System Design:** Designed a highly maintainable system by separating core logic into independent modules (`Area_calculator.py`, `Material_cost.py`, `Cutting_list.py`, `Waste_tracking.py`).
2. **Automated Testing (QA):** Built an automated testing suite (`test_joiner.py`) to validate mathematical accuracy across all modules and prevent code regressions. This demonstrates a proactive approach to system stability.
3. **Error Handling & Input Validation:** Implemented `try-except` blocks in the main controller (`Joiner_program.py`) to catch `ValueError` exceptions. This ensures the program handles incorrect user inputs gracefully without crashing the system.
4. **Process Automation:** Automated complex manual calculations, significantly reducing human error in cost estimation and material efficiency tracking.
5. **Standardization Protocol:** Developed string manipulation logic to generate standardized uppercase workshop labels, mirroring the strict naming conventions required in IT asset management.

### 🎯 Why This Matters for IT Support
In IT Support and System Administration, efficiency and reliability are everything. This project proves my ability to take a complex operational problem, break it down into logical components, and build a crash-resistant, automated solution. The inclusion of unit tests and error handling highlights my commitment to preventing issues before they affect the end-user.

### 🚀 How to Run the Tool
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/Bali8383/Joiner-world.git](https://github.com/Bali8383/Joiner-world.git)
Ensure you have Python installed. Install the testing framework if you wish to run the unit tests:

Bash
pip install pytest
Launch the main operating system interface:

Bash
python Joiner_program.py
To run the automated unit tests and verify system integrity:

Bash
pytest test_joiner.py
