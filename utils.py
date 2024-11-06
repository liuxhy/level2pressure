# cmip6_conversion/utils.py

import xarray as xr
import numpy as np

def identify_model_level_type(nc_file):
    """
    Identifies the model level type by checking vertical coordinate variables.
    """
    ds = xr.open_dataset(nc_file)
    if 'lev' in ds.variables:
        return ds.lev.standard_name, ds.lev.units
    elif 'presnivs' in ds.variables:
        return ds.presnivs.standard_name, ds.presnivs.units
    elif 'plev' in ds.variables:
        return ds.plev.standard_name, ds.plev.units
    return None, None


def define_target_levels(interval):
    """
    Defines a list of pressure levels from 1000 hPa to 0 with the specified interval.
    """
    return np.arange(1000e2, 0, -interval * 100)

def height2pressure(hgt):
    """
    Converts height levels to pressure level according to the U.S. Standard Atmosphere using
    the implementation of MetPy.
    
    Inputs:
       hgt: array of height levels in m
    Output:
       pres: array of pressure levels in Pa
    """    
    from metpy.calc import height_to_pressure_std
    from metpy.units import units
    return 100*height_to_pressure_std(hgt*units("m")).magnitude # pressure in Pa
