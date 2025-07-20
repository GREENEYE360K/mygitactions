"""
Main application demonstrating regular and print-friendly report views.
"""
from reports import create_sample_report
from views import view_report, print_friendly_view


def hello():
    print("hi")


def bye():
    print("bye")


def main():
    """Demonstrate regular and print-friendly report views."""
    print("Demo: Regular and Print-Friendly Report Views")
    print("=" * 50)
    
    # Create a sample report
    report = create_sample_report()
    
    print("\n1. Regular View:")
    view_report(report)
    
    print("\n\n2. Print-Friendly View:")
    print_friendly_view(report)


if __name__ == "__main__":
    main()
