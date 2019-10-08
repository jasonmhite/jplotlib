from setuptools import setup

setup(
    name="jplotlib",
    version="0.0.1",
    author="Jason M. Hite",
    license="BSD",
    packages=["jplotlib"],
    install_requires=["matplotlib", "seaborn", "numpy"],
    extra_requires={
        "incremental_stats": ["numba"],
    },
)
