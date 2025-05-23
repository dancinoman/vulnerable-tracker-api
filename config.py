import os

# Paths of projects.
CURENT_PATH = project_root = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURENT_PATH)
TEST_DATA_PATH = file_path = os.path.join(PROJECT_ROOT,"tests", "data")

# Global variables.
VERSION = "1.2.1"
APP_NAME = "Vulnerable Tracker API"
