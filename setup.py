from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
  this_directory = Path(__file__).absolute().parent
  with open((this_directory / "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()
  requirements = [line.strip() for line in requirements]
except FileNotFoundError:
  requirements = []

# Metadata
setup(
  name = "franzpy",
  version = "0.0.0.9000",
  author = "Franz Welscher",
  author_email = "franz.welscher@plus.ac.at",
  description = "The great-idea-for-a-seminar-session-luuk-package!",
  license = "Apache License 2.0",
  packages = find_packages(),
  install_requires = requirements
)