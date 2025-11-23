#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsAggregator.settings')
    try:
        from django.core.management import execute_from_command_line
    except Exception as exc:
        sys.stderr.write(
            "Couldn't import Django. Make sure Django is installed in your "
            "current Python environment (e.g. pip install django) and that "
            "you activated the virtual environment if using one.\n"
            f"Import error: {exc}\n"
        )
        sys.exit(1)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
