from prophet.serialize import model_to_json, model_from_json
import pandas as pd

# Function to load the saved prophet model
def load_model_and_predict(prediction_date, path="serialized_model.json"):
  with open(path, 'r') as fin:
    loaded_model = model_from_json(fin.read())
    prediction_df = pd.DataFrame({"ds" : [prediction_date]})
  prediction = loaded_model.predict(prediction_df)
  return prediction['yhat'][0].round()