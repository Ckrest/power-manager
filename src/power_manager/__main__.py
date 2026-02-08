"""Allow running as python -m power_manager."""
import sys
from .cli import main

sys.exit(main())
