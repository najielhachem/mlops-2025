# scripts/preprocess.py
import argparse
import pandas as pd

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Preprocess raw CSV data")
    p.add_argument("--input", required=True, help="Path to raw CSV file")
    p.add_argument("--output", required=True, help="Path to save cleaned CSV")
    return p

def main():
    args = build_parser().parse_args()
    
    # Step 1: read the raw CSV
    df = pd.read_csv(args.input)
    
    # Step 2: minimal cleaning
    # Example: drop obvious unwanted columns
    df = df.drop(columns=["unnecessary_column"], errors="ignore")
    # Example: fill missing values
    df = df.fillna(0)
    
    # Step 3: write cleaned dataframe
    df.to_csv(args.output, index=False)
    print(f"Cleaned data saved to {args.output}")

if __name__ == "__main__":
    main()
