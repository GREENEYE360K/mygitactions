"""
View functions for displaying reports in different formats.
"""
from reports import Report


def view():
    print("view")


def hide():
    print("hide")


def view_report(report: Report) -> None:
    """Display a report in regular format with basic styling."""
    print(f"\n=== {report.title} ===")
    print(f"Generated: {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    if not report.data:
        print("No data available.")
        return
    
    # Get column names
    columns = report.get_columns()
    
    # Print header
    header = " | ".join(f"{col:>15}" for col in columns)
    print(header)
    print("-" * len(header))
    
    # Print data rows
    for row in report.data:
        row_str = " | ".join(f"{str(row.get(col, '')):>15}" for col in columns)
        print(row_str)
    
    print(f"\nTotal records: {len(report.data)}")


def print_friendly_view(report: Report) -> None:
    """
    Display a report in print-friendly format.
    
    Print-friendly features:
    - Clean, monospace-friendly formatting
    - No special characters that might not print well
    - Proper spacing for physical printing
    - Clear section breaks
    - Page-friendly layout
    """
    print("\n" + "=" * 80)
    print(f"REPORT: {report.title}")
    print(f"Generated: {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    if not report.data:
        print("\nNo data available in this report.")
        print("\n" + "=" * 80)
        return
    
    # Get column names and calculate optimal widths
    columns = report.get_columns()
    col_widths = {}
    
    # Calculate column widths based on content
    for col in columns:
        max_width = len(col)
        for row in report.data:
            content_width = len(str(row.get(col, '')))
            max_width = max(max_width, content_width)
        # Add some padding and limit maximum width
        col_widths[col] = min(max_width + 2, 25)
    
    # Print table header
    print("\n")
    header_parts = []
    separator_parts = []
    
    for col in columns:
        width = col_widths[col]
        header_parts.append(f"{col:<{width}}")
        separator_parts.append("-" * width)
    
    print(" ".join(header_parts))
    print(" ".join(separator_parts))
    
    # Print data rows
    for i, row in enumerate(report.data, 1):
        row_parts = []
        for col in columns:
            width = col_widths[col]
            content = str(row.get(col, ''))
            # Truncate if too long
            if len(content) > width - 1:
                content = content[:width-4] + "..."
            row_parts.append(f"{content:<{width}}")
        
        print(" ".join(row_parts))
        
        # Add page break hint every 20 rows for printing
        if i % 20 == 0 and i < len(report.data):
            print("\n" + "-" * 60 + " (Page Break) " + "-" * 60)
    
    # Print summary
    print("\n" + "-" * 80)
    print(f"SUMMARY: Total records in report: {len(report.data)}")
    print(f"Report generation completed at: {report.generated_at.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    print(view())