# Advanced Supply Chain & Logistics Analytics Dashboard

An end-to-end **Data Engineering & Business Intelligence** project focused on analyzing global supply chain performance, transportation costs, shipping delays, and warehouse operational efficiency.

---

## 🛠️ Project Architecture & Tech Stack
1. **Python (Pandas, NumPy):** Data preprocessing, cleaning missing values, handling anomalies, and feature engineering (recalculating unit shipping costs: `ShippingCostPerUnit`).
2. **SQL Server:** Relational database management featuring **10 Advanced Views** built with **Common Table Expressions (CTEs)** and **Window Functions** (`RANK()`, `LAG()`, `SUM() OVER`, `PERCENT_RANK()`) to deliver clean, pre-aggregated data.
3. **Power BI:** An executive Control Tower dashboard designed with zero redundancy, transforming raw data into high-impact visual metrics for management.

---

## 📊 Dashboard Summary & Components (Power BI)

The final dashboard is structured into a single, dense, highly interactive executive page covering:
- **Global KPI Cards (Top):** Instant visibility over 500 total orders, a total transport spend of $32.84M, an average unit shipping cost of $597.32, and an average transit time of 8.29 days.
- **Destination & Delay Analysis:** Order distributions across key hubs (New York, London, Paris, Berlin), clearly contrasting *In-Time* versus *Delayed* shipments.
- **Warehouse Hub Load:** Percentage share of total order volume handled by each distribution center (WH-North: 27.2%, WH-West: 26.4%, WH-South: 24.4%, WH-East: 22%).
- **Transport Mode Efficiency:** Volume count (`Count of OrderID`) mapped against total costs (`Sum of ShippingCost`) across Air, Road, and Sea routes.
- **Supplier Performance:** Granular breakdown of suppliers (*Delta Express, Alpha Logistics, Gamma Freight, Beta Shipping*) segmented by transportation mode[cite: 1].

---

## 📈 Key Insights & Business Conclusions

Based on the dashboard visualizations, the following strategic takeaways emerge for management:

1. **Split Delivery Health (OTD Rate):** The overall delivery performance shows an almost even split between **50.8% (254 orders) on-time** and **49.2% (246 orders) delayed**. This nearly 50% delay margin indicates a systemic bottleneck across carriers or routes, requiring urgent SLA (Service Level Agreement) re-evaluations.
2. **Uniform Volumes, Divergent Transport Costs:** While order volumes shipped via *Air, Road*, and *Sea* are nearly identical (~160–170 orders each), air freight total costs peak significantly higher than alternative modes, highlighting a heavy financial reliance on expedited shipping.
3. **New York – Primary High-Risk Market:** New York concentrates the highest absolute order volume (over 220 orders) but also suffers from the highest absolute number of delays (107 delayed orders), making it the number one critical region impacting customer satisfaction.
4. **Balanced Warehouse Distribution:** Logistics flow is well-distributed among the 4 regional hubs, with *WH-North* holding the highest load at 27.2% and *WH-West* at 26.4%, indicating that operational stress is not concentrated inside a single warehouse.

---

## 🚀 How to Run
1. Run the Python preprocessing script from the `/python` folder on your raw dataset.
2. Execute the SQL scripts in the `/sql` folder within SSMS to generate the optimized views.
3. Open the `.pbix` file in Power BI and refresh the data source connection to your local SQL Server instance.
