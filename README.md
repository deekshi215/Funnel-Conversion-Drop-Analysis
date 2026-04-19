# Funnel & Conversion Drop Analysis




## Problem Statement

This dashboard helps businesses understand how users move through the conversion funnel and where they drop off. It enables the organization to identify bottlenecks in the user journey, improve conversion rates, and optimize marketing and product strategies.

Through this dashboard, businesses can track user progression from browsing to purchase, identify the stage with the highest drop-off, and analyze performance across devices, channels, and regions.

## Tools & Technologies Used
- Power BI Desktop
- Power Query (Data Transformation)
- Data Modeling 
- Python (Data Cleaning & Preprocessing)
- Pandas, NumPy, Matplotlib
- GitHub

## Steps Followed

**Step 1: Load the Dataset

  The dataset was imported from a CSV file containing user interaction events across different funnel stages.

**Step 2: Data Cleaning using Python

  Data preprocessing was performed using Python before loading into Power BI:

- Removed duplicate records
- Handled missing/null values
- Standardized event names (Browse, Add to Cart, Checkout, Purchase)
- Converted timestamp column to datetime format
- Filtered inconsistent or invalid entries

  This ensured accurate funnel tracking and analysis.

**Step 3: Data Transformation (Power Query)
- Verified column data types
- Created derived columns if required
- Ensured clean and structured dataset for modeling

**Step 4: Data Modeling

  A structured data model was created to support analysis:

- Fact Table → User Events
- Dimension Tables → Device, Channel, Region, Date

**Step 5: Funnel Creation

  A funnel visualization was built to represent user progression:

- Browse → Add to Cart → Checkout → Purchase

  This helps in understanding how users move step-by-step through the journey.

**Step 6: KPI Metrics

  Key performance indicators were added:

- Total Users
- Conversion Rate
- Total Revenue
- Drop-off Rate

**Step 7: Drop-Off Analysis

  A stage-wise drop-off analysis was created to identify where users exit the funnel.

**Step 8: Segmentation Analysis

  Multiple visualizations were added for deeper insights:

- Users by Device (Desktop, Mobile, Tablet)
- Users by Channel (Organic, Ads, Email, Social Media)
- Revenue by Region (North, South, East, West)

**Step 9: Interactive Filters

  Slicers were added for:

- Device
- Channel
- Region
- Time Range

  This allows dynamic exploration of user behavior.

**Step 10: Dashboard Design

  An interactive dashboard was built with:

- Funnel Chart
- Bar Charts
- KPI Cards
- Drop-off Visualization

## Dataset

The dataset used for this project is available in this repository.

File:
- Funnel_Analysis_Data.csv

The dataset includes:

- User ID
- Event Type (Browse, Cart, -Checkout, Purchase)
- Timestamp
- Device Type
- Channel Source
- Region
- Revenue

## Power BI Project File

The complete Power BI dashboard file is available in this repository.

File:
- Funnel_Conversion_Drop_Analysis.pbix

You can download and open it using Microsoft Power BI Desktop to explore the interactive dashboard.


## 

<img width="1296" height="733" alt="Image" src="https://github.com/user-attachments/assets/cd81147b-fad2-4ad2-ba02-869829d73213" />


<img width="1302" height="731" alt="Image" src="https://github.com/user-attachments/assets/767a5e9b-37b8-4394-addf-d94ed9a785a0" />

### Funnel Conversion

- Browse: 10K users
- Add to Cart: 7K users
- Checkout: 3K users
- Purchase: 1K users

### Drop-Off Rate by Stage
- Browse → Cart: 30.51% drop
- Cart → Checkout: 65.44% drop
- Checkout → Purchase: 89.96% drop  (Highest)

## Insights

### Funnel Performance
- Only 10% of users convert from browsing to purchase
- Significant user loss occurs at each stage

### Highest Drop-Off Stage
The Checkout → Purchase stage has the highest drop-off (~90%)
This indicates major issues like:
- Complicated checkout process
- Payment failures
- Lack of trust or pricing concerns

### Device Analysis
Desktop and Tablet users show slightly higher engagement than Mobile
Mobile experience may need optimization

### Channel Performance
Organic, Email, and Ads bring similar traffic
Social Media contributes slightly lower users

### Regional Performance
- South region generates highest revenue
- West region shows lowest performance

## Conclusion

This dashboard highlights critical bottlenecks in the user journey. The biggest opportunity lies in improving the checkout experience, as it has the highest drop-off rate.

By optimizing payment flow, simplifying checkout steps, and improving mobile usability, businesses can significantly increase conversions and revenue.
