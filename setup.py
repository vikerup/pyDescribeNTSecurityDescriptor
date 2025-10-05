from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = [
        line.strip() for line in f
        if line.strip() and not line.strip().startswith('#')
    ]

# Detect Python scripts in the same directory as this setup.py (excluding itself)
base_dir = os.path.abspath(os.path.dirname(__file__))
setup_py = os.path.basename(__file__)
binaries = [
    fname for fname in os.listdir(base_dir)
    if fname.endswith('.py')
       and os.path.isfile(os.path.join(base_dir, fname))
       and fname != setup_py
]

setup(
    name="pyDescribeNTSecurityDescriptor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    scripts=binaries,
)
