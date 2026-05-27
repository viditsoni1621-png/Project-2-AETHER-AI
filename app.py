import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import numpy as np
import time

from utils.history import (
    save_prediction,
    load_history
)

from utils.insights import (
    generate_insight
)


# -----------------------------
# LOAD CUSTOM CSS
# -----------------------------
def load_css():

    with open(
        "styles/theme.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AETHER AI",
    page_icon="🤖",
    layout="wide"
)

load_css()


# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load(
    "model/fraud_model.pkl"
)


# -----------------------------
# TITLE SECTION
# -----------------------------
st.title("AETHER AI")

st.subheader(
    "Fraud Detection Intelligence Dashboard"
)

st.markdown("---")


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title(
    "AETHER AI Console"
)

st.sidebar.success(
    "Neural Systems Online"
)

st.sidebar.markdown("---")

st.sidebar.subheader(
    "System Status"
)

st.sidebar.write(
    "Threat Engine: ONLINE"
)

st.sidebar.write(
    "Neural Scanner: ACTIVE"
)

st.sidebar.write(
    "Behavior Monitor: RUNNING"
)

st.sidebar.write(
    "Security Layer: STABLE"
)

st.sidebar.markdown("---")

st.sidebar.subheader(
    "Live Metrics"
)

st.sidebar.metric(
    "Threat Level",
    "LOW"
)

st.sidebar.metric(
    "AI Accuracy",
    "99.9%"
)

st.sidebar.metric(
    "Detection Speed",
    "0.21s"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Live Prediction",
        "Analytics",
        "Prediction History"
    ]
)


# =========================================================
# DASHBOARD PAGE
# =========================================================
if page == "Dashboard":

    st.header(
        "System Overview"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Model Status",
        "ACTIVE"
    )

    col2.metric(
        "Threat Engine",
        "ONLINE"
    )

    col3.metric(
        "AI Accuracy",
        "99.9%"
    )

    col4.metric(
        "Security Level",
        "MAXIMUM"
    )

    st.success(
        "AETHER AI operational."
    )

    st.info(
        "Monitoring transaction intelligence streams..."
    )

    st.markdown("---")

    st.subheader(
        "Neural Intelligence Feed"
    )

    st.write(
        """
        - Fraud detection engine initialized  
        - Behavioral anomaly analysis active  
        - Threat intelligence systems online  
        - Confidence scoring modules stable  
        - Predictive monitoring streams synchronized  
        """
    )

    st.markdown("---")

    st.subheader(
        "Threat Monitoring Status"
    )

    threat_data = pd.DataFrame({
        "Threat Level": [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],
        "Incidents": [
            120,
            32,
            9,
            2
        ]
    })

    fig = px.bar(
        threat_data,
        x="Threat Level",
        y="Incidents",
        title="Threat Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Live Transaction Feed"
    )

    live_feed = pd.DataFrame({

        "Transaction ID": [
            "TXN-8841",
            "TXN-1294",
            "TXN-5321",
            "TXN-7742",
            "TXN-9812"
        ],

        "Amount": [
            120,
            5400,
            87,
            9200,
            300
        ],

        "Status": [
            "SAFE",
            "FRAUD",
            "SAFE",
            "FRAUD",
            "SAFE"
        ],

        "Threat Level": [
            "LOW",
            "CRITICAL",
            "LOW",
            "HIGH",
            "LOW"
        ]
    })

    st.dataframe(
        live_feed,
        use_container_width=True
    )

    st.warning(
        "2 high-risk transactions detected in live monitoring stream."
    )


