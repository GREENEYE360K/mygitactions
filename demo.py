#!/usr/bin/env python3
"""
Demonstration script for the print-friendly report views.
This script shows different report scenarios and view formats.
"""

from reports import Report, create_sample_report
from views import view_report, print_friendly_view
from datetime import datetime


def demo_various_reports():
    """Demonstrate various report types and views."""
    
    print("🔍 REPORT VIEW DEMONSTRATION")
    print("=" * 60)
    
    # 1. Sample employee report
    print("\n📊 Sample Employee Report:")
    employee_report = create_sample_report()
    print("\nRegular view:")
    view_report(employee_report)
    
    print("\nPrint-friendly view:")
    print_friendly_view(employee_report)
    
    # 2. Custom financial report
    print("\n" + "=" * 60)
    print("\n💰 Financial Summary Report:")
    financial_data = [
        {"Quarter": "Q1 2024", "Revenue": "$1,250,000", "Expenses": "$800,000", "Profit": "$450,000"},
        {"Quarter": "Q2 2024", "Revenue": "$1,400,000", "Expenses": "$850,000", "Profit": "$550,000"},
        {"Quarter": "Q3 2024", "Revenue": "$1,600,000", "Expenses": "$900,000", "Profit": "$700,000"},
        {"Quarter": "Q4 2024", "Revenue": "$1,800,000", "Expenses": "$950,000", "Profit": "$850,000"}
    ]
    financial_report = Report("Quarterly Financial Summary", financial_data)
    
    print("\nPrint-friendly view:")
    print_friendly_view(financial_report)
    
    # 3. Empty report
    print("\n" + "=" * 60)
    print("\n📋 Empty Report Example:")
    empty_report = Report("Empty Report", [])
    print("\nPrint-friendly view:")
    print_friendly_view(empty_report)
    
    print("\n✅ Demonstration completed!")


if __name__ == "__main__":
    demo_various_reports()