"""Configuration for Synthetic Biomarker Data Generation"""

# ====================
# Study Design
# ====================
N_TOTAL = 16790
N_MCI = 556
N_CONTROLS = 16234
MCI_RATIO = 3  # 3:1 sampling

# ====================
# Baseline Dataset (CANTAB Cognitive Assessment)
# ====================
BASELINE_N_CANTAB_FEATURES = 176

# Demographics
BASELINE_AGE_MCI = {'loc': 67.1, 'scale': 8.3, 'min': 50, 'max': 86}
BASELINE_AGE_CONTROLS = {'loc': 65.7, 'scale': 6.9, 'min': 50, 'max': 86}

BASELINE_SEX_MCI_FEMALE_RATIO = 0.556
BASELINE_SEX_CONTROLS_FEMALE_RATIO = 0.657

BASELINE_EDU_MCI_LOW_RATIO = 0.431  # < Bachelor's
BASELINE_EDU_CONTROLS_LOW_RATIO = 0.323

# Survey Scores
BASELINE_CFI_MCI = {'loc': 6.8, 'scale': 3.9, 'min': 0, 'max': 14}
BASELINE_CFI_CONTROLS = {'loc': 1.2, 'scale': 1.1, 'min': 0, 'max': 14}

BASELINE_ECOG_MCI = {'loc': 2.02, 'scale': 0.68, 'min': 1.0, 'max': 4.0}
BASELINE_ECOG_CONTROLS = {'loc': 1.25, 'scale': 0.25, 'min': 1.0, 'max': 4.0}

BASELINE_CFI_ITEM_NOISE = 0.2
BASELINE_ECOG_ITEM_NOISE = 0.3

# CANTAB Task Scores
BASELINE_PAL_ERRORS_MCI = {'loc': 45.0, 'scale': 15.0, 'min': 0, 'max': 150}
BASELINE_PAL_ERRORS_CONTROLS = {'loc': 22.0, 'scale': 10.0, 'min': 0, 'max': 150}

BASELINE_SWM_ERRORS_MCI = {'loc': 48.1, 'scale': 17.6, 'min': 0, 'max': 100}
BASELINE_SWM_ERRORS_CONTROLS = {'loc': 41.3, 'scale': 18.8, 'min': 0, 'max': 100}

BASELINE_PRM_CORRECT_MCI = {'loc': 66.7, 'scale': 17.1, 'min': 0, 'max': 100}
BASELINE_PRM_CORRECT_CONTROLS = {'loc': 79.8, 'scale': 13.7, 'min': 0, 'max': 100}

BASELINE_MTS_TIME_MCI = {'loc': 5.45, 'scale': 4.16, 'min': 0.1, 'max': 20.0}
BASELINE_MTS_TIME_CONTROLS = {'loc': 4.55, 'scale': 1.36, 'min': 0.1, 'max': 20.0}

BASELINE_PADDING_NOISE_MEAN = 0.0
BASELINE_PADDING_NOISE_STD = 1.0

# ====================
# CAM-COG Burst Dataset (N-Back & DSST)
# ====================
CAMCOG_N_DAYS = 14
CAMCOG_SESSIONS_PER_DAY = 3
CAMCOG_MISSINGNESS_RATE = 0.18  # 18% missing compliance

CAMCOG_DSST_MCI = {'loc': 26.9, 'scale': 6.0}
CAMCOG_DSST_CONTROLS = {'loc': 32.8, 'scale': 7.0}
CAMCOG_DSST_NOISE = 2.5
CAMCOG_DSST_DAY_IMPROVEMENT = 0.15

CAMCOG_NBACK_MCI = {'loc': 1.40, 'scale': 0.5}
CAMCOG_NBACK_CONTROLS = {'loc': 1.84, 'scale': 0.5}
CAMCOG_NBACK_NOISE = 0.2
CAMCOG_NBACK_DAY_IMPROVEMENT = 0.01

CAMCOG_DISTRACTION_RATE_MCI = 0.11
CAMCOG_DISTRACTION_RATE_CONTROLS = 0.16

# ====================
# Telehealth MoCA Validation Dataset
# ====================
TELEMOCA_N_VALIDATION = 1015
TELEMOCA_MCI_OVERSAMPLING_RATIO = 0.60

TELEMOCA_TOTAL_MCI = {'loc': 22.1, 'scale': 2.8, 'min': 0, 'max': 30}
TELEMOCA_TOTAL_CONTROLS = {'loc': 27.4, 'scale': 1.9, 'min': 0, 'max': 30}

TELEMOCA_DELAYED_RECALL_MCI = {'loc': 1.5, 'scale': 1.1, 'min': 0, 'max': 5}
TELEMOCA_DELAYED_RECALL_CONTROLS = {'loc': 4.1, 'scale': 0.9, 'min': 0, 'max': 5}

