import logging
import numpy as np
from scipy.ndimage import distance_transform_edt
from skimage.util import map_array
from skimage.segmentation import watershed


logger = logging.getLogger(__name__)


def expand_labels(labels: np.ndarray, distances: dict) -> np.ndarray:
    """Expand labels by an individual distance for each label.

    Parameters
    ----------
    labels : np.ndarray
        nd array of positive integer labels that fit into uint32. 0 is background.
    distances : dict
        Dictionary of label -> distance (amount of dilation) pairs.
    """
    if 0 in distances:
        raise ValueError("Expanding background (label 0) is not allowed.")
    if labels.max() >= 2**32:
        raise ValueError("Labels must fit into uint32.")
    # TODO check label: distance pairs

    dense_distances = map_array(
        labels.astype(np.uint32),
        input_vals=np.array(list(distances.keys()), dtype=np.uint32),
        output_vals=np.array(list(distances.values()), dtype=np.uint32),
    )
    d, idx = distance_transform_edt(~labels.astype(bool), return_indices=True)
    v = dense_distances[tuple(idx)]
    # If the distance is smaller equal than the radius to expand, then do expand
    mask = d <= v

    expanded_labels = watershed(image=d, markers=labels, mask=mask)

    return expanded_labels
