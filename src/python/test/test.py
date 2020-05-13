from sklearn.linear_model import LinearRegression

def linear_regression(X_train, y_train):
  
  lr = LinearRegression().fit(X_train, y_train)
  y_pred = lr.predict(X_train)
  
  with open("res.json",'w') as f:
        f.write(json.dumps(y_pred)) # Write predictions to file as this will serve as output artifact
