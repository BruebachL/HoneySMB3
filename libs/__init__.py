from __future__ import absolute_import
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

LOG = logging.getLogger(__name__)
LOG.addHandler(NullHandler())