# California House Price Prediction

A machine learning project that predicts median house values in California using various housing district features. The project includes data exploration, feature engineering, model training, and an interactive web interface built with Gradio.

## 🎯 Project Overview

This project uses the California housing dataset to build a machine learning model that can predict the median house value of any housing district in California. The model takes into account various features such as location, house characteristics, and socioeconomic factors to make accurate predictions.

## 📊 Dataset

The project uses the California housing dataset with the following features:

- **longitude**: Longitude coordinate of the housing district
- **latitude**: Latitude coordinate of the housing district  
- **housing_median_age**: Median age of houses in the district (in years)
- **total_rooms**: Total number of rooms in the district
- **total_bedrooms**: Total number of bedrooms in the district
- **population**: Population of the district
- **households**: Number of households in the district
- **median_income**: Median income of households in the district (in tens of thousands USD)
- **ocean_proximity**: Categorical variable indicating proximity to ocean
  - `<1H OCEAN`: Less than 1 hour to ocean
  - `INLAND`: Inland location
  - `NEAR OCEAN`: Near ocean
  - `NEAR BAY`: Near bay
  - `ISLAND`: Island location
- **median_house_value**: Target variable - Median house value in the district (in USD)

## 🛠️ Technologies Used

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **scikit-learn**: Machine learning algorithms and preprocessing
- **gradio**: Interactive web interface
- **joblib**: Model serialization
- **Jupyter Notebook**: Development environment

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/nitish-niraj/house-price-prediction.git
cd house-price-prediction
```

2. Install required dependencies:
```bash
pip install pandas numpy matplotlib scikit-learn gradio joblib jupyter
```

Alternatively, install from requirements.txt:
```bash
pip install -r requirements.txt
```

**Note**: The pre-trained model files were created with a specific version of scikit-learn. If you encounter compatibility issues when loading the model files, you may need to retrain the model by running the complete notebook.

## 📈 Model Development Process

### 1. Data Exploration & Visualization
- Analyzed dataset characteristics and distributions
- Created geographical visualizations of housing data
- Identified correlations between features and target variable

### 2. Feature Engineering
- Created new features:
  - `rooms_per_household`: Total rooms divided by households
  - `bedrooms_per_room`: Total bedrooms divided by total rooms  
  - `population_per_household`: Population divided by households

### 3. Data Preprocessing Pipeline
- **Numerical features**: Missing value imputation (median) + Standard scaling
- **Categorical features**: One-hot encoding for ocean proximity

### 4. Model Training & Selection
- Tested multiple algorithms:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor (selected as final model)
- Used GridSearchCV for hyperparameter tuning
- Evaluated models using cross-validation and RMSE

### 5. Model Deployment
- Saved trained model and preprocessing pipeline using joblib
- Created interactive Gradio web interface for predictions

## 🎮 Usage

### Option 1: Run the Complete Pipeline
Open and run the Jupyter notebook to see the entire development process:
```bash
jupyter notebook housepriceprediction.ipynb
```

### Option 2: Use the Pre-trained Model
The repository includes pre-trained models that you can use directly:

```python
import joblib
import pandas as pd

# Load the trained model and preprocessing pipeline
model = joblib.load('house_price_model.joblib')
pipeline = joblib.load('preprocessing_pipeline.joblib')

# Create sample input data
sample_data = pd.DataFrame({
    'longitude': [-122.23],
    'latitude': [37.88],
    'housing_median_age': [41],
    'total_rooms': [880],
    'total_bedrooms': [129],
    'population': [322],
    'households': [126],
    'median_income': [8.3252],
    'ocean_proximity': ['NEAR BAY']
})

# Make prediction
prepared_data = pipeline.transform(sample_data)
prediction = model.predict(prepared_data)
print(f"Predicted house value: ${prediction[0]:,.2f}")
```

### Option 3: Interactive Web Interface
Launch the Gradio interface for interactive predictions by running the last cell of the Jupyter notebook:

1. Open the notebook:
```bash
jupyter notebook housepriceprediction.ipynb
```

2. Navigate to the last cell (Cell 34) and run it to start the Gradio interface
3. The interface will launch in your browser with input fields for all features
4. Enter housing district characteristics and get instant price predictions

**Alternative**: If you want to run just the Gradio interface without the full notebook, make sure the model files exist and use a Python script with the Gradio code from the notebook.

## 📁 File Structure

```
house-price-prediction/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── housepriceprediction.ipynb        # Main Jupyter notebook with complete pipeline
├── housing.csv                       # California housing dataset
├── house_price_model.joblib         # Trained Random Forest model
├── preprocessing_pipeline.joblib    # Data preprocessing pipeline
└── .gradio/                         # Gradio interface files
    └── flagged/                     # User interaction logs
```

## 🎯 Model Performance

The final Random Forest model achieved:
- **Cross-validation RMSE**: ~$50,000 (approximate)
- **Test set RMSE**: Final performance metrics available in the notebook

The model uses the best hyperparameters found through grid search and provides reliable predictions for California house prices.

## 🌟 Features of the Web Interface

The Gradio interface allows users to:
- Input housing district characteristics through an intuitive form
- Get instant predictions for median house values
- Experiment with different feature combinations
- Understand how different factors affect house prices

## 🔄 Future Improvements

- [ ] Add more advanced feature engineering techniques
- [ ] Experiment with ensemble methods and neural networks
- [ ] Include external data sources (crime rates, school ratings, etc.)
- [ ] Add model interpretability features (SHAP values, feature importance plots)
- [ ] Implement real-time data updates
- [ ] Add prediction confidence intervals
- [ ] Create more sophisticated data visualizations in the web interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- California housing dataset from the 1990 California census
- Scikit-learn for machine learning algorithms
- Gradio for the interactive web interface
- The open-source community for the amazing tools and libraries