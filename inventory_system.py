"""
Inventory System Module
Performs basic stock operations: add, remove, save, load, and report.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item with a given quantity to the stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.error("Invalid input: item must be str and qty must be int")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(item, qty):
    """Remove a quantity of an item from the stock."""
    try:
        if item not in stock_data:
            raise KeyError(f"Item '{item}' not found in stock")

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed %s from stock (quantity <= 0)", item)
        else:
            logging.info("Removed %d of %s", qty, item)

    except KeyError as e:
        logging.warning("Cannot remove item: %s", e)
    except TypeError as e:
        logging.error("Invalid quantity type: %s", e)


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file and return it."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        logging.info("Data loaded successfully from %s", file)
        return data
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty stock.", file)
        return {}
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON: %s", e)
        return {}


def save_data(file="inventory.json"):
    """Save stock data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Data saved successfully to %s", file)
    except (OSError, TypeError, ValueError) as e:
        logging.error("Error saving data: %s", e)


def print_data():
    """Print all items and quantities in stock."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items with stock below a given threshold."""
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """Demonstrate inventory system operations."""
    stock_data_local = load_data()

    # Use local variable instead of global
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 0)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {stock_data_local.get('apple', 0)}")
    low_items = [item for item, qty in stock_data_local.items() if qty < 5]
    print(f"Low items: {low_items}")

    save_data()
    print_data()

    logging.info("Program executed safely — eval removed.")


if __name__ == "__main__":
    main()
