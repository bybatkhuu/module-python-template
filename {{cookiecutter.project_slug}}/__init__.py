try:
    from .src.{{cookiecutter.module_name}} import *
except ImportError:
    from src.{{cookiecutter.module_name}} import *
