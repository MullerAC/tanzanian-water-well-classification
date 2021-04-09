from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score

def get_metrics(y_test, X_test, model):
    labels = y_test.to_numpy()
    preds = model.predict(X_test)
    
    metrics = {}
    metrics['accuracy'] = accuracy_score(labels, preds)
    metrics['f1'] = f1_score(labels, preds, average='weighted')
    metrics['precision'] = precision_score(labels, preds, average='weighted')
    metrics['recall'] = recall_score(labels, preds, average='weighted')
    
    return metrics