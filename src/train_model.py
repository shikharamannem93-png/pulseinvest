from sklearn.ensemble import RandomForestClassifier

def train(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model
