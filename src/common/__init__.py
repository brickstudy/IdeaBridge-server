import os
import sys


common_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
src_path = os.path.abspath(os.path.join(common_path, os.path.pardir))

sys.path.append(common_path)
sys.path.append(src_path)
