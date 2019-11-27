import xarray as xr
import glob
import time
import sys

base_path = '/badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas'
files = glob.glob(base_path + '/*.nc')


REQ_YEARS = set([int(_) for _ in range(2010, 2020)])


def test_files(fpaths):
    start_time = time.time()
    print(f'[INFO] Testing {len(files)} files...')

    files_in_range = []

    for fpath in fpaths:
        ds = xr.open_dataset(fpath)
        years = set([int(_) for _ in ds.time.dt.year])

        if REQ_YEARS.issubset(years):
            files_in_range.append(fpath) 
        
    try:
        xr.open_mfdataset(files_in_range)
        valid = files_in_range
        print(f'[INFO] Ready to load: {files_in_range}')
    except Exception as err:
        print(f'[ERROR] Could not load files: {files_in_range}')
        valid = []

    print(f'took {time.time() - start_time} seconds')


if __name__=='__main__':

    args = sys.argv[1:]
    if len(args) > 0:
        files = args
 
    test_files(fpaths=files)

