# level2pressure/cmip6_interp_to_pressure_level.py

import argparse
import xarray as xr
import numpy as np
from level2pressure import (
    identify_model_level_type,
    define_target_levels,
    hybrid_height_to_pressure,
    hybrid_sigma_to_pressure
)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Convert CMIP6 model vertical coordinates to pressure levels."
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Input NetCDF file."
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Output NetCDF file with interpolated data."
    )
    parser.add_argument(
        "-p", "--pressure_interval", type=int, default=25,
        help="Pressure interval in hPa (default: 25hPa)."
    )

    args = parser.parse_args()

    # Identify the model level type
    model_type, _ = identify_model_level_type(args.input)
    
    # Define target pressure levels based on interval
    target_levels = define_target_levels(args.pressure_interval)

    # Open the input dataset and convert to pressure levels
    if model_type == "atmosphere_hybrid_height_coordinate":
        ds_converted = hybrid_height_to_pressure(args.input)
    elif model_type == "atmosphere_hybrid_sigma_pressure_coordinate":
        ds_converted = hybrid_sigma_to_pressure(args.input)
    else:
        raise ValueError(f"Unsupported model level type: {model_type}")

    # Interpolate to target pressure levels
    ds_interpolated = ds_converted.interp(lev=target_levels)

    # Save the interpolated dataset to the output file
    ds_interpolated.to_netcdf(args.output)
    print(f"Converted and interpolated dataset saved to {args.output}")

if __name__ == "__main__":
    main()
