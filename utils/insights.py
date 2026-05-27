def generate_insight(
    amount,
    confidence,
    prediction
):

    if prediction == 1:

        if amount > 1000:

            return (
                "Critical anomaly detected in "
                "high-value transaction stream."
            )

        return (
            "Suspicious behavioral pattern "
            "identified by AI engine."
        )

    else:

        if confidence > 95:

            return (
                "Transaction verified with "
                "strong behavioral consistency."
            )

        return (
            "Low-risk transaction with "
            "minimal anomaly indicators."
        )