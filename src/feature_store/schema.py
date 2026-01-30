FEATURE_SCHEMA = {
    "entity_id": "customerID",
    "target": "Churn",
    "numerical": [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ],
    "categorical": [
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod"
    ]
}
