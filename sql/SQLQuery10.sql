CREATE OR ALTER VIEW vw_PerformantaLivrari AS
SELECT 
    TransportMode,
    Supplier,
    DeliveryStatus,
    COUNT(OrderID) AS TotalComenzi,
    AVG(CAST(TransitDays AS DECIMAL(10,2))) AS TimpMediuTranzitZile,
    AVG(CAST(ShippingCost AS DECIMAL(18,2))) AS CostMediuTransport
FROM supply_chain_cleaned1
GROUP BY TransportMode, Supplier, DeliveryStatus;