import csv

def financial_analysis(row):
    revenue = float(row["Revenue"])
    net_profit = float(row["Net_Profit"])
    current_assets = float(row["Current_Assets"])
    current_liabilities = float(row["Current_Liabilities"])
    total_debt = float(row["Total_Debt"])
    total_equity = float(row["Total_Equity"])

    profit_margin = (net_profit / revenue) * 100
    current_ratio = current_assets / current_liabilities
    debt_to_equity = total_debt / total_equity

    print(f"\nFINANCIAL ANALYSIS - {row['Company']} ({row['Year']})")
    print("-" * 45)

    print(f"Revenue: ₹{revenue:,.0f}")
    print(f"Net Profit: ₹{net_profit:,.0f}")
    print(f"Net Profit Margin: {profit_margin:.2f}%")
    print(f"Current Ratio: {current_ratio:.2f}")
    print(f"Debt-to-Equity Ratio: {debt_to_equity:.2f}")

    print("\nKEY INSIGHTS")
    print("-" * 45)

    if profit_margin >= 10:
        print("• Profitability is relatively healthy.")
    else:
        print("• Profitability may need improvement.")

    if current_ratio >= 1.5:
        print("• Liquidity position is comfortable.")
    elif current_ratio >= 1:
        print("• Short-term liquidity is adequate but should be monitored.")
    else:
        print("• Short-term liquidity may require attention.")

    if debt_to_equity <= 1:
        print("• Debt levels are relatively manageable.")
    else:
        print("• Debt is relatively high compared with equity.")


# Read financial data from CSV
with open("data/financial_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        financial_analysis(row)
