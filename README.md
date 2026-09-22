## Snack Truck Sales Tracker

A beginner-friendly data analysis project demonstrating how to use **Python** and **pandas** to group and summarize raw sales receipts using the Split-Apply-Combine method.

---

## Project Overview

Imagine running a busy food truck. Every time a customer orders an item, a receipt is logged with the item name, category, time of day, price, and quantity.

This project shows how to turn raw receipts into actionable insights using pandas grouping and aggregation:
- Calculate total revenue per food category.
- Track sales volumes by time of day (Morning vs. Afternoon).
- Build a multi-metric scoreboard showing revenue, average order size, and purchase frequency.

---

## Key Concepts Covered

- **Feature Engineering:** Creating calculated columns (`price * quantity`).
- **Single-Column Grouping:** `df.groupby('category')['total_sale'].sum()`
- **Multi-Column Grouping:** `df.groupby(['time_of_day', 'category'])['quantity'].sum()`
- **Named Aggregation (`.agg`):** Calculating multiple summary statistics (`sum`, `mean`, `count`) in a single step.

---

## Requirements

- Python 3.8+
- pandas

Install pandas via pip:

```bash
pip install pandas
