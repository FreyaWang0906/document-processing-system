#This is just a placeholder model used to demonstrate the workflow.
#In a real project, it should be replaced with a trained PyTorch model for actual document classification.
import torch
import torch.nn as nn
import torch.nn.functional as F

# Dummy keyword-based classification
LABELS = {
    "resume": ["education", "experience", "skills"],
    "invoice": ["total", "amount", "tax"],
    "contract": ["agreement", "terms", "party"]
}

def classify_text(text: str) -> str:
    """
    A naive rule-based classifier to simulate model prediction.
    """
    text = text.lower()
    scores = {label: 0 for label in LABELS}

    for label, keywords in LABELS.items():
        for kw in keywords:
            if kw in text:
                scores[label] += 1

    best_label = max(scores, key=scores.get)
    return best_label if scores[best_label] > 0 else "unknown"