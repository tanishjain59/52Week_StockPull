import requests
from datetime import datetime, timedelta
import sys

def fetch_daily_data(stock_symbol, date, api_key):
    url = f"https://api.polygon.io/v1/open-close/{stock_symbol}/{date}?adjusted=true&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {date}: {response.text}")
        return None

def find_6_month_high_low(stock_symbol, api_key):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=6*30)  # 6 months
    current_date = start_date
    highs = []
    lows = []

    while current_date <= end_date:
        data = fetch_daily_data(stock_symbol, current_date.strftime('%Y-%m-%d'), api_key)
        if data:
            highs.append(data['high'])
            lows.append(data['low'])
        current_date += timedelta(days=1)

    return max(highs), min(lows)

def main():
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Usage: python3 main.py <STOCK_SYMBOL> <API_KEY>")
        sys.exit(1)

    stock_symbol = sys.argv[1].upper()
    api_key = 'B4rnW9AXRV3T0vfueCYLxmGwvVpy3XUv'

    high, low = find_6_month_high_low(stock_symbol, api_key)
    print(f"6-Month High for {stock_symbol}: ${high}")
    print(f"6-Month Low for {stock_symbol}: ${low}")

if __name__ == "__main__":
    main()