TELEMOCA_ATTENTION_MCI = {'loc': 4.2, 'scale': 1.1, 'min': 0, 'max': 6}
TELEMOCA_ATTENTION_CONTROLS = {'loc': 5.5, 'scale': 0.7, 'min': 0, 'max': 6}

TELEMOCA_EXECUTIVE_MCI = {'loc': 3.1, 'scale': 1.0, 'min': 0, 'max': 5}
TELEMOCA_EXECUTIVE_CONTROLS = {'loc': 4.4, 'scale': 0.8, 'min': 0, 'max': 5}

TELEMOCA_ORIENTATION_FRACTION = 0.4
TELEMOCA_MIS_MULTIPLIER = 3
TELEMOCA_MIS_NOISE_MCI = [0, 1, 2]
TELEMOCA_MIS_NOISE_CONTROLS = [2, 3]
TELEMOCA_TECHNICAL_VALIDITY_RATE = 0.978

# ====================
# Sensor Kit Dataset (Keyboard & Device Interaction)
# ====================
SENSORKIT_N_WEEKS = 4

SENSORKIT_TAPS_MCI = {'loc': 140.0, 'scale': 25.0}
SENSORKIT_TAPS_CONTROLS = {'loc': 175.0, 'scale': 20.0}
SENSORKIT_TAPS_NOISE = 8.0

SENSORKIT_HOLD_TIME_MCI = {'loc': 95.0, 'scale': 12.0}
SENSORKIT_HOLD_TIME_CONTROLS = {'loc': 80.0, 'scale': 8.0}
SENSORKIT_HOLD_TIME_NOISE = 3.0

SENSORKIT_FLIGHT_TIME_MCI = {'loc': 260.0, 'scale': 45.0}
SENSORKIT_FLIGHT_TIME_CONTROLS = {'loc': 210.0, 'scale': 30.0}
SENSORKIT_FLIGHT_TIME_NOISE = 15.0

SENSORKIT_UNLOCKS_MCI = {'loc': 42.0, 'scale': 10.0}
SENSORKIT_UNLOCKS_CONTROLS = {'loc': 55.0, 'scale': 12.0}
SENSORKIT_UNLOCKS_NOISE = 4.0

SENSORKIT_MSG_MULTIPLIER = 0.4
SENSORKIT_MSG_BASE_NOISE_MCI = 8.0
SENSORKIT_MSG_BASE_NOISE_CONTROLS = 12.0
SENSORKIT_MSG_BASE = 15

SENSORKIT_LOCATIONS_LAMBDA_MCI = 12
SENSORKIT_LOCATIONS_LAMBDA_CONTROLS = 18

# ====================
# Health Kit Dataset (Smartwatch Biometrics)
# ====================
HEALTHKIT_N_DAYS = 14
HEALTHKIT_WEAR_TIME_THRESHOLD = 12.0  # Hours

HEALTHKIT_STEPS_MCI = {'loc': 4500, 'scale': 1200}
HEALTHKIT_STEPS_CONTROLS = {'loc': 6800, 'scale': 1800}
HEALTHKIT_STEPS_NOISE = 600
HEALTHKIT_STEPS_MIN = 100
HEALTHKIT_STEPS_MAX = 22000

HEALTHKIT_HRV_MCI = {'loc': 28.0, 'scale': 8.0}
HEALTHKIT_HRV_CONTROLS = {'loc': 42.0, 'scale': 12.0}
HEALTHKIT_HRV_NOISE = 4.0
HEALTHKIT_HRV_MIN = 5.0
HEALTHKIT_HRV_MAX = 150.0

HEALTHKIT_DEEP_SLEEP_MCI = {'loc': 45.0, 'scale': 15.0}
HEALTHKIT_DEEP_SLEEP_CONTROLS = {'loc': 65.0, 'scale': 18.0}
HEALTHKIT_DEEP_SLEEP_NOISE = 8.0

HEALTHKIT_WEAR_TIME_MCI = {'loc': 12.5, 'scale': 4.5}
HEALTHKIT_WEAR_TIME_CONTROLS = {'loc': 16.0, 'scale': 3.0}
HEALTHKIT_WEAR_TIME_NOISE = 1.5

HEALTHKIT_SLEEP_COLLECTION_RATE = 0.85  # 15% missingness if wear < 12h
HEALTHKIT_REM_MULTIPLIER = 1.2
HEALTHKIT_REM_NOISE = 10.0
HEALTHKIT_CORE_BASE = 240
HEALTHKIT_CORE_NOISE = 45.0

HEALTHKIT_HR_MCI = {'loc': 72.0, 'scale': 6.0}
HEALTHKIT_HR_CONTROLS = {'loc': 72.0, 'scale': 5.0}
HEALTHKIT_HR_MIN = 50
HEALTHKIT_HR_MAX = 110