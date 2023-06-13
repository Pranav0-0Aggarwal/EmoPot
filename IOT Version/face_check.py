U_T=40
L_T=20
U_M=40
L_M=20
U_S=40
L_S=20
U_H=40
L_H=20


def check(temperature, moisture,sunlight,humidity):
    if(temperature>L_T and temperature<U_T and moisture>L_M and moisture<L_M and sunlight>L_S and sunlight<U_S ):
        return "happy"
    if(temperature>U_T):
        return "hot"
    elif (temperature < L_T):
        return "cold"
    elif (moisture > U_M):
        return "grumpy"
    elif (moisture < L_M):
        return "thirsty"
    elif (sunlight > U_S):
        return "blink"
    elif (sunlight < L_S):
        return "vampire"
    elif (humidity > U_H):
        return "blink"
    elif (humidity < L_H):
        return "grumpy"
    else:
       return "blank"
    

def rain_check(temperature, humidity):
  """
  Checks if it will rain today based on temperature and humidity.

  Args:
    temperature: The current temperature in degrees Fahrenheit.
    humidity: The current humidity in percentage.

  Returns:
    True if it will rain today, False otherwise.
  """

  # Get the dew point temperature.
  dew_point = get_dew_point(temperature, humidity)

  # Check if the dew point is above the temperature.
  if dew_point >= temperature:
    return True
  else:
    return False


def get_dew_point(temperature, humidity):
  """
  Gets the dew point temperature.

  Args:
    temperature: The current temperature in degrees Fahrenheit.
    humidity: The current humidity in percentage.

  Returns:
    The dew point temperature in degrees Fahrenheit.
  """

  # Calculate the dew point temperature.
  dew_point = temperature * (100 - humidity) / 50 + 32

  return dew_point

