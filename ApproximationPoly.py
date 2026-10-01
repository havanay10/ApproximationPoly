import math

def f(x):
    return math.sqrt(1 + 2*x)

x0 = 0

# Dérivées en x0 = 0 pour f(x) = (1+2x)^(1/2)
# f(0) = 1
# f'(x) = (1+2x)^(-1/2), f'(0) = 1
# f''(x) = -(1+2x)^(-3/2), f''(0) = -1
# f'''(x) = 3*(1+2x)^(-5/2), f'''(0) = 3
# f''''(x) = -15*(1+2x)^(-7/2), f''''(0) = -15

derivatives = [1, 1, -1, 3, -15]  # f(0), f'(0), f''(0), f'''(0), f''''(0)

print("\nDérivées en x₀ = 0:")
print("-" * 50)
print(f"f(0)  = {derivatives[0]}")
print(f"f'(0) = {derivatives[1]}")
print(f"f''(0) = {derivatives[2]}")
print(f"f'''(0) = {derivatives[3]}")

# QUESTION 1: Polynôme de Taylor de degré 3

print("\n")
print("QUESTION 1: Polynôme de Taylor de degré 3")
print("\n")


# P₃(x) = f(0) + f'(0)x + f''(0)x²/2! + f'''(0)x³/3!
P3 = lambda x: derivatives[0] + derivatives[1]*x + (derivatives[2]/2)*x**2 + (derivatives[3]/6)*x**3

print(f"\nFormule générale: P₃(x) = f(0) + f'(0)·x + f''(0)·x²/2! + f'''(0)·x³/3")
print(f"\nP₃(x) = {derivatives[0]} + {derivatives[1]}·x + ({derivatives[2]}/2)·x² + ({derivatives[3]}/6)·x³")
print(f"P₃(x) = 1 + x - (1/2)x² + (1/2)x³")

# QUESTION 2
print("\n")
print("QUESTION 2: Approximation de √1.2 avec P₃")
print("\n")

# Pour √1.2, on cherche x tel que 1 + 2x = 1.2 => x = 0.1
x_approx = 0.1
valeur_exacte = f(x_approx)  # √1.2
valeur_approx_P3 = P3(x_approx)

print(f"\nPour √1.2: 1 + 2x = 1.2 => x = {x_approx}")
print(f"\nValeur exacte de √1.2 = {valeur_exacte:.15f}")
print(f"Approximation P₃({x_approx}) = {valeur_approx_P3:.15f}")
print(f"\nErreur = |{valeur_exacte:.15f} - {valeur_approx_P3:.15f}|")
print(f"Erreur = {abs(valeur_exacte - valeur_approx_P3):.15f}")

# QUESTION 3: Approximation de l'intégrale avec P₃
print("\n")
print("QUESTION 3: Approximation de l'intégrale ∫₀⁰·¹ √(1+2x) dx avec P₃")
print("\n")

# Intégrale exacte: ∫₀⁰·¹ (1+2x)^(1/2) dx
# Formule: ∫ (1+2x)^(1/2) dx = (1/3)(1+2x)^(3/2)
def integrale_exacte(a, b):
    return (1/3) * ((1 + 2*b)**(3/2) - (1 + 2*a)**(3/2))

valeur_integrale_exacte = integrale_exacte(0, 0.1)

# Approximation avec P₃: ∫₀⁰·¹ P₃(x) dx
# P₃(x) = 1 + x - (1/2)x² + (1/2)x³
# ∫ P₃(x) dx = x + x²/2 - x³/6 + x⁴/8
def integrale_P3(a, b):
    return (b + b**2/2 - b**3/6 + b**4/8) - (a + a**2/2 - a**3/6 + a**4/8)

valeur_integrale_approx = integrale_P3(0, 0.1)

print(f"\nIntégrale exacte: ∫₀⁰·¹ √(1+2x) dx = {valeur_integrale_exacte:.15f}")
print(f"Approximation avec P₃: ∫₀⁰·¹ P₃(x) dx = {valeur_integrale_approx:.15f}")
print(f"\nErreur d'intégration = |{valeur_integrale_exacte:.15f} - {valeur_integrale_approx:.15f}|")
print(f"Erreur = {abs(valeur_integrale_exacte - valeur_integrale_approx):.15f}")

# Comparaison des erreurs
print("\n")
print("Comparaison des erreurs entre la Question 2 et la Question 3")
print("\n")

erreur_Q2 = abs(valeur_exacte - valeur_approx_P3)
erreur_Q3 = abs(valeur_integrale_exacte - valeur_integrale_approx)

