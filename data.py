import pandas as pd



#Load the csv file
df = pd.read_csv('C:\\Users\DELL\Documents\Work.csv')

#Calculate total revenue
total_revenue = df['Sold Revenue($)'].sum()
print(f"Total Revenue: ${total_revenue}")

best_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()
best_selling_product_quantity = df.groupby('Product')['Quantity'].sum().max()

print(f"Best-Selling Product: {best_selling_product} ({best_selling_product_quantity} units sold)")



#Load the csv file
df = pd.read_csv('C:\\Users\DELL\Documents\Work.csv')


df['Date'] = pd.to_datetime(df['Date'])
highest_sales_day = df.groupby('Date')['Sold Revenue($)'].sum().idxmax()

print(f"Highest Sales Day: {highest_sales_day.date()}")

with open('sales_summary.txt', 'w') as f:
    f.write(f"Total Revenue: ${total_revenue}\n")
    f.write(f"Best-Selling Product: {best_selling_product} ({best_selling_product_quantity} units sold)\n")
    f.write(f"Highest Sales Day: {highest_sales_day.date()}\n")
    
    
