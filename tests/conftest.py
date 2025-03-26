# conftest.py
import os
import sys

def pytest_sessionstart(session):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    src_dir = os.path.join(parent_dir, 'src')
    # set the source directory in the path
    sys.path = [*sys.path, parent_dir, src_dir]