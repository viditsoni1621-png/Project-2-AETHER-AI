import pandas as pd
import os
from datetime import datetime


HISTORY_FILE = "prediction_history.csv"


def save_prediction(
    amount,
    prediction,
    confidence
):

    entry = {
        "Time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "Amount": amount,
        "Prediction": prediction,
        "Confidence": round(confidence, 2)
    }

    if os.path.exists(
        HISTORY_FILE
    ):

        df = pd.read_csv(
            HISTORY_FILE
        )

        df = pd.concat(
            [
                df,
                pd.DataFrame([entry])
            ],
            ignore_index=True
        )

    else:

        df = pd.DataFrame([entry])

    df.to_csv(
        HISTORY_FILE,
        index=False
    )


def load_history():

    if os.path.exists(
        HISTORY_FILE
    ):

        return pd.read_csv(
            HISTORY_FILE
        )

    return pd.DataFrame()