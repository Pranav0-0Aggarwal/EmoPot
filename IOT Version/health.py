def calculate_health(temperature, moisture, sunlight, humidity):
    # Define weight for each parameter (adjust as needed)
    temperature_weight = 1
    moisture_weight = 1
    sunlight_weight = 1
    humidity_weight = 1

    # Define the minimum and maximum values for each parameter (adjust as needed)
    temperature_min = 0
    temperature_max = 100
    moisture_min = 0
    moisture_max = 100
    sunlight_min = 0
    sunlight_max = 100
    humidity_min = 0
    humidity_max = 100

    # Calculate the normalized values between 0 and 100
    temperature_normalized = (temperature - temperature_min) / (temperature_max - temperature_min) * 100
    moisture_normalized = (moisture - moisture_min) / (moisture_max - moisture_min) * 100
    sunlight_normalized = (sunlight - sunlight_min) / (sunlight_max - sunlight_min) * 100
    humidity_normalized = (humidity - humidity_min) / (humidity_max - humidity_min) * 100

    # Calculate the average health score
    health_score = (temperature_normalized * temperature_weight +
                    moisture_normalized * moisture_weight +
                    sunlight_normalized * sunlight_weight +
                    humidity_normalized * humidity_weight) / (temperature_weight + moisture_weight + sunlight_weight + humidity_weight)

    return health_score

