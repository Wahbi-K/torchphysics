"""Useful helper methods for the definition and evaluation of a problem.

For the creation of conditions, some differential operators are implemented under
torchphysics.utils.differentialoperators.

For the evaluation of the trained model, some plot and animation functionalities are provided.
They can give you a rough overview of the determined solution. These lay under
torchphysics.utils.plotting
"""
from .differentialoperators import (laplacian,
                                    grad,
                                    div,
                                    jac,
                                    partial,
                                    convective,
                                    rot, 
                                    normal_derivative)

from .data import PointsDataset, PointsDataLoader

from .user_fun import UserFunction
from .plotting import plot, Plotter, animate, scatter
from .evaluation import compute_min_and_max