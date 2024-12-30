import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

amazon_df = pd.read_json('amazon_products.json')

bestbuy_df = pd.read_json('bestbuy_headphones.json')

amazon_df.dropna(subset=['Product Name', 'Price', 'True Price'], inplace = True)
amazon_df['Price'] = amazon_df['Price'].replace('[\$,]', '', regex=True).astype(float)
amazon_df['True Price'] = amazon_df['True Price'].replace('[\$,]', '', regex=True).astype(float)

bestbuy_df.dropna(subset=['Product Name', 'Price', 'True Price'], inplace=True)
bestbuy_df['Price'] = bestbuy_df['Price'].replace('[\$,]', '', regex=True).astype(float)
bestbuy_df['True Price'] = bestbuy_df['True Price'].replace('[\$,]', '', regex=True).astype(float)

amazon_df['Savings'] = amazon_df['True Price'] - amazon_df['Price']

bestbuy_df['Savings'] = bestbuy_df['True Price'] - bestbuy_df['Price']

average_savings_amazon = amazon_df['Savings'].mean()
average_savings_bestbuy = bestbuy_df['Savings'].mean()

print(f'Average Savings on Amazon: ${average_savings_amazon:.2f}')
print(f'Average Savings on Best Buy: ${average_savings_bestbuy:.2f}')

max_savings_amazon_idx = amazon_df['Savings'].idxmax()
max_saving_amazon = amazon_df.loc[max_savings_amazon_idx]

print('\nProdict with the biggest savings on Amazon:')
print(max_saving_amazon)

max_savings_bestbuy_idx = bestbuy_df['Savings'].idxmax()
max_savings_bestbuy = bestbuy_df.loc[max_savings_bestbuy_idx]

print('\nProdict with the biggest savings on best Buy:')
print(max_savings_bestbuy)

sns.set_theme(style='whitegrid')

average_savings_df = pd.DataFrame({
    'Site': ['Amazon', 'Best Buy'],
    'Average Savings': [average_savings_amazon, average_savings_bestbuy]
})

plt.figure(figsize=(8,6))
sns.barplot(x='Site', y='Average Savings', data= average_savings_df)
plt.title('Average Savings on Each Site')
plt.xlabel('Site')
plt.ylabel('Average Savings ($)')
plt.show()