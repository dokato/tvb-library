# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
# CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#   The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

"""

How to generate your own connectivity. Intended for small architectures.

.. moduleauthor:: Paula Sanz Leon <Paula@tvb.invalid>

"""

# Third party python libraries

from tvb.basic.logger.builder import get_logger
LOG = get_logger(__name__)

#Import from tvb.datatypes modules:
import tvb.datatypes.connectivity as connectivity
import numpy
# from matplotlib.pyplot import *
from tvb.simulator.plot.tools import *

LOG.info("Reading default connectivity...")
#Initialise a Connectivity object
wm = connectivity.Connectivity()

#The following will erase some attributes that we'll generate afterwards.
wm.wipe_out()


# First weights and distances
nor = 4
wm.motif_all_to_all(number_of_regions=nor)

# Centres, specify the number of regions, ptherwise it'll use a default value.
# If we have spherical centres, the orientations will also be created.
wm.centres_spherical(number_of_regions=nor)

# By default, the new regions labels are numeric characters, ie [0, 1, ...]
# It is possible to get alphabetic characters.
wm.create_region_labels(mode='alphabetic')

# Or creting your own

my_labels = numpy.array(['a1', 'b1', 'a2', 'b2'])
wm.region_labels = my_labels

wm.configure()

plot_matrix(wm.weights, connectivity=wm, binary_matrix=True)
import matplotlib.pyplot as plt
plt.show()







