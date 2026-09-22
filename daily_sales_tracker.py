import pandas as pd


data = {
    "item": [
        "Choco Cone",
        "Fruit Pop",
        "Choco Cone",
        "Cookie",
        "Fruit Pop",
        "Choco Cone",
        "Cookie",
    ],
    "category": [
        "Ice Cream",
        "Popsicle",
        "Ice Cream",
        "Bakery",
        "Popsicle",
        "Ice Cream",
        "Bakery",
    ],
    "time_of_day": [
        "Morning",
        "Morning",
        "Afternoon",
        "Morning",
        "Afternoon",
        "Afternoon",
        "Afternoon",
    ],
    "price": [3.50, 2.00, 3.50, 1.50, 2.00, 3.50, 1.50],
    "quantity": [2, 3, 1, 4, 2, 5, 2],
}

df = pd.DataFrame(data)


df["total_sale"] = df["price"] * df["quantity"]

print("=" * 45)
print("1. RAW SALES RECEIPTS")
print("=" * 45)
print(df)



category_totals = (
    df.groupby("category")["total_sale"]
    .sum()
    .reset_index()
    .rename(columns={"total_sale": "revenue"})
)

print("\n" + "=" * 45)
print("2. TOTAL REVENUE BY CATEGORY")
print("=" * 45)
print(category_totals)



time_breakdown = (
    df.groupby(["time_of_day", "category"])["quantity"]
    .sum()
    .reset_index()
    .rename(columns={"quantity": "total_items_sold"})
)

print("\n" + "=" * 45)
print("3. ITEMS SOLD BY TIME & CATEGORY")
print("=" * 45)
print(time_breakdown)



item_summary = (
    df.groupby("item")
    .agg(
        total_revenue=("total_sale", "sum"),
        avg_units_per_order=("quantity", "mean"),
        order_count=("quantity", "count"),
    )
    .reset_index()
)

print("\n" + "=" * 45)
print("4. COMPLETE ITEM SCOREBOARD")
print("=" * 45)
print(item_summary)
