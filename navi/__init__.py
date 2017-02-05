import os, sys, inspect

# Add matrix-sdk submodule to path
__this_dir = os.path.split(inspect.getfile(inspect.currentframe()))[0]
__this_dir = os.path.realpath(os.path.abspath(__this_dir))
__matrix_dir = os.path.join(__this_dir, "matrix-python-sdk")
if __matrix_dir not in sys.path:
    sys.path.insert(0, __matrix_dir)