print(f"\nErreur de la Question 2 (approximation de √1.2): {erreur_Q2:.15f}")
print(f"Erreur de la Question 3 (approximation de l'intégrale): {erreur_Q3:.15f}")
print(f"\nRapport erreur_Q2 / erreur_Q3 = {erreur_Q2/erreur_Q3:.4f}")

# ALGORITHME DE TAYLOR À DEGRÉ SUPÉRIEUR
print("\n")
print("ALGORITHME DE LA MÉTHODE DE TAYLOR À DEGRÉ SUPÉRIEUR")
print("\n")

print("\nApproximations de √1.2 pour différents degrés:")
print("-" * 60)
print(f"{'Degré':<8} {'Polynôme de Taylor':<45} {'Approximation':<20} {'Erreur':<20}")
print("-" * 110)

for n in range(1, 5):
    # Construction du polynôme de Taylor de degré n
    approx = 0
    polynome = "P" + str(n) + "(x) = "
    termes = []
    
    for i in range(n + 1):
        coeff = derivatives[i] / math.factorial(i)
        term = coeff * (x_approx)**i
        approx += term
        
        # Construction de l'affichage du polynôme
        if i == 0:
            termes.append(f"{derivatives[i]}")
        elif coeff >= 0:
            if i == 1:
                termes.append(f"+ {coeff:.0f}·x")
            else:
                termes.append(f"+ {coeff:.2f}·x^{i}")
        else:
            if i == 1:
                termes.append(f"- {abs(coeff):.0f}·x")
            else:
                termes.append(f"- {abs(coeff):.2f}·x^{i}")
    
    error = abs(valeur_exacte - approx)
    print(f"{n:<8} {' '.join(termes):<45} {approx:<20.15f} {error:<20.15f}")

# ALGORITHME POUR L'INTÉGRALE À DEGRÉ SUPÉRIEUR
print("\n")
print("ALGORITHME DE TAYLOR POUR L'INTÉGRALE À DEGRÉ SUPÉRIEUR")
print("\n")

print("\nApproximations de ∫₀⁰·¹ √(1+2x) dx pour différents degrés:")
print("-" * 80)
print(f"{'Degré':<8} {'Polynôme intégré':<50} {'Approximation':<20} {'Erreur':<20}")
print("-" * 120)

for n in range(1, 5):
    # Construction du polynôme de Taylor de degré n pour l'intégrale
    integral_approx = 0
    termes_integral = []
    
    for i in range(n + 1):
        coeff = derivatives[i] / math.factorial(i)
        # Intégrale de x^i de 0 à 0.1
        integral_term = coeff * (0.1**(i+1)) / (i + 1)
        integral_approx += integral_term
        
        # Construction de l'affichage du polynôme intégré
        if i == 0:
            termes_integral.append(f"{derivatives[i]}·x")
        elif coeff >= 0:
            termes_integral.append(f"+ {coeff:.2f}·x^{i+1}/{i+1}")
        else:
            termes_integral.append(f"- {abs(coeff):.2f}·x^{i+1}/{i+1}")
    
    error_integral = abs(valeur_integrale_exacte - integral_approx)
    print(f"{n:<8} {' '.join(termes_integral):<50} {integral_approx:<20.15f} {error_integral:<20.15f}")

# TABLEAU RÉCAPITULATIF
print("\n")
print("TABLEAU RÉCAPITULATIF DES RÉSULTATS")
print("\n")

print("\n1) Approximation de √1.2:")
print("-" * 70)
print(f"{'Degré':<10} {'Approximation':<25} {'Erreur absolue':<25} {'Erreur':<20}")
print("-" * 80)
for n in range(1, 5):
    approx = 0
    for i in range(n + 1):
        coeff = derivatives[i] / math.factorial(i)
        approx += coeff * (x_approx)**i
    error = abs(valeur_exacte - approx)
    rel_error = error / abs(valeur_exacte) * 100
    print(f"{n:<10} {approx:<25.15f} {error:<25.15f} {rel_error:<20.6f}")

print("\n2) Approximation de l'intégrale ∫₀⁰·¹ √(1+2x) dx:")
print("-" * 70)
print(f"{'Degré':<10} {'Approximation':<25} {'Erreur absolue':<25} {'Erreur relative (%)':<20}")
print("-" * 80)
for n in range(1, 5):
    integral_approx = 0
    for i in range(n + 1):
        coeff = derivatives[i] / math.factorial(i)
        integral_approx += coeff * (0.1**(i+1)) / (i + 1)
    error_integral = abs(valeur_integrale_exacte - integral_approx)
    rel_error = error_integral / abs(valeur_integrale_exacte) * 100
    print(f"{n:<10} {integral_approx:<25.15f} {error_integral:<25.15f} {rel_error:<20.6f}")
