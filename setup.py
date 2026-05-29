from setuptools import setup, Extension
import numpy as np
import sys

if sys.platform == "win32":
    compile_args = ["/O2", "/W3"]
else:
    compile_args = ["-O3", "-Wall", "-Wextra", "-Wno-unused-parameter"]

setup(
    ext_modules=[
        Extension(
            "fastchess",
            sources=["fastchess.c"],
            include_dirs=[np.get_include()],
            extra_compile_args=compile_args,
        ),
    ],
)
