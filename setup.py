from setuptools import find_packages, setup
from retail import __version__

setup(
    name="retail",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks Labs CICD Templates Sample Project",
    author="jasser.abidi@databricks.com",
)
