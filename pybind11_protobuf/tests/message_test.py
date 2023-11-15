# Copyright (c) 2021 The Pybind Development Team. All rights reserved.
#
# All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.
"""Tests for basic proto operations on pybind11 type_cast<> protobufs."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

from pybind11_protobuf.tests import vmec_inputs_pb2
from pybind11_protobuf.tests import message_module as m

if __name__ == '__main__':

  inputs = vmec_inputs_pb2.Inputs()
  inputs.center = 0.6
  inputs.sigma = 0.2
  inputs.intensity = 13.0


  inputs.evaluation_locations[:] = np.linspace(0.0, 1.0, 20)

  outputs = m.evaluate_profile(inputs)

  plt.figure()
  plt.plot(inputs.evaluation_locations, outputs.profile, ".-")
  plt.grid(True)

  plt.show()
