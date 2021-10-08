from setuptools import setup,find_packages

setup(
    name='Count4Game',
    extras_require=find_packages(where='src'),
    package_dir={"":"src"}
)