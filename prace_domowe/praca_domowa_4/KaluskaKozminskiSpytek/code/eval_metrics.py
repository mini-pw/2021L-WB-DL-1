import numpy as np
from sklearn.metrics import roc_auc_score


def confusion_matrix(y_pred, y):
    y = y.flatten()
    y_pred = y_pred.flatten()
    y = y.astype(np.int16)

    n_labels = 2
    cm = np.zeros((n_labels, n_labels))

    def assign(x1, x2):
        cm[x1, x2] += 1

    np.vectorize(assign)(y, y_pred)
    return cm


def accuracy(y_pred, y, cm=None):
    """
    Proporcja dobrze sklasyfikowanych obserwacji do liczby wszystkich obserwacji.
    """
    if cm is None:
        cm = confusion_matrix(y_pred, y)

    TN, FP, FN, TP = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
    return (TP + TN) / (TN + FP + FN + TP)


def precision(y_pred, y, cm=None):
    """
    Stosunek właściwie wykrytych wartości pozytywnych do wszystkich wartości sklasyfikowanych jako pozytywne.
    """
    if cm is None:
        cm = confusion_matrix(y_pred, y)
    TN, FP, FN, TP = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
    return TP / (TP + FP)


def recall(y_pred, y, cm=None):
    """
    Stosunek wykrytych obserwacji pozytywnych do wszystkich obserwacji pozytywnych.
    Alternatywna nazwa 'sensitivity'
    """
    if cm is None:
        cm = confusion_matrix(y_pred, y)
    TN, FP, FN, TP = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
    return TP / (TP + FN)


def specificity(y_pred, y, cm=None):
    """
    Stosunek poprawnie wykrytych obserwacji negatywnych do wszystkich obserwacji negatywnych.
    """
    if cm is None:
        cm = confusion_matrix(y_pred, y)
    TN, FP, FN, TP = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
    return TN / (TN + FP)


def dice_coefficient(y_pred, y, cm=None):
    """
    Średnia harmoniczna precision i recall. Nadaje się szczególnie zamiast accuracy,
    gdy dane są niezbalansowane.
    Inaczej nazywane F1-Score.
    """
    if cm is None:
        cm = confusion_matrix(y_pred, y)
    TN, FP, FN, TP = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]
    return 2 * TP / (2 * TP + FP + FN)


def pixel_accuracy(y_pred, y_true, cm=None):
    """
    Funkcja mierzy dokładność klasyfikacji pikseli.
    Niestety nie jest to zbyt dobra miara szczególnie kiedy interesujący nas obiekt
    zajmuje małą powierzchnię w porównaniu do całego obrazka.
    Działa w tym wypadku jak accuracy.
    """
    accuracy(y_pred, y_true, cm=cm)


def gini_coefficient(y_pred, y_true):
    auc = roc_auc_score(y_true, y_pred)

    return (auc - 0.5) / 0.5