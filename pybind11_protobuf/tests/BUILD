# Tests and examples for the pybind11_protobuf package.

load("@com_github_grpc_grpc//bazel:python_rules.bzl", "py_proto_library")

# Placeholder: load py_proto_library
# Placeholder: load py_library
load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")
# [internal] load cc_proto_library.bzl

licenses(["notice"])

py_library(
    name = "compare",
    srcs = ["compare.py"],
    srcs_version = "PY3",
    visibility = ["//visibility:public"],
    deps = ["@com_google_protobuf//:protobuf_python"],
)

proto_library(
    name = "test_proto",
    srcs = ["test.proto"],
)

cc_proto_library(
    name = "test_cc_proto",
    deps = [":test_proto"],
)

py_proto_library(
    name = "test_py_pb2",
    deps = [":test_proto"],
)

# Tests for native_proto_caster


pybind_extension(
    name = "message_module",
    srcs = ["message_module.cc"],
    deps = [
        ":test_cc_proto",
        "//pybind11_protobuf:native_proto_caster",
        "@com_google_protobuf//:protobuf",
    ],
)

py_test(
    name = "message_test",
    srcs = ["message_test.py"],
    data = [
        ":message_module.so",
    ],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":compare",
        ":test_py_pb2",
        "@com_google_absl_py//absl/testing:absltest",
        "@com_google_absl_py//absl/testing:parameterized",
        "@com_google_protobuf//:protobuf_python",
    ],
)
