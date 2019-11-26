import xarray as xr


def test_unpack_time_fails():
    fpath = '/badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadCM3_rcp45_r1i1p1_200601-203012.nc'

    with xr.open_dataset(fpath) as ds:
        first_year = ds.variables['time_bnds'][0].data[0].strftime('%Y')



