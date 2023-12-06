# Car_accidents_forecast
## Goals


1.   Preprocess and perform EDA of the “Monatszahlen Verkehrsunfälle” Dataset from the [München Open Data Portal](https://www.opengov-muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7). 
2.   [Visualise](https://road-accidents-forecast.streamlit.app/) historically the number of accidents per category.
3. Create an application that [forecasts](https://road-accidents-forecast.streamlit.app/) the values for:
```
Category: 'Alkoholunfälle'
Type: 'insgesamt
Year: '2021'
Month: '01'
```
4. Create an [endpoint](https://road-accidents-forecast.onrender.com/predict) that returns your predictions.
5. Deploy to a [cloud service](https://road-accidents-forecast.streamlit.app/).

## The app
* Api endpoint with prediction is hosted here: [Click this link](https://road-accidents-forecast.onrender.com/predict)
* To test the endpoint [Click this link](https://road-accidents-forecast.onrender.com/docs)
* Web app that contain prediction and visualisation is located here: [Click this link](https://road-accidents-forecast.streamlit.app/)

## Visualisation
![alt text](https://github.com/NuriaAk/Car_accidents_forecast/blob/main/IMG%20Vizualization/Accidents%20per%20Category%20and%20Type.png?raw=true)

![alt text](https://github.com/NuriaAk/Car_accidents_forecast/blob/main/IMG%20Vizualization/Accidents%20per%20Category.png?raw=true)

## Future steps
*   Test the app with users: 
    * The visualisation and usage of the app.


*   Make the model better: 
    * Apply other models (for example LSTM or Boosting methods);
    * Add features using lags or mean number of accidents per month, year;
    * Add other categories to the model / create separate models for other categories. 
*   Make the code better:
    * Create separate modules for backend, frontend;
    * Add documentation;
    * Create a pipeline for data processing, training, validation and prediction;
    * Add more endpoints;
    * Connect with a database that can be updated.
  
## Libraries used
### Visualisation
* matplotlib
* seaborn
### Data preprocessing and modeling
* pandas
* sklearn
* etna
* prophet
### Backend
* fastapi
* requests
* uvicorn
* pydantic
### Frontend
* pillow
* streamlit
### Testing
* pytest

