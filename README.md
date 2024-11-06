# level2pressure

`level2pressure` is a Python package designed to convert vertical coordinates in CMIP6 climate model data to pressure levels. This is particularly useful for models that use hybrid sigma or hybrid height coordinates, allowing users to interpolate their data to standard pressure levels for easier comparison and analysis.

## Features

- Identify vertical coordinate types in NetCDF files (e.g., hybrid height, hybrid sigma-pressure).
- Convert height levels to pressure levels using the U.S. Standard Atmosphere.
- Interpolate data to a user-specified list of standard pressure levels.
- Command-line interface (CLI) for easy use in workflows.

## Directory Structure

```plaintext
level2pressure/
├── __init__.py
├── cmip6_interp_to_pressure_level.py    # CLI script to convert vertical coordinates to pressure levels
├── core.py                              # Main functions for coordinate transformations
├── utils.py                             # Utility functions, including coordinate identification
└── requirements.txt                     # Package dependencies

## Installation

### Prerequisites
- **Python 3.7+**
- The following Python libraries (listed in `requirements.txt`):
  - `xarray`
  - `numpy`
  - `netCDF4`
  - `metpy`

### Installation Steps
1. Clone the repository (or download it as a zip file):

   ```bash
   git clone https://github.com/yourusername/level2pressure.git
   cd level2pressure
   ```

2. Install the package and its dependencies:

   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

   This installs the `level2pressure` package in editable mode, so you can import it in any Python script or Jupyter Notebook.

## Usage

### Importing the Package
After installation, you can import the package in your Python scripts or notebooks:

```python
from level2pressure import cmip6_interp_to_pressure_level, core, utils
```

### Command-Line Interface (CLI)
The package includes a CLI tool for easy usage from the terminal.

```bash
python cmip6_interp_to_pressure_level.py -p 25 -o output.nc -i input.nc
```

**Arguments:**

- `-p, --pressure_interval`: Specifies the pressure interval in hPa (default is 25 hPa).
- `-o, --output`: The output NetCDF file with interpolated data.
- `-i, --input`: The input NetCDF file to be processed.

This command reads the input file, identifies the vertical coordinate type, converts it to pressure levels, interpolates to the specified standard pressure levels, and saves the result to the output file.

### Example Usage in Python

```python
from level2pressure.core import hybrid_height_coordinate_to_pressure, hybrid_sigma_to_pressure
from level2pressure.utils import identify_model_level_type

# Identify model level type in a NetCDF file
model_type, units = identify_model_level_type("input.nc")
print(f"Model Level Type: {model_type} with units: {units}")

# Convert based on type
if model_type == "atmosphere_hybrid_height_coordinate":
    converted_ds = hybrid_height_coordinate_to_pressure("input.nc")
elif model_type == "atmosphere_hybrid_sigma_pressure_coordinate":
    converted_ds = hybrid_sigma_to_pressure("input.nc")

# Save the converted dataset
converted_ds.to_netcdf("output.nc")
```

### Defining Custom Target Pressure Levels
The package includes a function to define standard pressure levels. By default, levels range from 1000 hPa to 0 hPa with a user-specified interval.

```python
from level2pressure.utils import define_targetlevels

# Define target pressure levels with a 25 hPa interval
target_levels = define_targetlevels(25)  # Outputs levels from 1000 hPa to 0 hPa at 25 hPa intervals
```

## Dependencies
- **xarray**: For handling NetCDF data.
- **numpy**: For numerical calculations.
- **netCDF4**: For reading and writing NetCDF files.
- **metpy**: For conversions between height and pressure using the U.S. Standard Atmosphere.

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
This package leverages **MetPy** for U.S. Standard Atmosphere calculations, as well as **xarray** and **numpy** for efficient handling and processing of multidimensional climate model data.