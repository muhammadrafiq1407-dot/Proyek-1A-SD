import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.inventory.cli.app import InventoryCLIApp

def main():
    app = InventoryCLIApp()
    app.run()

if __name__ == "__main__":
    main()
