// error.cpp, the c++-class
#include "error.hpp"

void Error::error() { throw std::runtime_error("This is an error"); }