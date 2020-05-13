from sklearn.linear_model import LinearRegression()

def linear_regression(X, y):
  
  lr = LinearRegression(X, y)
  y_pred = lr.predict(X)
  
  with open("res.json",'w') as f:
        f.write(json.dumps(y_pred)) # Write predictions to file as this will serve as output artifact
