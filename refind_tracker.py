import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_record(self, amount, category, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        record = {"amount": amount, "category": category, "date": date}
        self.data.append(record)
        self.save_data()

    def view_records(self):
        for record in self.data:
            print(f"Date: {record['date']}, Category: {record['category']}, Amount: {record['amount']}")

    def filter_by_category(self, category):
        return [record for record in self.data if record["category"] == category]

# 測試程式碼
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_record(100, "Food")
    tracker.view_records()