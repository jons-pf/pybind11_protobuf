# Copyright (c) 2021 The Pybind Development Team. All rights reserved.
#
# All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.
"""Tests for basic proto operations on pybind11 type_cast<> protobufs."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import copy
import pickle
import re

from absl.testing import absltest
from absl.testing import parameterized

from pybind11_protobuf.tests import compare
from pybind11_protobuf.tests import vmec_inputs_pb2

from pybind11_protobuf.tests import message_module as m

class MessageTest(parameterized.TestCase, compare.ProtoAssertions):

  @parameterized.named_parameters(
      ('native_proto', vmec_inputs_pb2.TestMessage),
      ('cast_proto', m.make_test_message),
  )
  def test_isinstance(self, factory):
    self.assertIsInstance(factory(), vmec_inputs_pb2.TestMessage)

  @parameterized.named_parameters(
      ('native_proto', vmec_inputs_pb2.TestMessage),
      ('cast_proto', m.make_test_message),
  )
  def test_access_singluar_fields(self, factory):
    message = factory()
    message.string_value = 'test'
    message.int_value = 5
    message.double_value = 5.5
    message.int_message.value = 6
    self.assertEqual(message.string_value, 'test')
    self.assertEqual(message.int_value, 5)
    self.assertEqual(message.double_value, 5.5)
    self.assertEqual(message.int_message.value, 6)

  @parameterized.named_parameters(
      ('native_proto', vmec_inputs_pb2.TestMessage),
      ('cast_proto', m.make_test_message),
  )
  def test_access_repeated_int_value(self, factory):
    message = factory()
    message.repeated_int_value.append(6)
    message.repeated_int_value.append(7)

    self.assertLen(message.repeated_int_value, 2)
    self.assertEqual(message.repeated_int_value[0], 6)
    self.assertEqual(message.repeated_int_value[1], 7)
    for value, expected in zip(message.repeated_int_value, [6, 7]):
      self.assertEqual(value, expected)

    self.assertEqual(str(message.repeated_int_value), '[6, 7]')

    message.repeated_int_value[0] = 8
    self.assertSequenceEqual(message.repeated_int_value, [8, 7])

    message.repeated_int_value.insert(1, 2)
    self.assertSequenceEqual(message.repeated_int_value, [8, 2, 7])

    del message.repeated_int_value[1]
    self.assertSequenceEqual(message.repeated_int_value, [8, 7])

    message.repeated_int_value.extend([6, 5])
    self.assertSequenceEqual(message.repeated_int_value, [8, 7, 6, 5])


if __name__ == '__main__':

  message = vmec_inputs_pb2.TestMessage()

  message.string_value = 'test'
  message.repeated_int_value.append(6)
  message.repeated_int_value.append(7)

  print(message)

  msg2 = m.make_int_message(42)
  print(msg2)


  ans = m.perform_int_operation(msg2)
  print(42*42, ans)




  absltest.main()
