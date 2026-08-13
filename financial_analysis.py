# AI-Based Financial Analysis Assistant
# Calculates key financial ratios and provides basic interpretations.

def financial_analysis(data):
    revenue = data["revenue"]
    net_profit = data["net_profit"]
    current_assets = data["current_assets"]
    current_liabilities = data["current_liabilities"]
    total_debt = data["total_debt"]
    total_equity = data["total_equity"]

    # Financial ratios
    profit_margin = (net_profit / revenue) * 100
    current_ratio = current_assets / current_liabilities
    debt_to_equity = total_debt / total_equity

    print("FINANCIAL ANALYSIS REPORT")
    print("-" * 40)

    print(f"Net Profit Margin: {profit_margin:.2f}%")
    print(f"Current Ratio: {current_ratio:.2f}")
    print(f"Debt-to-Equity Ratio: {debt_to_equity:.2f}")

    print("\nKEY INSIGHTS")
    print("-" * 40)

    if profit_margin >= 10:
        print("• Profitability: The company has a healthy net profit margin.")
    else:
        print("• Profitability: The company may need to improve its profitability.")

    if current_ratio >= 1.5:
        print("• Liquidity: The company appears to have a comfortable short-term liquidity position.")
    elif current_ratio >= 1:
        print("• Liquidity: The company can cover its short-term liabilities, but the position should be monitored.")
    else:
        print("• Liquidity: The company may face difficulty meeting short-term obligations.")

    if debt_to_equity <= 1:
        print("• Solvency: Debt levels appear relatively manageable compared with equity.")
    else:
        print("• Solvency: The company has relatively high debt compared with equity.")


# Example financial data
company_data = {
    "revenue": 10000000,
    "net_profit": 1500000,
    "current_assets": 8000000,
    "current_liabilities": 5000000,
    "total_debt": 6000000,
    "total_equity": 10000000
}

financial_analysis(company_data)
