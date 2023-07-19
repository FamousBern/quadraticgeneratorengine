from django.shortcuts import render
from django.http import JsonResponse


def quadratic_equation_solver(request):
    if request.method == 'POST':
        a = int(float(request.POST.get('a')))
        b = int(float(request.POST.get('b')))
        c = int(float(request.POST.get('c')))

        equation = f"{a}x^2"
        if b < 0:
            equation += f" - {-b}x"
        elif b > 0:
            equation += f" + {b}x"
        if c < 0:
            equation += f" - {-c}"
        elif c > 0:
            equation += f" + {c}"
        
        equation += " = 0"

        discriminant = b**2 - 4*a*c

        if discriminant < 0:
            response_data = {
                'equation': equation,
                'discriminant': discriminant,
                'roots': None
            }
        else:
            sqrt_discriminant = discriminant**0.5
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
            response_data = {
                'equation': equation,
                'discriminant': discriminant,
                'roots': [round(x1, 4), round(x2, 4)]
            }

        return JsonResponse(response_data)

    return render(request, 'solver.html')
