import os
import sys
import shutil
import platform

from subprocess import check_call, CalledProcessError

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ["-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + extdir,
                      "-DCMAKE_PREFIX_PATH=" + os.popen("python -m pybind11 --cmakedir").read().strip()]

        cfg = "Release"
        build_args = ["--config", "Release"]

        if platform.system() == "Windows":
            cmake_args += ["-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}".format(cfg.upper(), extdir)]
            cmake_args += ["-A", "x64" if sys.maxsize > 2**32 else "Win32"]
            build_args += ["--", "/v:m", "/m"]
        else:
            cmake_args += ["-DCMAKE_BUILD_TYPE=" + cfg]

        def build():
            os.makedirs(self.build_temp, exist_ok=True)
            check_call(["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp)
            check_call(["cmake", "--build", "."] + build_args, cwd=self.build_temp)

        try:
            build()
        except CalledProcessError:  # possible CMake error if the build cache has been copied
            shutil.rmtree(self.build_temp)  # delete build cache and try again
            build()

setup(
    packages=find_packages(),
    include_package_data=True,
    ext_modules=[CMakeExtension('_pyerror')],
    cmdclass=dict(build_ext=CMakeBuild)
)
