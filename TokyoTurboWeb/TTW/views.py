# TokyoTurboWeb/views.py
from django.shortcuts import render
from django.http import HttpResponse
import math

# Function to calculate the dew point
def calculate_dew_point(T_ambient, H_ambient):
    a = 17.27
    b = 237.7
    alpha = ((a * T_ambient) / (b + T_ambient)) + math.log(H_ambient/100.0)
    T_dew = (b * alpha) / (a - alpha)
    return T_dew

# Function to detect dew formation
def dew_formation_detector(T_ambient, T_windshield, H_ambient):
    T_dew = calculate_dew_point(T_ambient, H_ambient)
    return T_windshield <= T_dew

# View to handle dew point detection
def dew_point_view(request):
    dew_message = ""
    if request.method == 'POST':
        # Get values from POST request
        T_ambient = float(request.POST.get('ambientTemp', 0))
        T_windshield = float(request.POST.get('windshieldTemp', 0))
        H_ambient = float(request.POST.get('humidity', 100))

        # Perform the dew detection
        dew_detected = dew_formation_detector(T_ambient, T_windshield, H_ambient)

        # Set the result message
        dew_message = "Dew formation detected." if dew_detected else "No dew formation detected."

    # Render the HTML template with the dew_message
    return render(request, 'index.html', {'dew_message': dew_message})

# def hello_world(request):
#     return render(request, 'index.html')
