import random
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')


def generate_quadratic_equations(request):
    if request.method == 'POST':
        num_equations = int(request.POST.get('num_equations', 1))
        include_roots_discriminant = request.POST.get('include_roots_discriminant', False)

        equations = []

        for _ in range(num_equations):
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)

            equation = f"{a}x^2"
            if b < 0:
                equation += f" - {-b}x"
            else:
                equation += f" + {b}x"
            if c < 0:
                equation += f" - {-c}"
            else:
                equation += f" + {c}"

            if include_roots_discriminant:
                discriminant = b**2 - 4*a*c
                if discriminant < 0:
                    equation_data = {'equation': equation, 'discriminant': discriminant}
                else:
                    sqrt_discriminant = discriminant**0.5
                    x1 = (-b + sqrt_discriminant) / (2*a)
                    x2 = (-b - sqrt_discriminant) / (2*a)
                    equation_data = {
                        'equation': equation,
                        'discriminant': discriminant,
                        'roots': [round(x1, 4), round(x2, 4)]
                    }
            else:
                equation_data = {'equation': equation}

            equations.append(equation_data)

        return JsonResponse({'equations': equations})

    return render(request, 'index.html')
