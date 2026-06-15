# Digital Biomarker Pipeline: Mild Cognitive Impairment (MCI) Detection

## Project Overview
This repository contains a modular, end-to-end data processing pipeline designed to transform raw passive sensor telemetry and active cognitive assessment data into actionable digital health insights. The project focuses on detecting signals related to Mild Cognitive Impairment (MCI) through the analysis of longitudinal sensor data.

### Key Objectives
* **Data integrity:** Implementing robust cleaning pipelines for noisy, multi-source longitudinal health data
* **Signal reliability:** Distinguishing true behavioral patterns from device-related data gaps (synchronization delays, non-wear time)
* **Clinical insight:** Translating passive behavioral telemetry into meaningful constructs that assist in longitudinal health monitoring



## Project Structure
- `data/`: Sample synthetic datasets used for pipeline testing
- `src/`: Reusable Python modules for data cleaning, feature engineering, and signal diagnostic logic
- `notebooks/`: Exploratory Data Analysis (EDA) and clinical validation experiments
- `tests/`: Basic unit tests for critical signal-processing functions
- `docs/`: Methodological documentation and rationale behind health-metric design

## Technical Highlights
* **Longitudinal modeling:** The pipeline is built to handle repeated-measures data, accounting for temporal variability in user engagement
* **Engineering logic:** Cleaning strategies are informed by the engineering constraints of the sensors (e.g., handling backfilled cache data vs. true non-use)
* **Modularity:** Designed for maintainability, with clear separation between raw data processing and feature engineering

## Data Stewardship & Ethics
*Note: The datasets contained in this repository are synthetic and created for demonstration purposes only. They do not contain any Protected Health Information (PHI) or real-world user data.*

## Getting Started
1. Clone the repo: `git clone https://github.com/yourusername/digital-biomarker-pipeline.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the pipeline diagnostics: `pytest tests/`
