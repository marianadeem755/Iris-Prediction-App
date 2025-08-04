# Iris Flower Prediction App 🌸
This app predicts the class of an Iris flower based on user-provided input parameters such as sepal length, sepal width, petal length, and petal width. It uses a **Random Forest Classifier** to make predictions and provides probabilities for each class.

## Features ✨

- **Interactive User Input**: Use sliders in the sidebar to input flower measurements.
- **Real-Time Predictions**: Get predictions for the Iris flower class instantly.
- **Class Probabilities**: View the probability distribution for each class.
- **Feature Importance**: Visualize the importance of each feature in the prediction model.
- **Clean and Intuitive UI**: Includes a background image and an intuitive layout.

## How to Use the App 🛠️

1. **Run the App**:
   - Install the required libraries using the following command:
     ```bash
     pip install streamlit pandas scikit-learn matplotlib
     ```
   - Save the Python script (`iris_app.py`) in your working directory.
   - Run the app using the command:
     ```bash
     streamlit run iris_app.py
     ```

2. **Input Parameters**:
   - Use the sliders in the sidebar to adjust the following parameters:
     - Sepal Length
     - Sepal Width
     - Petal Length
     - Petal Width

3. **View Predictions**:
   - The app will display:
     - The predicted class of the Iris flower.
     - The probability distribution for each class.
     - A bar chart showing the feature importance.

4. **Explore the Dataset**:
   - The app provides the class names and their corresponding index numbers for better understanding.

## App Preview 📸

### Sidebar
- Input parameters using sliders.
- Author information and contact links.

### Main Page
- Displays user input parameters.
- Shows predictions and probabilities.
- Visualizes feature importance with a bar chart.

## Technologies Used 🖥️

- **Python**: Programming language.
- **Streamlit**: Framework for building interactive web apps.
- **Scikit-learn**: Machine learning library for training the Random Forest model.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Visualization library for feature importance.

## Future Enhancements 🚀

- Add more machine learning models for comparison.
- Include additional visualizations for better insights.

## 📄 🌟 Acknowledgments
- Built with [Streamlit](https://streamlit.io/).
Enjoy using the **Iris Flower Prediction App**! 🌼
