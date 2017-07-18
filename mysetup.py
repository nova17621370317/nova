
from distutils.core import setup
import py2exe

setup(windows = [{"script" : "get_weekno.py", "icon_resources" : [(1, "1.ico")]}])
#setup(console=["get_weekno.py"])
#setup(windows=["get_weekno.py"])