import json
from sklearn.linear_model import LinearRegression

def run_test(X_train, y_train):
  
  lr = LinearRegression().fit(X_train, y_train)
  res = {}
  res['X_train'] = X_train
  res['y_train'] = y_train
  res['y_pred'] = lr.predict(X_train).tolist()
  res['coef'] = lr.coef_.tolist()
  res['intercept'] = lr.intercept_
  res['schema'] = "test"
  
  with open("results.json",'w') as f:
        f.write(json.dumps(res)) # Write predictions to file as this will serve as output artifact
