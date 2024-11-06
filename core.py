# cmip6_conversion/convert.py

import xarray as xr
import numpy as np
from .utils import define_target_levels, height2pressure

def hybrid_height_to_pressure(filename, interval = 25):
    """
    Converts hybrid height coordinates to pressure levels.
    """
    ds = xr.open_dataset(filename)
    b = ds['b'].values.reshape(-1, 1, 1)  # Reference pressure (scalar)
    orog = ds['orog'].values
    sigma = ds['lev'].values.reshape(-1, 1, 1)  # Reshape to (lev, 1, 1)
    height_levels = sigma + b * orog[np.newaxis, :, :]
    pressure_lev = height2pressure(height_levels)
    ds = ds.assign_coords(pressure_lev=("lev", pressure_lev)).swap_dims({"lev": "pressure_lev"}).drop_vars("lev")
    ds = ds.rename({"pressure_lev": "lev"})
    ds_interped = ds.interp(lev=define_target_levels(interval))
    return ds_interped

def hybrid_sigma_to_pressure(filename, interval = 25):
    """
    Converts hybrid sigma-pressure coordinates to pressure levels.
    """
    ds = xr.open_dataset(filename)
    if 'ap' in ds.variables:
        ap = ds['ap'].values.reshape(-1, 1, 1)
        b = ds['b'].values.reshape(-1, 1, 1)
        ps = ds['ps'].values
        pressure_levels = ap + b * ps[:, np.newaxis, :, :]
    else:
        p0 = ds['p0'].values  # Reference pressure (scalar)
        a = ds['a'].values.reshape(-1, 1, 1)
        b = ds['b'].values.reshape(-1, 1, 1)
        ps = ds['ps'].values
        pressure_levels = a * p0 + b * ps[:, np.newaxis, :, :]
    averaged_pressure_lev = np.mean(pressure_levels, axis=(0, 2, 3))
    ds = ds.assign_coords(pressure_lev=("lev", averaged_pressure_lev)).swap_dims({"lev": "pressure_lev"}).drop_vars("lev")
    ds = ds.rename({"pressure_lev": "lev"})
    ds_interped = ds.interp(lev=define_target_levels(interval))
    return ds_interped