---
title: California House Price Prediction
emoji: 🏠
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# California House Price Prediction 🏠

Interactive demo for predicting California house prices using a Random Forest model.

## How to Use

1. Adjust the sliders to set house features:
   - **Location**: Longitude and Latitude
   - **Age**: Housing median age
   - **Size**: Total rooms, bedrooms, population, households
   - **Income**: Median income in the area
   - **Proximity**: Distance to ocean

2. Click **Submit** to get the predicted house price

## Model

This app uses the [house-price-prediction](https://huggingface.co/niru-nny/house-price-prediction) model trained on California Housing dataset.

**Features:**
- Random Forest Regressor (scikit-learn)
- RMSE: ~$47,000-49,000
- Trained on 20,640 California districts

## Examples

Try these sample inputs:
- **Bay Area House**: High median income, near bay location
- **Inland House**: Lower median income, inland location
