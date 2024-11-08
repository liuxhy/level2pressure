# level2pressure

`level2pressure` is a Python package designed to convert vertical coordinates in CMIP6 climate model data to pressure levels. This is particularly useful for models that use hybrid sigma or hybrid height coordinates, allowing users to interpolate their data to standard pressure levels for easier comparison and analysis.

## Why Convert to Pressure Levels?

Climate and weather models often use hybrid coordinate systems, such as hybrid height and hybrid sigma-pressure coordinates, to capture atmospheric processes near the surface and in the free atmosphere. However, pressure levels are the standard for atmospheric analysis, as they simplify comparisons with observational data, standardize analyses across models, and make data interpretation more straightforward.

Converting model data to pressure levels allows for:
- **Consistency with Observational Data**: Many atmospheric observations (e.g., radiosondes, satellite data) are reported on pressure levels. Conversion facilitates direct comparisons.
- **Cross-Model Comparisons**: Standardizing data on pressure levels makes it easier to compare outputs from different models.
- **Simplified Analysis**: Pressure levels align with meteorological concepts, like the tropopause or jet stream, making data interpretation more intuitive.

## Coordinate Systems

### Hybrid Height Coordinate

The **hybrid height coordinate** system combines terrain-following coordinates near the surface with fixed-height levels in the upper atmosphere. This allows models to accurately represent boundary-layer processes by following the terrain, while transitioning to fixed height levels higher up for stability.

### Hybrid Sigma-Pressure Coordinate

The **hybrid sigma-pressure coordinate** system uses terrain-following sigma coordinates near the surface and pressure-based coordinates in the free atmosphere. This approach captures surface-level processes accurately by following terrain, while using pressure levels aloft to better align with observational data.

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
```
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

## Acknowledgments
This package leverages **MetPy** for U.S. Standard Atmosphere calculations, as well as **xarray** and **numpy** for efficient handling and processing of multidimensional climate model data.

## Author

This package was created by [Xinhuiyu Liu, University of Virginia](https://github.com/liuxhy).

Feel free to reach out with questions, suggestions, or contributions via GitHub or email.