"""Cellgrid method for coordinate analysis


"""
from __future__ import division, print_function

import numpy as np

def _address_to_id(addr, ncells):
    """Return the cell index from a cell address

    address is (z, y, x)
    """
    return addr[2] + addr[1] * ncells[0] + addr[0] * ncells[1] * ncells[2]

def _id_to_address(cid, ncells):
    """Return the cell adress from a cell index

    address is (z, y, x)
    """
    z = cid // (ncells[0] * ncells[1])
    cid %= ncells[0] * ncells[1]
    y = cid // ncells[0]
    cid %= ncells[0]

    return z, y, cid

class CellGrid(object):
    def __init__(self, box, max_dist, coordinates=None):
        """
        :Arguments:
        coordinates (n,3) array of positions
        box (3) size of box in each direction
        cellsize
        """
        self._box = box
        # Maximum desired distance
        self._max_dist = max_dist
        # determine number of cells
        self._determine_cells()

        self._coordinates = coordinates

    def _determine_cells(self):
        # number of cells in each direction
        self._ncells = np.floor_divide(self._box, self._max_dist).astype(np.int)
        self._total_cells = np.product(self._ncells)
        # size of cell in each direction
        self._cell_size = self._box / self._ncells

    def _put_into_cells(self):
        self._cell_locations = np.floor_divide(self._coordinates, self._cell_size)

    def __iter__(self):
        return iter(self.cells)


class Cell(object):
    def __init__(self):
        pass