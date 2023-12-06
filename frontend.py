import streamlit as st
from PIL import Image
import requests
import json

# Let's create a streamlit page with prediction and vizualization 
def main():
    # Page configuration
    st.set_page_config(layout="wide", page_title="Car accidents prediction", page_icon=':car:')

    # Title
    st.title("Road accidents prediction and visualisation")

    # Variables that refer to the vizualisation images
    viz_cat_type = Image.open('IMG Vizualization/Accidents per Category and Type.png')
    viz_category = Image.open('IMG Vizualization/Accidents per Category.png')
    
    # Our page is divided in two sections: tab1 for a prediction and tab2 for visualisation
    tab1, tab2 = st.tabs([':eyes: Predict', ':bar_chart: Visualise'])
    
    # Let's create our prediction section
    with tab1:
            endpoint = "https://road-accidents-forecast.onrender.com/predict"
            
            st.write("Which year do choose for prediction? (NB! Only '2021' is available for prediction.)")
            month = st.selectbox("Which month do you choose for prediction?", ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"))
            
                
            execute_button = st.button(label='Predict 🔎')
            if execute_button:
                dic = {"year" : "2021", "month": str(month)}
                dic_json = json.dumps(dic)
                response = requests.post(endpoint, dic_json)

                st.write(f"Predicted number of 'Alkoholunfälle' 'insgesamt' car accidents for {month} month 2021:")
                st.write(response.json())
    
    # Let's create our visualisation section
    with tab2:
        st.write("Our task is to visualise historically the number of accidents per Category.")
        st.write("We have three categories:")
        
        st.write("1) Verkehrsunfälle")
        st.write("2) Fluchtunfälle")
        st.write("3) Alkoholunfälle")

        st.write("And 3 types within each category.")


        st.image(viz_cat_type)
        st.write("Most of the accidents refer to Verkehrsunfälle category and 'insgesamt' type. There is no clear trend.")
        st.divider()

        st.write("### Let's have a look at 'insgesamt' type of each category.")
        st.image(viz_category)
        st.write("Alkoholunfälle has the lowest numbers. It is the segment that we want to predict.")
        st.divider()

        
if __name__ == '__main__':
    main()
