from . import backend_py

backend = backend_py

## try C++ backend
try:
  ## hide python backend by overwriting the variable
  from . import backend_cpp as backend
  ## import python backend with original name, in case still required
  from . import backend_py

## if fails, only load python backend
except (ModuleNotFoundError, ImportError) as e:
  import logging
  _logger = logging.getLogger(__name__)
  _logger.warning(f"C++ backend could not be imported, falling back to python!\nReason:\n\n{e}\n\n")

__all__ = ["backend", "backend_py"]
