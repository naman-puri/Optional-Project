import matplotlib.pyplot as plt
import csv

#Step 1:
with open('data.csv', mode='r') as r:
    r = csv.reader(r)
    data = list(r)
    data.pop(0)

#Step 2:
years = [int(row[0]) for row in data]
total_sales = [sum(map(int, row[1:])) for row in data]

with open('stats.txt', 'w') as outfile:
    for year, sales in zip(years, total_sales):
        outfile.write(f"{year}: {sales}\n")

#Step 3:
plt.bar(years, total_sales)

plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Sales by Year')

plt.show()

#Step 4:

#sales data for all 12 months of 2021 and 2022 on different arrays but same line
sales_data = ([110903, 114510, 153722, 154105, 152141, 162549, 153081, 146164, 143922, 122925, 115241, 109077],
              [36922, 39082, 55611, 57110, 56991, 66514, 0, 0, 0, 0, 0, 0])

sales_2021 = sum(sales_data[0][:6])
print("Total sales in first 6 months of 2021:", sales_2021)

sales_2022 = sum(sales_data[1][:6])
print("Total sales in first 6 months of 2022:", sales_2022)

Sales_Growth_Rate = (sales_2022 - sales_2021) / sales_2021
print("Sales growth rate for first 6 months of 2022:", Sales_Growth_Rate)

est_2022_last_6_months = [x + x * Sales_Growth_Rate for x in sales_data[0][6:]]
print("Estimated sales for last six months of 2022:", est_2022_last_6_months)

with open("stats.txt", "a") as file:
    file.write("\n\nTotal sales in first 6 months of 2021: {}\n".format(sales_2021))
    file.write("Total sales in first 6 months of 2022: {}\n".format(sales_2022))
    file.write("Sales growth rate for first 6 months of 2022: {:.2f}\n".format(Sales_Growth_Rate))
    file.write("Estimated sales for last six months of 2022: {}\n".format(est_2022_last_6_months))

#Step 5:
months = ['July', 'August', 'September', 'October', 'November', 'December']
plt.figure()
plt.barh(months, est_2022_last_6_months)
plt.xlabel('Estimated Sales')
plt.ylabel('Months')
plt.title('Estimated Sales for Last Six Months of 2022')
plt.show()