import numpy as np
import pandas as pd

# Setăm seed-ul pentru reproducibilitate
np.random.seed(42)

n_rows = 500

# Generăm date de bază
order_ids = [f'ORD-{1000 + i}' for i in range(n_rows)]
suppliers = np.random.choice(
    ['Alpha Logistics', 'Beta Shipping', 'Gamma Freight', 'Delta Express'],
    n_rows,
)
warehouses = np.random.choice(
    ['WH-North', 'WH-South', 'WH-East', 'WH-West'], n_rows
)
transport_modes = np.random.choice(['Road', 'Air', 'Sea'], n_rows)
destinations = np.random.choice(
    ['New York', 'new york', 'NY', 'Berlin', 'London', 'Paris   ', 'London'],
    n_rows,
)

# Generăm date calendaristice
order_dates = pd.date_range(start='2025-01-01', periods=n_rows, freq='h')
shipping_delay_days = np.random.randint(-2, 10, n_rows)
shipping_dates = order_dates + pd.to_timedelta(
    shipping_delay_days, unit='d'
)

promised_delay_days = shipping_delay_days + np.random.randint(
    -1, 3, n_rows
)
delivery_dates = order_dates + pd.to_timedelta(
    shipping_delay_days + np.maximum(0, promised_delay_days), unit='d'
)

quantities = np.random.randint(10, 500, n_rows)
shipping_costs = np.random.uniform(50, 1500, n_rows)

# Cream DataFrame-ul
df = pd.DataFrame({
    'OrderID': order_ids,
    'Supplier': suppliers,
    'Warehouse': warehouses,
    'TransportMode': transport_modes,
    'Destination': destinations,
    'OrderDate': order_dates,
    'DeliveryDate': delivery_dates,
    'Quantity': quantities,
    'ShippingCost': shipping_costs,
})

# 1. Introducem intenționat Valori Lipse (NaNs)
df.loc[np.random.choice(n_rows, 25), 'ShippingCost'] = np.nan
df.loc[np.random.choice(n_rows, 15), 'DeliveryDate'] = np.nan
df.loc[np.random.choice(n_rows, 20), 'Supplier'] = None

# 2. Introducem Anomalii Logice (Data de livrare înaintea datei de comandă)
anomaly_indices = np.random.choice(n_rows, 10)
df.loc[anomaly_indices, 'DeliveryDate'] = df.loc[
    anomaly_indices, 'OrderDate'
] - pd.Timedelta(days=5)

# 3. Introducem valori negative la costuri și cantități
df.loc[np.random.choice(n_rows, 5), 'ShippingCost'] = -250.0
df.loc[np.random.choice(n_rows, 5), 'Quantity'] = -50

# 4. Introducem Duplicate
df = pd.concat(
    [df, df.sample(15, random_state=42)], ignore_index=True
)  # 15 rânduri duplicate

# Salvăm în CSV
df.to_csv('supply_chain_messy.csv', index=False)
print(
    'Fișierul \'supply_chain_messy.csv\' a fost generat cu succes și este plin de probleme gata de curățare!'
)