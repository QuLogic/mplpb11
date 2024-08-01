// main.cpp, linking with python
#include "error.hpp"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_pyerror, m) {
    py::class_<Error>(m, "Error")
        .def(py::init<>())
        .def("error", &Error::error);
}