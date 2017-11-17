import site
import os

script_directory = os.path.dirname((os.path.dirname(__file__)))
site.addsitedir(script_directory)
