

def calculate_points(entry_price, target_price):
    return abs(target_price - entry_price)

def calculate_profit(points, lot_size, value_per_point):
    return points * lot_size * value_per_point

def calculate_lot_size(account_balance, risk_percent, stop_loss_points, value_per_point):
    risk_amount = (risk_percent / 100) * account_balance
    lot_size = risk_amount / (stop_loss_points * value_per_point)
    return lot_size

def main():
    print("\n📈 NAS100 ADVANCED TRADE CALCULATOR 📈\n")

    account_balance = float(input("Enter your account balance (e.g., 5000): "))
    risk_percent = float(input("Enter your risk % per trade (e.g., 1): "))
    entry_price = float(input("Enter your entry price (e.g., 19800): "))
    stop_loss_price = float(input("Enter your stop loss price (e.g., 19750): "))
    take_profit_price = float(input("Enter your take profit price (e.g., 19900): "))

    # Adjust based on your broker: 0.10 per point per 0.01 lot = $1 per point per 0.10 lot
    value_per_point_per_lot = 1  # $1 per point per 0.10 lot

    sl_points = calculate_points(entry_price, stop_loss_price)
    tp_points = calculate_points(entry_price, take_profit_price)

    recommended_lot_size = calculate_lot_size(account_balance, risk_percent, sl_points, value_per_point_per_lot)

    potential_profit = calculate_profit(tp_points, recommended_lot_size, value_per_point_per_lot)
    potential_loss = calculate_profit(sl_points, recommended_lot_size, value_per_point_per_lot)

    print("\n📊 **CALCULATION RESULTS**")
    print(f"Points to Stop Loss: {sl_points} points")
    print(f"Points to Take Profit: {tp_points} points")
    print(f"Recommended Lot Size: {recommended_lot_size:.2f} lots")
    print(f"Potential Profit at TP: ${potential_profit:.2f}")
    print(f"Potential Loss at SL: ${potential_loss:.2f}")
    print(f"Risking {risk_percent}% (${(risk_percent / 100) * account_balance:.2f}) of your account.\n")
    print("Trade wisely. Use this to align with your prop challenge discipline.\n")

if __name__ == "__main__":
    main()
