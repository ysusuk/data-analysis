from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

default_task = "publish"

@init
def initialize(project):
    project.build_depends_on('mockito')
    project.build_depends_on('pandas')
    project.build_depends_on('numpy')
    project.build_depends_on('matplotlib')
    # project.build_depends_on('json')
    # project.set_property('coverage_threshold_warn', 50)
    project.set_property('coverage_break_build', False)
