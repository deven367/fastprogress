__version__ = "1.0.3"


__all__ = ["master_bar", "progress_bar", "force_console_behavior"]

from .fastprogress import force_console_behavior, master_bar, progress_bar
