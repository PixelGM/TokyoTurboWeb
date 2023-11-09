from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    if request.method == 'POST':
        try:
            T_ambient = float(request.POST.get('ambientTemp', ''))
            T_windshield = float(request.POST.get('windshieldTemp', ''))
            H_ambient = float(request.POST.get('humidity', ''))

            dew_detected = dew_formation_detector(T_ambient, T_windshield, H_ambient)
            dew_message = "Dew formation detected." if dew_detected else "No dew formation detected."

            return JsonResponse({'dew_message': dew_message, 'error': False})
        except ValueError as e:
            # Error Message for 3 valid/invalid variables HERE!, but since we don't need need, we don't print anything
            return JsonResponse({'error_message': "", 'error': True})

    # If not POST request, just render the template
    return render(request, 'dew_detector.html')



def index(request):
     return render(request, 'index.html')

# def hello_world(request):
#     return render(request, 'index.html')
