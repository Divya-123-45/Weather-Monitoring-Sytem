 # Weather Monitoring System

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd weather_monitoring
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the OpenWeatherMap API key in `config.py`.

4. Run the main application:
    ```bash
    python main.py
    ```

5. (Optional) View visualizations for any city by running:
    ```bash
    python -c "import visualizations; visualizations.plot_daily_weather('Mumbai')"
    ```

## Features
- Real-time weather monitoring for major metros in India.
- Daily summaries, including max/min/average temperature.
- Alerts for temperature thresholds.
- Visualizations for weather trends.

