def crop_black_borders(x):
    """Crop black borders of 2D image.

    Parameters
    ----------
    x : np.ndarray
        2d array, or 3d array (RGB, RGBA) with trailing channels dimension.
    """
    if x.ndim < 2 or x.ndim > 3:
        raise ValueError("Input must be 2D image.")
    mask = x > 0
    if x.ndim == 3:
        if x.shape[2] not in (3, 4):
            raise ValueError("Input image must have 3 (RGB) or 4 (RGBA) channels.")
        mask = mask[..., :3].all(2)

    m, n = mask.shape
    mask0, mask1 = mask.any(0), mask.any(1)
    col_start, col_end = mask0.argmax(), n - mask0[::-1].argmax()
    row_start, row_end = mask1.argmax(), m - mask1[::-1].argmax()

    return x[row_start:row_end, col_start:col_end]
