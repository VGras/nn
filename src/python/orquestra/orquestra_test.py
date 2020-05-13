import json

def run_test(var_1, var_2):
  
  res = {'var_1': var_1, 'var_2': var_2}
  res['schema'] = "test"
  
  with open("results.json",'w') as f:
        f.write(json.dumps(res)) # Write predictions to file as this will serve as output artifact
