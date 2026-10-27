
from pathlib import Path

import pandas as pd


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Location of the original dataset files
DATA_DIR = PROJECT_ROOT / "data" / "raw"


def inspect_dataset():
    """Check the dataset files and inspect their structure."""

    required_files = [
        "sales_train_validation.csv",
        "calendar.csv",
        "sell_prices.csv",
    ]

    print("=" * 60)
    print("SALES FORECASTING - DATA INSPECTION")
    print("=" * 60)

    # Step 1: Verify that all required files exist
    missing_files = []

    for filename in required_files:
        file_path = DATA_DIR / filename

        if file_path.exists():
            size_mb = file_path.stat().st_size / (1024 ** 2)

            print(f"\nFOUND: {filename}")
            print(f"Size: {size_mb:.2f} MB")
        else:
            print(f"\nMISSING: {filename}")
            missing_files.append(filename)

    if missing_files:
        print("\nPlease add the missing files to:")
        print(DATA_DIR)
        return

    # Step 2: Inspect sales data without loading the full file
    sales_path = DATA_DIR / required_files[0]

    sales_sample = pd.read_csv(
        sales_path,
        nrows=5
    )

    print("\n" + "=" * 60)
    print("SALES DATA")
    print("=" * 60)

    print("Sample shape:", sales_sample.shape)
    print("Columns:", sales_sample.columns.tolist())
    print("\nFirst five records:")
    print(sales_sample.head().to_string(index=False))

    # Step 3: Inspect the calendar
    calendar_path = DATA_DIR / required_files[1]

    calendar = pd.read_csv(calendar_path)

    print("\n" + "=" * 60)
    print("CALENDAR DATA")
    print("=" * 60)

    print("Shape:", calendar.shape)
    print("Columns:", calendar.columns.tolist())

    if "date" in calendar.columns:
        calendar["date"] = pd.to_datetime(calendar["date"])

        print("First date:", calendar["date"].min().date())
        print("Last date:", calendar["date"].max().date())

    # Step 4: Inspect a sample of selling prices
    prices_path = DATA_DIR / required_files[2]

    prices_sample = pd.read_csv(
        prices_path,
        nrows=5
    )

    print("\n" + "=" * 60)
    print("SELLING PRICE DATA")
    print("=" * 60)

    print("Sample shape:", prices_sample.shape)
    print("Columns:", prices_sample.columns.tolist())
    print("\nFirst five records:")
    print(prices_sample.head().to_string(index=False))

    print("\n" + "=" * 60)
    print("INITIAL DATA INSPECTION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    inspect_dataset()
