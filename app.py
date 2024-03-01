# Import libraries
import pandas as pd 
import streamlit as st 
from sklearn import datasets 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Title of the app
st.write("""
## Iris Flower Prediction App by Maria Nadeem!!
This App Provides the predicted class of the iris Flower""")

# Sidebar for user input parameters
st.sidebar.header('User Input parameters')

# Function to get user input parameters
def user_input_parameters():
    sepal_length = st.sidebar.slider('Sepal Length', 6.0,3.8)
    sepal_width = st.sidebar.slider('Sepal Width', 2.3,4.4)
    petal_length = st.sidebar.slider('Petal Length', 0.6,1.3)
    petal_width = st.sidebar.slider('Petal Width', 1.0,6.9)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input parameters
df = user_input_parameters()

# Display user input parameters
st.subheader('User Input Parameters')
st.write(df)

# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Predictions
predictions = model.predict(df)
predictions_proba = model.predict_proba(df)
predicted_class_name = iris.target_names[predictions]

# Display class names with their corresponding index number
st.subheader('Class names with their corresponding Index Number')
st.write(iris.target_names)

# Display predictions
st.subheader('Predictions')
st.write(predictions_proba[0])

# Display the predicted class
st.subheader('The predicted class is:')
st.write(predicted_class_name[0])

# Feature Importance
st.subheader('Feature Importance')
feature_importance = pd.Series(model.feature_importances_, index=iris.feature_names)
st.bar_chart(feature_importance)
# Add author name and info to the sidebar
st.sidebar.markdown("### Author: Maria Nadeem🎉🎊⚡")
st.sidebar.markdown("### GitHub: [GitHub](https://github.com/marianadeem755)")
st.sidebar.markdown("### LinkedIn: [LinkedIn Account](https://www.linkedin.com/in/maria-nadeem-4994122aa/)")
st.sidebar.markdown("### Contact: [Email](mailto:marianadeem755@gmail.com)")

# Background Image
st.markdown("""
<style>
.stApp {
background: url("https://images.unsplash.com/photo-1605726135442-468dd2b7eff1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcwOTI5MjU4MQ&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080");
background-size: cover;
    }
</style>""", unsafe_allow_html=True)
