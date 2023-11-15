// Copyright (c) 2021 The Pybind Development Team. All rights reserved.
//
// All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

#include <pybind11/pybind11.h>

#include <functional>
#include <cmath>
#include <memory>
#include <stdexcept>

#include "google/protobuf/message.h"
#include "google/protobuf/text_format.h"
#include "pybind11_protobuf/native_proto_caster.h"

#include "pybind11_protobuf/tests/vmec_inputs.pb.h"

namespace py = ::pybind11;

namespace {

using pybind11::test::Inputs;
using pybind11::test::Outputs;

Outputs evaluate_profile(const Inputs &inputs) {

  const double center = inputs.center();
  const double sigma = inputs.sigma();
  const double intensity = inputs.intensity();

  Outputs out;

  for (const double x: inputs.evaluation_locations()) {
    const double dx = x - center;
    const double value = intensity * std::exp(- dx * dx / (2.0 * sigma * sigma));
    out.add_profile(value);
  }

  return out;
}

PYBIND11_MODULE(message_module, m) {
  pybind11_protobuf::ImportNativeProtoCasters();

  m.def(
      "evaluate_profile",
      evaluate_profile,
      py::arg("inputs") = nullptr);
}

}  // namespace
