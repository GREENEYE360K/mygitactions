"""
Basic report data structures and functionality.
"""
from datetime import datetime
from typing import List, Dict, Any


class Report:
    """Represents a basic report with title, data, and metadata."""
    
    def __init__(self, title: str, data: List[Dict[str, Any]], 
                 generated_at: datetime = None):
        self.title = title
        self.data = data
        self.generated_at = generated_at or datetime.now()
    
    def add_row(self, row: Dict[str, Any]) -> None:
        """Add a row of data to the report."""
        self.data.append(row)
    
    def get_columns(self) -> List[str]:
        """Get column names from the data."""
        if not self.data:
            return []
        return list(self.data[0].keys())


def create_sample_report() -> Report:
    """Create a sample report for demonstration purposes."""
    sample_data = [
        {"Name": "Alice Johnson", "Department": "Engineering", "Salary": 75000, "Start Date": "2022-01-15"},
        {"Name": "Bob Smith", "Department": "Marketing", "Salary": 62000, "Start Date": "2021-08-20"},
        {"Name": "Carol Davis", "Department": "Engineering", "Salary": 82000, "Start Date": "2020-03-10"},
        {"Name": "David Wilson", "Department": "Sales", "Salary": 58000, "Start Date": "2023-02-01"},
        {"Name": "Eva Brown", "Department": "HR", "Salary": 65000, "Start Date": "2021-11-30"}
    ]
    
    return Report("Employee Report", sample_data)