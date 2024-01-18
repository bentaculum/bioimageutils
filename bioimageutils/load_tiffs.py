"""
Adapted from https://napari.org/stable/tutorials/processing/dask.html
"""
import os
from tifffile import imread

from skimage.io.collection import alphanumeric_key
from dask import delayed
import dask.array as da
from glob import glob


# TODO more stringent input checks
def load_tiffs(path, ext="tif"):
    filenames = sorted(
        glob(os.path.join(path, f"*.{ext}")),
        key=alphanumeric_key,
    )
    # read the first file to get the shape and dtype
    # ASSUMES THAT ALL FILES SHARE THE SAME SHAPE/TYPE
    sample = imread(filenames[0])

    lazy_imread = delayed(imread)  # lazy reader
    lazy_arrays = [lazy_imread(fn) for fn in filenames]
    dask_arrays = [
        da.from_delayed(delayed_reader, shape=sample.shape, dtype=sample.dtype)
        for delayed_reader in lazy_arrays
    ]
    # Stack into one large dask.array
    stack = da.stack(dask_arrays, axis=0)
    return stack.compute()


if __name__ == "__main__":
    path = "/Users/gallusse/data/celltracking/BF-C2DL-HSC/train/01/"
    load_tiffs(path)
