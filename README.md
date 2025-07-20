# mygitactions

A Python application demonstrating print-friendly report views.

## Features

### Report Views
This application provides two types of report views:

1. **Regular View** (`view_report()`) - Standard console display with basic formatting
2. **Print-Friendly View** (`print_friendly_view()`) - Optimized for physical printing

### Print-Friendly Features
The print-friendly view includes:
- Clean monospace formatting suitable for any printer
- Proper spacing and alignment
- Clear headers and section separators
- Page break hints for long reports (every 20 rows)
- Content truncation to prevent line wrapping
- Summary information with record counts and generation timestamps

## Usage

### Basic Usage
```python
from reports import create_sample_report
from views import view_report, print_friendly_view

# Create a report
report = create_sample_report()

# Display in regular format
view_report(report)

# Display in print-friendly format
print_friendly_view(report)
```

### Custom Reports
```python
from reports import Report
from views import print_friendly_view

# Create custom report data
data = [
    {"Product": "Widget A", "Sales": 1500, "Revenue": "$45,000"},
    {"Product": "Widget B", "Sales": 2300, "Revenue": "$69,000"}
]

report = Report("Sales Report", data)
print_friendly_view(report)
```

## Running the Demo

```bash
# Run the main demonstration
python3 main.py

# Run extended demonstration with multiple report types
python3 demo.py

# Test individual components
python3 views.py
python3 -c "from reports import create_sample_report; print('Report created successfully')"
```

## Files

- `reports.py` - Report data structures and sample data generation
- `views.py` - Report display functions (regular and print-friendly)
- `main.py` - Main demonstration script
- `demo.py` - Extended demonstration with multiple report types