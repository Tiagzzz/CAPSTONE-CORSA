#!/usr/bin/env python3
"""
Master entry point for CORSA Jakarta analytical pipeline.
Runs:
  1. analysis/inventory.py
  2. analysis/extract_model.py
  3. analysis/compute_stats.py
  4. analysis/check_links.py
  5. analysis/verify_report.py

Usage:
  python3 analysis/run_all.py [--model-path PATH] [--skip-links]
"""

import argparse
import sys
from pathlib import Path

ANALYSIS_DIR = Path(__file__).resolve().parent
ROOT = ANALYSIS_DIR.parent
if str(ANALYSIS_DIR) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_DIR))

import inventory
import extract_model
import compute_stats
import check_links
import verify_report


def main():
    parser = argparse.ArgumentParser(description="Run all CORSA Jakarta analysis & verification scripts")
    parser.add_argument(
        "--model-path",
        type=Path,
        default=extract_model.DEFAULT_MODEL,
        help="Path to the financial model .xlsx file (default: v0.6)",
    )
    parser.add_argument(
        "--skip-links",
        action="store_true",
        help="Skip live HTTP network reachability checks in check_links.py",
    )
    args = parser.parse_args()

    print("=== [1/5] Running inventory.py ===")
    inventory.main()

    print("\n=== [2/5] Running extract_model.py ===")
    extract_model.extract_model(args.model_path)

    print("\n=== [3/5] Running compute_stats.py ===")
    compute_stats.main()

    print("\n=== [4/5] Running check_links.py ===")
    check_links.check_links(skip_network=args.skip_links)

    print("\n=== [5/5] Running verify_report.py ===")
    verify_report.parse_report_and_generate_artifacts()

    print("\n=== All pipeline steps completed successfully. Outputs saved in analysis/outputs/ ===")


if __name__ == "__main__":
    main()
