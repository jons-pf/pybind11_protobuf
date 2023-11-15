// Copyright (c) 2021 The Pybind Development Team. All rights reserved.
//
// All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

#include <pybind11/pybind11.h>

#include <functional>
#include <memory>
#include <stdexcept>

#include "google/protobuf/message.h"
#include "google/protobuf/text_format.h"
#include "pybind11_protobuf/native_proto_caster.h"

#include "pybind11_protobuf/tests/vmec_inputs.pb.h"

namespace py = ::pybind11;

namespace {

using pybind11::test::IntMessage;
using pybind11::test::TestMessage;

PYBIND11_MODULE(message_module, m) {
  pybind11_protobuf::ImportNativeProtoCasters();

  m.def(
      "make_test_message",
      [](std::string text) -> TestMessage {
        TestMessage msg;
        if (!text.empty() && !::google::protobuf::TextFormat::ParseFromString(text, &msg)) {
          throw py::value_error("Failed to parse text format TestMessage");
        }
        return msg;
      },
      py::arg("text") = "");

  m.def(
      "make_int_message",
      [](int value) -> IntMessage {
        IntMessage msg;
        msg.set_value(value);
        return msg;
      },
      py::arg("value") = 123);

  m.def(
      "make_nested_message",
      [](int value) -> TestMessage::Nested {
        TestMessage::Nested msg;
        msg.set_value(value);
        return msg;
      },
      py::arg("value") = 123);
}

}  // namespace
