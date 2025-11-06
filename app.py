"""
Gradio app for House Price Prediction Model
Deploy this to Hugging Face Spaces for interactive inference
"""
import gradio as gr  # type: ignore
import joblib  # type: ignore
import pandas as pd
from huggingface_hub import hf_hub_download  # type: ignore
from typing import Any

print("🔄 Downloading model files...")

# Download model files
try:
    model_path: str = hf_hub_download(  # type: ignore
        repo_id="niru-nny/house-price-prediction",
        filename="house_price_model.joblib"
    )
    print(f"✅ Model downloaded: {model_path}")
    
    pipeline_path: str = hf_hub_download(  # type: ignore
        repo_id="niru-nny/house-price-prediction",
        filename="preprocessing_pipeline.joblib"
    )
    print(f"✅ Pipeline downloaded: {pipeline_path}")
    
    # Load model and pipeline
    print("🔄 Loading model and pipeline...")
    model: Any = joblib.load(model_path)  # type: ignore
    pipeline: Any = joblib.load(pipeline_path)  # type: ignore
    print("✅ Model and pipeline loaded successfully!")
    
except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise

def predict_price(
    longitude: float, 
    latitude: float, 
    housing_median_age: int,
    total_rooms: int,
    total_bedrooms: int, 
    population: int, 
    households: int, 
    median_income: float,
    ocean_proximity: str
) -> str:
    """Predict house price based on input features"""
    
    # Create input dataframe
    input_data = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]
    })
    
    # Preprocess and predict
    processed_data: Any = pipeline.transform(input_data)  # type: ignore
    prediction: float = model.predict(processed_data)[0]  # type: ignore
    
    return f"${prediction:,.2f}"

# Create Gradio interface
demo: Any = gr.Interface(  # type: ignore
    fn=predict_price,
    inputs=[
        gr.Slider(-124.5, -114.0, value=-122.23, label="Longitude"),
        gr.Slider(32.5, 42.0, value=37.88, label="Latitude"),
        gr.Slider(0, 52, value=41, step=1, label="Housing Median Age"),
        gr.Slider(0, 40000, value=880, step=10, label="Total Rooms"),
        gr.Slider(0, 6500, value=129, step=1, label="Total Bedrooms"),
        gr.Slider(0, 35000, value=322, step=1, label="Population"),
        gr.Slider(0, 6000, value=126, step=1, label="Households"),
        gr.Slider(0, 15, value=8.3252, step=0.1, label="Median Income (in $10,000s)"),
        gr.Dropdown(
            choices=["NEAR BAY", "INLAND", "<1H OCEAN", "NEAR OCEAN", "ISLAND"],
            value="NEAR BAY",
            label="Ocean Proximity"
        )
    ],
    outputs=gr.Textbox(label="Predicted House Price"),
    title="🏠 California House Price Prediction",
    description="Predict California house prices based on location and features",
    examples=[
        [-122.23, 37.88, 41, 880, 129, 322, 126, 8.3252, "NEAR BAY"],
        [-121.22, 39.43, 7, 1430, 244, 515, 226, 3.8462, "INLAND"],
    ]
)

if __name__ == "__main__":
    demo.launch()
