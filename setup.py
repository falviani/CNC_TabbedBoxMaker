import os
from setuptools import setup
# from freecad.workbench_starterkit.version import __version__
# name: this is the name of the distribution.
# Packages using the same name here cannot be installed together

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            "freecad", "TabbedBoxWorkbench", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.workbench_tabbedbox',
      version=str(__version__),
      packages=['freecad',
                'freecad.TabbedBoxWorkbench'],
      maintainer="Frank_Alviani",
      maintainer_email="frank.alviani@gmail.com",
      url="https://github.com/falviani/CNC_TabbedBoxMaker",
      description="a freecad extension to create parameterized tabbed boxes, installable with pip",
      install_requires=['numpy'], # should be satisfied by FreeCAD's system dependencies already
      include_package_data=True)
