# TokyoTurboWeb/views.py
from django.http import HttpResponse
from django.shortcuts import render
import math

def calculate_dew_point(T_ambient, H_ambient):
    a = 17.27
    b = 237.7
    alpha = ((a * T_ambient) / (b + T_ambient)) + math.log(H_ambient/100.0)
    T_dew = (b * alpha) / (a - alpha)
    return T_dew

def dew_formation_detector(T_ambient, T_windshield, H_ambient):
    T_dew = calculate_dew_point(T_ambient, H_ambient)
    return T_windshield <= T_dew

def dew_point_view(request):
    # Inputs
    T_ambient = 10.0      # Ambient temperature in degrees Celsius
    T_windshield = 8.0    # Windshield temperature in degrees Celsius
    H_ambient = 85.0      # Ambient humidity in percent

    # Perform the dew detection
    dew_detected = dew_formation_detector(T_ambient, T_windshield, H_ambient)

    # Prepare the message
    dew_message = "Dew formation detected." if dew_detected else "No dew formation detected."

    # Render the index.html template with the dew_message context
    return render(request, 'index.html', {'dew_message': dew_message})


# def hello_world(request):
#     return render(request, 'index.html')
