# Mid-term Project: Signals and Systems (Python)

## Description
This project shows how to generate and manipulate simple signals using Python and NumPy.  
It is designed for a **mid-term evaluation** in a Signals and Systems course.

The code includes:
- Functions to generate signals (sine, unit step)
- Functions to modify signals (time shift, time scaling)
- Example script to plot and save results

## Project structure
.
├── signals.py # Functions for signals
├── script.py # Example script
├── README.md # Documentation
└── pyproject.toml

## Functions
### Signal generation
- **generate_sine()**: creates a sampled sine wave  
- **generate_unit_step()**: creates a unit step signal

### Signal operations
- **time_shift()**: shifts a signal in time (left or right)  
- **time_scale()**: compresses or stretches a signal in time

### Utility
- **plot_signal()**: plots one or more signals and saves the figure

## How to run
1. Install Python and the required packages:
''pip install numpy matplotlib''
2. Run the script:
'' python script.py ''
3. Figures will be saved in the plots/ folder.

