"""This allows you to mock out the entire arcpy package so that you can test packages that use arcpy in github's CI
environment. You just need to 'import mock_arcpy' prior to importing arcpy directly or importing any other packages/
modules that import arcpy in turn.
"""

import sys
from unittest.mock import Mock

module_name = 'arcpy'
arcpy = Mock(name=module_name)
sys.modules[module_name] = arcpy
