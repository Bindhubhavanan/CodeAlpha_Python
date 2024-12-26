import requests
import json

# Define the API key and base URL for Alpha Vantage
API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'  # Replace with your own Alpha Vantage API key
BASE_URL = 'https://www.alphavantage.co/query?'

# Function to get the stock price using Alpha Vantage API
def get_stock_price(symbol):
    url = f"{BASE_URL}function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if the response contains the data for the stock symbol
        if 'Time Series (5min)' in data:
            latest_time = next(iter(data['Time Series (5min)']))  # Get the latest timestamp
            latest_data = data['Time Series (5min)'][latest_time]
            closing_price = float(latest_data['4. close'])
            return closing_price
        else:
            print(f"Error: Stock data for {symbol} not found.")
            return None
    else:
        print(f"Error fetching data for {symbol}. HTTP Status code: {response.status_code}")
        return None

# Portfolio class to manage the stock investments
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Dictionary to store stock symbol and the number of shares
    
    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")
    
    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio and self.portfolio[symbol] >= shares:
            self.portfolio[symbol] -= shares
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            print(f"Removed {shares} shares of {symbol} from your portfolio.")
        else:
            print(f"Error: You don't have {shares} shares of {symbol} in your portfolio.")
    
    def track_performance(self):
        total_value = 0
        print("\nCurrent Portfolio:")
        for symbol, shares in self.portfolio.items():
            price = get_stock_price(symbol)
            if price:
                value = price * shares
                total_value += value
                print(f"{symbol}: {shares} shares @ ${price:.2f} each, Total: ${value:.2f}")
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        
# Main function to interact with the user
def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Performance")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL, MSFT, TSLA): ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(symbol, shares)
        
        elif choice == '2':
            symbol = input("Enter stock symbol to remove (e.g., AAPL, MSFT, TSLA): ").upper()
            shares = int(input("Enter the number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        
        elif choice == '3':
            portfolio.track_performance()
        
        elif choice == '4':
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
