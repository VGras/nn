import json
#from sklearn.linear_model import LinearRegression

def linear_regression():#(X_train, y_train):
  
  #lr = LinearRegression().fit(X_train, y_train)
  #res = {'coef': lr.coef_.tolist(), 'intercept': lr.intercept_, 'pred': lr.predict(X_train).tolist()}
  #res = {'X-train': X_train, 'y-train': y_train}
  res = {'test': 'test'}
  res['schema'] = "test"
  
  with open("res.json",'w') as f:
        f.write(json.dumps(res)) # Write predictions to file as this will serve as output artifact