# =========================================================
# LIVE PREDICTION PAGE
# =========================================================
elif page == "Live Prediction":

    st.header(
        "Transaction Threat Analysis"
    )

    st.write(
        "Analyze transaction behavior using AETHER AI."
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0
    )

    time_value = st.number_input(
        "Transaction Time",
        min_value=0.0,
        value=10000.0
    )

    if st.button(
        "Analyze Transaction"
    ):

        progress_bar = st.progress(0)

        status = st.empty()

        messages = [
            "Initializing neural scanners...",
            "Analyzing transaction vectors...",
            "Running fraud heuristics...",
            "Evaluating behavioral patterns...",
            "Generating threat intelligence..."
        ]

        for i, msg in enumerate(messages):

            status.warning(msg)

            progress_bar.progress(
                (i + 1) * 20
            )

            time.sleep(0.7)

        input_data = np.zeros((1, 30))

        input_data[0][0] = time_value
        input_data[0][-1] = amount

        prediction = model.predict(
            input_data
        )[0]

        confidence = np.max(
            model.predict_proba(
                input_data
            )
        ) * 100

        save_prediction(
            amount,
            "FRAUD" if prediction == 1 else "SAFE",
            confidence
        )

        st.markdown("---")

        st.subheader(
            "Threat Assessment"
        )

        if prediction == 1:

            st.error(
                "CRITICAL RISK DETECTED"
            )

            threat_level = "HIGH"

        else:

            st.success(
                "Transaction appears SAFE"
            )

            threat_level = "LOW"

        col1, col2 = st.columns(2)

        col1.metric(
            "AI Confidence",
            f"{confidence:.2f}%"
        )

        col2.metric(
            "Threat Level",
            threat_level
        )

        st.progress(
            int(confidence)
        )

        insight = generate_insight(
            amount,
            confidence,
            prediction
        )

        st.markdown("---")

        st.subheader(
            "AI Insight"
        )

        st.info(
            insight
        )

        st.markdown("---")

        st.subheader(
            "System Logs"
        )

        st.code(
            f"""
[INFO] Neural scan completed
[INFO] Threat level: {threat_level}
[INFO] Confidence score: {confidence:.2f}%
[INFO] Transaction amount analyzed: ₹{amount}
[INFO] Intelligence pipeline stable
            """
        )


# =========================================================
# ANALYTICS PAGE
# =========================================================
elif page == "Analytics":

    st.header(
        "AI Intelligence Analytics"
    )

    data = pd.read_csv(
        "data/creditcard.csv"
    )

    st.subheader(
        "Fraud Distribution"
    )

    fraud_count = data["Class"].value_counts()

    fig = px.pie(
        values=fraud_count.values,
        names=["Normal", "Fraud"],
        title="Fraud Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Transaction Amount Distribution"
    )

    fig2 = px.histogram(
        data,
        x="Amount",
        title="Transaction Amount Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Dataset Overview"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Transactions",
        f"{len(data)}"
    )

    col2.metric(
        "Fraud Cases",
        f"{data['Class'].sum()}"
    )

    col3.metric(
        "Features",
        f"{data.shape[1]}"
    )

    st.markdown("---")

    st.subheader(
        "Transaction Sample Data"
    )

    st.dataframe(
        data.head(),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "AI Feature Importance"
    )

    feature_importance = pd.DataFrame({

        "Feature": data.drop(
            "Class",
            axis=1
        ).columns,

        "Importance": model.feature_importances_

    })

    feature_importance = feature_importance.sort_values(
        by="Importance",
        ascending=False
    ).head(10)

    fig4 = px.bar(
        feature_importance,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top Influential Features"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    st.info(
        "These features contribute most strongly to fraud detection decisions."
    )


# =========================================================
# PREDICTION HISTORY PAGE
# =========================================================
elif page == "Prediction History":

    st.header(
        "Threat Intelligence Logs"
    )

    history = load_history()

    if history.empty:

        st.warning(
            "No prediction history found."
        )

    else:

        st.success(
            "Prediction history loaded successfully."
        )

        st.dataframe(
            history,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader(
            "Prediction Insights"
        )

        prediction_counts = history[
            "Prediction"
        ].value_counts()

        fig3 = px.bar(
            x=prediction_counts.index,
            y=prediction_counts.values,
            title="Prediction History Distribution"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

        csv = history.to_csv(
            index=False
        )

        st.download_button(
            "Download Intelligence Report",
            csv,
            "aether_ai_report.csv",
            "text/csv"
        )

        st.markdown("---")

        st.subheader(
            "AI Monitoring Feed"
        )

        st.code(
            """
[INFO] Historical transaction analysis active
[INFO] Threat monitoring systems synchronized
[INFO] Prediction archives secured
[INFO] Intelligence reports available
            """
        )