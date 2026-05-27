import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from rich.console import Console
from rich.table import Table


console = Console()


# LOAD DATASET
console.print(
    "\n[cyan]Loading dataset...[/cyan]"
)

data = pd.read_csv(
    "data/creditcard.csv"
)

console.print(
    f"[green]Dataset loaded successfully.[/green]"
)

console.print(
    f"Rows: {data.shape[0]}"
)

console.print(
    f"Columns: {data.shape[1]}"
)


# FEATURES & TARGET
X = data.drop(
    "Class",
    axis=1
)

y = data["Class"]


# TRAIN TEST SPLIT
console.print(
    "\n[yellow]Splitting dataset...[/yellow]"
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# MODEL TRAINING
console.print(
    "\n[cyan]Training AI model...[/cyan]"
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

console.print(
    "[green]Model training complete.[/green]"
)


# PREDICTIONS
predictions = model.predict(
    X_test
)


# EVALUATION
accuracy = accuracy_score(
    y_test,
    predictions
)

console.print(
    f"\n[bold green]Accuracy:[/bold green] {accuracy:.4f}"
)


# CONFUSION MATRIX
cm = confusion_matrix(
    y_test,
    predictions
)

table = Table(
    title="Confusion Matrix"
)

table.add_column(
    "Metric",
    style="cyan"
)

table.add_column(
    "Value",
    style="green"
)

table.add_row(
    "True Negative",
    str(cm[0][0])
)

table.add_row(
    "False Positive",
    str(cm[0][1])
)

table.add_row(
    "False Negative",
    str(cm[1][0])
)

table.add_row(
    "True Positive",
    str(cm[1][1])
)

console.print(table)


# CLASSIFICATION REPORT
console.print(
    "\n[magenta]Classification Report[/magenta]"
)

print(
    classification_report(
        y_test,
        predictions
    )
)


# SAVE MODEL
joblib.dump(
    model,
    "model/fraud_model.pkl"
)

console.print(
    "\n[bold cyan]Model saved successfully.[/bold cyan]"
)