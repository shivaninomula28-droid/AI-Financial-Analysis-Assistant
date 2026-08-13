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
    reader = list(csv.DictReader(file))

for row in reader:
    financial_analysis(row)

# Year-on-year growth analysis
if len(reader) >= 2:
    previous_year = reader[-2]
    current_year = reader[-1]

    revenue_growth = (
        (float(current_year["Revenue"]) - float(previous_year["Revenue"]))
        / float(previous_year["Revenue"])
    ) * 100

    profit_growth = (
        (float(current_year["Net_Profit"]) - float(previous_year["Net_Profit"]))
        / float(previous_year["Net_Profit"])
    ) * 100

    print("\nYEAR-ON-YEAR GROWTH")
    print("-" * 45)
    print(f"Revenue Growth: {revenue_growth:.2f}%")
    print(f"Net Profit Growth: {profit_growth:.2f}%")
