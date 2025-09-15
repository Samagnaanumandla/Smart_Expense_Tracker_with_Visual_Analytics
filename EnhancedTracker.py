# EnhancedAnalytics.py

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "data.csv"

class color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"

def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        df["Date"] = pd.to_datetime(df["Date"], format="mixed", errors="coerce")
        return df
    except FileNotFoundError:
        print(f"{color.WARNING}⚠️ No data file found.{color.ENDC}")
        return pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])

def ai_insight(df):
    if df.empty:
        return "No spending data available for insights."
    top_cat = df.groupby("Category")["Amount"].sum().idxmax()
    top_amt = df.groupby("Category")["Amount"].sum().max()
    high_day = df.groupby("Date")["Amount"].sum().idxmax().strftime("%Y-%m-%d")
    return f"You spent the most on {top_cat} (₹{top_amt:.2f}). Your costliest day was {high_day}."

def plot_expense_by_category():
    df = load_data()
    if df.empty:
        print("No data to display.")
        return
    category_sum = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    category_sum.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6), startangle=90)
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def plot_daily_trend():
    df = load_data()
    if df.empty:
        print("No data to display.")
        return
    daily = df.groupby("Date")["Amount"].sum()
    daily.plot(kind="line", marker="o", linestyle="-", color="green")
    plt.title("Daily Expense Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Expense")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_monthly_trend():
    df = load_data()
    if df.empty:
        print("No data to display.")
        return
    monthly = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()
    monthly.plot(kind="bar", color="skyblue")
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_top_categories(n=5):
    df = load_data()
    if df.empty:
        print("No data to display.")
        return
    top = df.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(n)
    print(f"{color.OKGREEN}💰 Top {n} Spending Categories:{color.ENDC}")
    print(top)

def show_statistics():
    df = load_data()
    if df.empty:
        print("No data to display.")
        return
    total = df["Amount"].sum()
    avg_per_day = df.groupby("Date")["Amount"].sum().mean()
    print(f"{color.OKBLUE}🔢 Total Spent: ₹{total:.2f}{color.ENDC}")
    print(f"{color.OKCYAN}📅 Average Daily Spend: ₹{avg_per_day:.2f}{color.ENDC}")
    print(f"{color.HEADER}📊 AI Insight: {ai_insight(df)}{color.ENDC}")

if __name__ == "__main__":
    while True:
        print(f"\n{color.HEADER}--- Expense Analytics ---{color.ENDC}")
        print("1. Show Statistics & Insights")
        print("2. Top Categories")
        print("3. Plot by Category")
        print("4. Plot Daily Trend")
        print("5. Plot Monthly Trend")
        print("6. Exit")

        choice = input("Choose option: ")
        if choice == "1":
            show_statistics()
        elif choice == "2":
            show_top_categories()
        elif choice == "3":
            plot_expense_by_category()
        elif choice == "4":
            plot_daily_trend()
        elif choice == "5":
            plot_monthly_trend()
        elif choice == "6":
            break
        else:
            print(f"{color.FAIL}❌ Invalid option.{color.ENDC}")
