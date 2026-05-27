from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.platypus.tables import (
    Table
)

from reportlab.lib import colors


def generate_report(history):

    doc = SimpleDocTemplate(
        "AETHER_AI_Report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "AETHER AI Intelligence Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    data = [
        [
            "Amount",
            "Prediction",
            "Confidence"
        ]
    ]

    for _, row in history.iterrows():

        data.append([
            row["Amount"],
            row["Prediction"],
            row["Confidence"]
        ])

    table = Table(data)

    table.setStyle([
        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.cyan
        ),

        (
            "TEXTCOLOR",
            (0, 0),
            (-1, 0),
            colors.black
        ),

        (
            "GRID",
            (0, 0),
            (-1, -1),
            1,
            colors.white
        )
    ])

    elements.append(table)

    doc.build(elements)