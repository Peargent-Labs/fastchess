from setuptools import setup, Extension
import numpy as np

setup(
    ext_modules=[
        Extension(
            "fastchess",
            sources=["fastchess.c"],
            include_dirs=[np.get_include()],
            extra_compile_args=["-O3", "-Wall", "-Wextra", "-Wno-unused-parameter"],
        ),
    ],
)
