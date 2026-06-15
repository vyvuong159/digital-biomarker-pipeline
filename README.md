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

## Datasets (synthetic)
**1. Baseline classifier**
- What it is: A collection of participant profiles, including demographics and survey scores. Level: Participant level (one row per person).
- Purpose: Provides the "ground truth" to train models that distinguish between healthy individuals and those with early signs of cognitive impairment.

**2. High-frequency burst testing**
- What it is: Records of repeated cognitive games (like memory tests) performed multiple times a day over short cycles. Level: Session level (one row per game session).
- Purpose: Captures how cognitive performance fluctuates throughout the day, providing a more accurate "real-world" view than a single, one-time test.

**3. Tele-research validation**
- What it is: Results from professional cognitive assessments conducted remotely via video call. Level: Participant level (one row per assessment).
- Purpose: Acts as our "gold standard" or reliable answer key. We compare these expert-verified results against our automated digital signals to prove the system's accuracy.

**4. Passive smartphone telemetry**
- What it is: Automated logs of daily phone interaction habits. Level: Daily/Event level (one row per day or interaction).
- Purpose: Tracks "micro-behaviors" like typing speed and screen usage. These patterns serve as subtle, non-intrusive indicators of how a user’s coordination and engagement levels change over time.

**5. Passive health kit**
- What it is: Continuous data streaming from wearable devices. Level: Daily level (one row per day per person).
- Purpose: Provides lifestyle context, such as sleep quality, heart rate, and step counts. Includes a daily *wear-time* flag. Our cleaning pipeline strictly utilizes this to filter out days where the device was not worn for at least 4 hours, ensuring our analysis is based on genuine behavioral trajectories rather than device inactivity.

## Getting Started
1. Clone the repo: `git clone https://github.com/yourusername/digital-biomarker-pipeline.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the pipeline diagnostics: `pytest tests/`
