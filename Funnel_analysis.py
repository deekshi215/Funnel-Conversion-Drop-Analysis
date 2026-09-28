#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import library
import pandas as pd


# In[2]:


# Load the dataset
df = pd.read_csv(r"C:\Users\drdee\Downloads\funnel_raw_data.csv")


# In[3]:


# Check the first five rows
df.head()


# In[4]:


# Check number of rows and columns
df.shape


# In[5]:


# check all column names
df.columns.tolist()


# In[6]:


#check columns, datatypes and non-null values
df.info()


# In[7]:


# check summary statistics
df.describe()


# In[8]:


# Check missing values
df.isnull().sum()


# In[9]:


# check duplicate rows
df.duplicated().sum()


# In[10]:


# Convert Event Time into date & time format
df['Event Time'] = pd.to_datetime(df['Event Time'])


# In[11]:


# Analyze where do users drop off the most in the funnel
funnel_counts = df.groupby('Event')['User ID'].nunique()
print(funnel_counts)


# In[12]:


# Calculate drop-off
drop_off = funnel_counts.diff()
print("\nDrop-off between stages:\n", drop_off)


# In[13]:


# Conversion rate at each stage
browse = funnel_counts.get('Browse', 0)
cart = funnel_counts.get('Add to Cart', 0)
checkout = funnel_counts.get('Checkout', 0)
purchase = funnel_counts.get('Purchase', 0)
print("Browse → Cart:", round(cart / browse * 100, 2), "%")
print("Cart → Checkout:", round(checkout / cart * 100, 2), "%")
print("Checkout → Purchase:", round(purchase / checkout * 100, 2), "%")


# In[14]:


# Overall conversion rate(browse-purchase)
overall_conversion = (purchase / browse) * 100
print("Overall Conversion Rate:", round(overall_conversion, 2), "%")


# In[15]:


# Identify the device with the highest conversion rate
device_users = df.groupby('Device')['User ID'].nunique()

device_purchases = (
    df[df['Event'] == 'Purchase']
    .groupby('Device')['User ID']
    .nunique()
)

device_conversion = (device_purchases / device_users) * 100
print(device_conversion.sort_values(ascending=False))


# In[16]:


# Identify the marketing channel driving the highest conversions and revenue
channel_conversion = df[df['Event'] == 'Purchase'] \
    .groupby('Channel')['User ID'].nunique()
print("Conversions by Channel:\n", channel_conversion.sort_values(ascending=False))


# In[17]:


# Revenue
channel_revenue = df[df['Event'] == 'Purchase'] \
    .groupby('Channel')['Revenue'].sum()


# In[18]:


print("\nRevenue by Channel:\n", channel_revenue.sort_values(ascending=False))


# In[19]:


# Identify the segment contributing the highest revenue
# By device
device_revenue = df[df['Event'] == 'Purchase'] \
.groupby('Device')['Revenue'].sum()
print(device_revenue.sort_values(ascending=False))


# In[20]:


# By region
region_revenue = df[df['Event'] == 'Purchase'] \
.groupby('Region')['Revenue'].sum()
print(region_revenue.sort_values(ascending=False))


# In[21]:


 #By product category
category_revenue = df[df['Event'] == 'Purchase'] \
.groupby('Product Category')['Revenue'].sum()
print(category_revenue.sort_values(ascending=False))


# In[22]:


# Save cleaned dataset
df.to_csv(
    r"C:\Users\drdee\Downloads\Funnel_cleaned_data.csv",
    index=False
)


