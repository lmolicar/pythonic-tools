"""

"""
import xarray as xr
import pandas as pd

def extract_values_xr_dataarray(da, points):
    
    result_df = pd.DataFrame()
    
    # Dimensions in the source NetCDF may have different names.
    dim_lat = da.indexes["latitude"].name
    dim_lon = da.indexes["longitude"].name
    
    xcoords = []
    ycoords = []
    for each in points:
        xcoords.append(each[0])
        ycoords.append(each[1])
    
    tgt_x = xr.DataArray(xcoords, dims="points")
    tgt_y = xr.DataArray(ycoords, dims="points")
    res = da.sel({dim_lat : tgt_y, dim_lon : tgt_x}, method = "nearest")
    
    # Convert to a Pandas DataFrame for easy export to other formats.
    labels = [f"Point{nn+1}" for nn in range(len(points))]
    res_df = pd.DataFrame(res.values, columns = labels)
    
    return res_df