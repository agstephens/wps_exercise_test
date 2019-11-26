import xarray as xr
import numpy as np


def test_unpack_time_fails():
    fpath = '/badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadCM3_rcp45_r1i1p1_200601-203012.nc'

    with xr.open_dataset(fpath) as ds:

        t0d0 = ds.variables['time_bnds'][0].data[0]
        assert('strftime' not in dir(t0d0))
#        first_year = ds.variables['time_bnds'][0].data[0].strftime('%Y')


def test_unpack_time_success():
    fpath = '/badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadCM3_rcp45_r1i1p1_200601-203012.nc'

    with xr.open_dataset(fpath) as ds:
        assert('time_bnds' in ds.variables)

        time_bnds = ds.variables['time_bnds']
        assert(len(time_bnds > 0))

        t0 = time_bnds[0]
        print(t0)
        t0d = t0.data
        print(t0d)
        assert(len(t0d) == 2)

        t0d0 = t0d[0]
        assert(type(t0d0) == np.float64)
       
#        first_year = ds.variables['time_bnds'][0].data[0].strftime('%Y')

        # This URL gave me some hints on using time in xarray: http://xarray.pydata.org/en/stable/time-series.html
        # - if it exists in the dataset then you can use: ds.time.dt

        # So you only need one line:
        first_year = int(ds.time.dt.year[0]) 
        assert(first_year == 2006)


test_unpack_time_fails()
test_unpack_time_success()

