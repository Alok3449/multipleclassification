import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def plot_stock_trend(ticker, company_name):
    data = yf.download(ticker, period="12d", interval="1d")

    if data.empty:
        print(f" No data found for {company_name} ({ticker})")
        return

    dates = data.index.strftime('%Y-%m-%d').tolist()
    closing_prices = data['Close'].values.tolist()

    color = 'green' if closing_prices[-1] > closing_prices[0] else 'red'
    trend = "📈 Stock is rising" if color == 'green' else "📉 Stock is falling"

    x_vals = np.arange(len(dates)).reshape(-1, 1)
    y_vals = np.array(closing_prices)

    model = LinearRegression()
    model.fit(x_vals, y_vals)
    y_pred = model.predict(x_vals)

    plt.figure(figsize=(9, 5))
    plt.plot(dates, closing_prices, marker='o', color=color, linewidth=2, label='Stock Price')
    plt.plot(dates, y_pred, linestyle='--', color='Blue', linewidth=2, label='Regression Line')

    plt.title(f"{company_name} Stock Trend (Last 12 Days)")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (INR)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

    print(f"{company_name}: {trend}\n")

# Listed company
companies = [
    ("PNB BANK", "PNB.NS"),
    ("Reliance Private Limited", "RELIANCE.NS"),
    ("Tata Steel", "TATASTEEL.NS")
]

# Loop through each company
for company_name, ticker in companies:
    plot_stock_trend(ticker, company_name)
