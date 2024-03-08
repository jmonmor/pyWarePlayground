import importlib.util
import os

def run_pyc_file(pyc_file_path):
    # Create a spec using the path to the .pyc file
    spec = importlib.util.spec_from_file_location("module_name", pyc_file_path)
    # Create a module based on the spec
    module = importlib.util.module_from_spec(spec)
    # Load the code from the .pyc file into the module
    spec.loader.exec_module(module)

def run():
    pyc_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './__pycache__/processor.cpython-311.pyc')
    print(pyc_file_path)
    run_pyc_file(pyc_file_path)
    
run()
