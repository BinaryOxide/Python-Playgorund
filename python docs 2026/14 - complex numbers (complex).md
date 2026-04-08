# 14 - Complex Numbers (complex) in Python

## What are Complex Numbers?
Complex numbers are numbers of the form **a + bj**, where:
- **a** is the real part
- **b** is the imaginary part
- **j** (or **J**) represents the imaginary unit (√-1)

Python has built-in support for complex numbers using `j` or `J` as the imaginary unit.

## Basic Complex Number Declaration

```python
# Different ways to create complex numbers
z1 = 3 + 4j        # Real: 3, Imag: 4
z2 = 5 - 2j        # Real: 5, Imag: -2
z3 = -2 + 3j       # Negative real, positive imaginary
z4 = 0 + 5j        # Pure imaginary (no real part)
z5 = 7 + 0j        # Pure real (no imaginary part)
z6 = 1j            # Same as 0 + 1j

# Using complex() constructor
z7 = complex(3, 4)     # 3 + 4j
z8 = complex(5)        # 5 + 0j (real only)
z9 = complex(0, -2)    # -2j

print(z1, type(z1))    # (3+4j) <class 'complex'>
print(z7)              # (3+4j)
```

## Accessing Real and Imaginary Parts

```python
z = 3 + 4j

# Real part (float)
real_part = z.real
print(f"Real: {real_part}")      # 3.0

# Imaginary part (float)
imag_part = z.imag
print(f"Imaginary: {imag_part}") # 4.0

# Conjugate (a - bj)
conjugate = z.conjugate()
print(f"Conjugate: {conjugate}") # (3-4j)

# Check if number is real (imaginary part is zero)
print(z.real == 0)               # False
print((5+0j).imag == 0)          # True
```

## Complex Number Operations

### Arithmetic Operations
```python
a = 2 + 3j
b = 1 - 2j

# Addition
print(f"{a} + {b} = {a + b}")    # (3+1j)

# Subtraction
print(f"{a} - {b} = {a - b}")    # (1+5j)

# Multiplication
print(f"{a} * {b} = {a * b}")    # (8-1j)

# Division
print(f"{a} / {b} = {a / b}")    # (-0.8+1.4j)

# Exponentiation
print(f"{a} ** 2 = {a ** 2}")    # (-5+12j)

# Negation
print(f"-{a} = {-a}")            # (-2-3j)
```

### Comparison Operations
```python
# Complex numbers can only be compared for equality
z1 = 3 + 4j
z2 = 3 + 4j
z3 = 4 + 3j

print(z1 == z2)      # True
print(z1 == z3)      # False
print(z1 != z3)      # True

# Cannot compare with <, >, <=, >=
# print(z1 > z2)     # TypeError!
# print(z1 < z3)     # TypeError!

# Compare magnitudes instead
def magnitude(z):
    return abs(z)

print(magnitude(z1) < magnitude(z3))  # True (5.0 < 5.0? Actually equal)
print(abs(z1) < abs(z3))              # False (5.0 < 5.0 is False)
```

## Mathematical Functions for Complex Numbers

### Basic Functions (cmath module)
```python
import cmath
import math

z = 3 + 4j

# Absolute value (magnitude)
print(f"|{z}| = {abs(z)}")           # 5.0
print(f"|{z}| = {cmath.phase(z)}")   # 0.9272952180016122 (phase angle)

# Square root
print(f"√{z} = {cmath.sqrt(z)}")      # (2+1j)

# Exponential
print(f"e^{z} = {cmath.exp(z)}")      # (-13.128783081462158-15.200784463067954j)

# Logarithms
print(f"ln({z}) = {cmath.log(z)}")    # (1.6094379124341003+0.9272952180016122j)
print(f"log10({z}) = {cmath.log10(z)}") # (0.69897+0.402719j)

# Trigonometric functions
print(f"sin({z}) = {cmath.sin(z)}")   # (3.853738037919377-6.054423963686047j)
print(f"cos({z}) = {cmath.cos(z)}")   # (-27.034945603074224-3.8511533348117775j)
print(f"tan({z}) = {cmath.tan(z)}")   # (-0.0001873462046294524+0.999355987381473j)

# Inverse trigonometric functions
print(f"asin({z}) = {cmath.asin(z)}") # (0.6339838656391766+2.305509031243477j)
print(f"acos({z}) = {cmath.acos(z)}") # (0.9368124611557199-2.305509031243477j)
print(f"atan({z}) = {cmath.atan(z)}") # (1.4483069952314644+0.15899719167999918j)

# Hyperbolic functions
print(f"sinh({z}) = {cmath.sinh(z)}") # (-6.5481200409110025-7.61923172032141j)
print(f"cosh({z}) = {cmath.cosh(z)}") # (-6.580663040551157-7.581552742746543j)
print(f"tanh({z}) = {cmath.tanh(z)}") # (1.000709536067231+0.00490825806749606j)
```

### Converting Between Forms

```python
import cmath
import math

# Rectangular (a + bj) to Polar (r, θ)
z = 3 + 4j
r = abs(z)                    # Magnitude: 5.0
theta = cmath.phase(z)        # Phase angle: 0.9272952180016122 rad

print(f"Rectangular: {z}")
print(f"Polar: r={r}, θ={theta} rad")
print(f"Polar: r={r}, θ={math.degrees(theta)}°")

# Polar to Rectangular
r = 5.0
theta = 0.9272952180016122
x = r * math.cos(theta)       # Real part: 3.0
y = r * math.sin(theta)       # Imaginary part: 4.0
z_rect = complex(x, y)

print(f"Polar: r={r}, θ={theta} rad")
print(f"Rectangular: {z_rect}")

# Using cmath.rect() (direct conversion)
z_rect2 = cmath.rect(r, theta)
print(f"cmath.rect(): {z_rect2}")
```

## Complex Number Properties

```python
import cmath

z = 3 + 4j

# Magnitude (modulus)
magnitude = abs(z)
print(f"|z| = {magnitude}")           # 5.0

# Phase (argument)
phase = cmath.phase(z)
print(f"arg(z) = {phase} rad")        # 0.9272952180016122
print(f"arg(z) = {phase * 180 / cmath.pi}°")  # 53.13010235415598°

# Complex conjugate
conj = z.conjugate()
print(f"z̄ = {conj}")                  # (3-4j)

# Properties of conjugates
print(f"z * z̄ = {z * conj}")          # (25+0j) (magnitude squared)
print(f"|z|² = {abs(z)**2}")          # 25.0

# Real and imaginary parts
print(f"Re(z) = {z.real}")            # 3.0
print(f"Im(z) = {z.imag}")            # 4.0

# Euler's formula: e^(iθ) = cos(θ) + i·sin(θ)
theta = cmath.pi / 3  # 60 degrees
euler = cmath.exp(1j * theta)
print(f"e^(i·π/3) = {euler}")         # (0.5+0.8660254037844386j)
print(f"cos(π/3) = {math.cos(theta)}") # 0.5
print(f"sin(π/3) = {math.sin(theta)}") # 0.8660254037844386
```

## Practical Examples

### Example 1: Complex Number Calculator
```python
import cmath
import math

class ComplexCalculator:
    """Calculator for complex number operations"""
    
    @staticmethod
    def add(z1, z2):
        return z1 + z2
    
    @staticmethod
    def subtract(z1, z2):
        return z1 - z2
    
    @staticmethod
    def multiply(z1, z2):
        return z1 * z2
    
    @staticmethod
    def divide(z1, z2):
        if z2 == 0:
            raise ValueError("Division by zero")
        return z1 / z2
    
    @staticmethod
    def magnitude(z):
        return abs(z)
    
    @staticmethod
    def phase(z):
        return cmath.phase(z)
    
    @staticmethod
    def conjugate(z):
        return z.conjugate()
    
    @staticmethod
    def power(z, n):
        return z ** n
    
    @staticmethod
    def sqrt(z):
        return cmath.sqrt(z)
    
    @staticmethod
    def display(z):
        """Display complex number in a readable format"""
        real = z.real
        imag = z.imag
        
        if imag >= 0:
            return f"{real:.4f} + {imag:.4f}i"
        else:
            return f"{real:.4f} - {abs(imag):.4f}i"

def complex_calculator_demo():
    """Interactive complex number calculator"""
    
    calc = ComplexCalculator()
    
    print("Complex Number Calculator")
    print("=" * 50)
    
    try:
        # Get input
        print("\nEnter first complex number (format: a+bj):")
        z1_str = input("z1 = ")
        z1 = complex(z1_str)
        
        print("\nEnter second complex number (format: a+bj):")
        z2_str = input("z2 = ")
        z2 = complex(z2_str)
        
        print(f"\nz1 = {calc.display(z1)}")
        print(f"z2 = {calc.display(z2)}")
        
        # Perform operations
        print("\n=== ARITHMETIC ===")
        print(f"z1 + z2 = {calc.display(calc.add(z1, z2))}")
        print(f"z1 - z2 = {calc.display(calc.subtract(z1, z2))}")
        print(f"z1 * z2 = {calc.display(calc.multiply(z1, z2))}")
        print(f"z1 / z2 = {calc.display(calc.divide(z1, z2))}")
        
        print("\n=== PROPERTIES ===")
        print(f"|z1| = {calc.magnitude(z1):.4f}")
        print(f"|z2| = {calc.magnitude(z2):.4f}")
        print(f"arg(z1) = {calc.phase(z1):.4f} rad ({math.degrees(calc.phase(z1)):.2f}°)")
        print(f"arg(z2) = {calc.phase(z2):.4f} rad ({math.degrees(calc.phase(z2)):.2f}°)")
        print(f"z1̄ = {calc.display(calc.conjugate(z1))}")
        print(f"z2̄ = {calc.display(calc.conjugate(z2))}")
        
        print("\n=== POWERS AND ROOTS ===")
        power = int(input("Enter power (integer): "))
        print(f"z1^{power} = {calc.display(calc.power(z1, power))}")
        print(f"√z1 = {calc.display(calc.sqrt(z1))}")
        print(f"√z2 = {calc.display(calc.sqrt(z2))}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Invalid input: {e}")

# complex_calculator_demo()
```

### Example 2: Mandelbrot Set Visualization
```python
import cmath

def mandelbrot(c, max_iterations=100):
    """
    Calculate if a point is in the Mandelbrot set
    Returns number of iterations until divergence
    """
    z = 0
    for n in range(max_iterations):
        z = z * z + c
        if abs(z) > 2:
            return n
    return max_iterations

def mandelbrot_ascii(width=80, height=24, x_range=(-2, 1), y_range=(-1, 1)):
    """Generate ASCII representation of Mandelbrot set"""
    
    x_start, x_end = x_range
    y_start, y_end = y_range
    
    # Characters for different iteration counts
    chars = " .:-=+*#%@"
    
    print("Mandelbrot Set Visualization")
    print("=" * width)
    
    for y in range(height):
        # Map y coordinate to complex plane
        cy = y_start + (y / height) * (y_end - y_start)
        line = ""
        
        for x in range(width):
            # Map x coordinate to complex plane
            cx = x_start + (x / width) * (x_end - x_start)
            c = complex(cx, cy)
            
            # Get iteration count
            iterations = mandelbrot(c, len(chars) - 1)
            
            # Select character based on iterations
            char_index = min(iterations, len(chars) - 1)
            line += chars[char_index]
        
        print(line)

def mandelbrot_detailed():
    """Detailed analysis of specific points"""
    
    print("Mandelbrot Set Analysis")
    print("=" * 50)
    
    test_points = [
        (0, 0),           # Origin (inside)
        (-0.5, 0),        # Inside
        (-1.5, 0),        # Boundary
        (-2, 0),          # Boundary
        (0.5, 0.5),       # Outside
        (-0.7269, 0.1889) # Interesting point
    ]
    
    for real, imag in test_points:
        c = complex(real, imag)
        iterations = mandelbrot(c, 1000)
        
        if iterations == 1000:
            status = "INSIDE (converges)"
        else:
            status = f"OUTSIDE (diverges after {iterations} iterations)"
        
        print(f"c = {real:6.4f} + {imag:6.4f}i → {status}")

# Uncomment to run (may take a moment)
# mandelbrot_ascii(80, 24)
# mandelbrot_detailed()
```

### Example 3: AC Circuit Analysis
```python
import cmath
import math

class ACComponent:
    """Base class for AC circuit components"""
    pass

class Resistor(ACComponent):
    def __init__(self, resistance):
        self.resistance = complex(resistance, 0)
    
    def impedance(self, frequency=None):
        return self.resistance

class Inductor(ACComponent):
    def __init__(self, inductance):
        self.inductance = inductance
    
    def impedance(self, frequency):
        # Z = jωL = j·2πf·L
        omega = 2 * math.pi * frequency
        return complex(0, omega * self.inductance)

class Capacitor(ACComponent):
    def __init__(self, capacitance):
        self.capacitance = capacitance
    
    def impedance(self, frequency):
        # Z = 1/(jωC) = -j/(ωC)
        omega = 2 * math.pi * frequency
        return complex(0, -1 / (omega * self.capacitance))

class ACCircuit:
    """AC circuit analyzer"""
    
    def __init__(self, frequency):
        self.frequency = frequency
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
    
    def total_impedance(self):
        """Calculate total impedance (series circuit)"""
        total = 0
        for comp in self.components:
            total += comp.impedance(self.frequency)
        return total
    
    def current(self, voltage):
        """Calculate current using Ohm's law: I = V / Z"""
        Z = self.total_impedance()
        if Z == 0:
            raise ValueError("Total impedance cannot be zero")
        return voltage / Z
    
    def power(self, voltage):
        """Calculate complex power: S = V * I* (I conjugate)"""
        I = self.current(voltage)
        return voltage * I.conjugate()
    
    def analyze(self, voltage_magnitude, voltage_phase=0):
        """Analyze circuit and display results"""
        voltage = cmath.rect(voltage_magnitude, voltage_phase)
        Z = self.total_impedance()
        I = self.current(voltage)
        S = self.power(voltage)
        
        print(f"Frequency: {self.frequency} Hz")
        print(f"Voltage: {voltage_magnitude}∠{math.degrees(voltage_phase):.1f}° V")
        print(f"Impedance: |Z| = {abs(Z):.2f} Ω, θ = {math.degrees(cmath.phase(Z)):.1f}°")
        print(f"Current: |I| = {abs(I):.3f} A, θ = {math.degrees(cmath.phase(I)):.1f}°")
        print(f"Power: |S| = {abs(S):.2f} VA")
        print(f"Real Power: {S.real:.2f} W")
        print(f"Reactive Power: {S.imag:.2f} VAR")
        print(f"Power Factor: {S.real / abs(S):.3f}")

# Example: RLC series circuit
print("RLC Series Circuit Analysis")
print("=" * 50)

# Create circuit
frequency = 1000  # 1 kHz
circuit = ACCircuit(frequency)

# Add components
R = 100  # 100 ohms
L = 0.1  # 100 mH
C = 1e-6  # 1 μF

circuit.add_component(Resistor(R))
circuit.add_component(Inductor(L))
circuit.add_component(Capacitor(C))

# Analyze
circuit.analyze(voltage_magnitude=10, voltage_phase=0)

# Find resonant frequency
print("\n" + "=" * 50)
print("Resonant Frequency Analysis:")
resonant_freq = 1 / (2 * math.pi * math.sqrt(L * C))
print(f"Resonant frequency: {resonant_freq:.1f} Hz")
```

### Example 4: Fourier Series Visualization
```python
import cmath
import math

class FourierSeries:
    """Fourier series representation of periodic signals"""
    
    def __init__(self, num_terms=10):
        self.num_terms = num_terms
        self.coefficients = []
    
    def square_wave_coefficients(self):
        """Calculate coefficients for square wave"""
        self.coefficients = []
        for n in range(1, self.num_terms + 1):
            if n % 2 == 1:  # Odd harmonics only
                cn = 4 / (cmath.pi * n)  # Real coefficient
                self.coefficients.append((n, complex(cn, 0)))
            else:
                self.coefficients.append((n, 0))
    
    def sawtooth_coefficients(self):
        """Calculate coefficients for sawtooth wave"""
        self.coefficients = []
        for n in range(1, self.num_terms + 1):
            cn = 2 / (cmath.pi * n) * (1j if n % 2 == 0 else -1j)
            self.coefficients.append((n, cn))
    
    def evaluate(self, t):
        """Evaluate Fourier series at time t"""
        result = 0
        for n, cn in self.coefficients:
            if cn != 0:
                result += cn * cmath.exp(1j * 2 * math.pi * n * t)
        return result.real  # Return real part
    
    def plot_approximation(self, cycles=2, points_per_cycle=200):
        """Generate ASCII plot of the approximation"""
        
        total_points = cycles * points_per_cycle
        t_values = [i / points_per_cycle for i in range(total_points)]
        y_values = [self.evaluate(t) for t in t_values]
        
        # Normalize y values
        y_min = min(y_values)
        y_max = max(y_values)
        y_range = y_max - y_min
        
        # Create ASCII plot
        height = 20
        width = 80
        
        print(f"\nFourier Series Approximation ({self.num_terms} terms)")
        print("=" * width)
        
        for row in range(height):
            y = y_max - (row / (height - 1)) * y_range
            line = ""
            
            for x in range(width):
                t = (x / width) * cycles
                y_approx = self.evaluate(t)
                
                # Check if this point is close to the current y level
                if abs(y_approx - y) < y_range / (height * 2):
                    line += "*"
                else:
                    line += " "
            
            # Add y-axis label
            if row == 0:
                label = f"{y_max:6.2f}"
            elif row == height // 2:
                label = f"{0:6.2f}"
            elif row == height - 1:
                label = f"{y_min:6.2f}"
            else:
                label = " " * 6
            
            print(f"{label} |{line}")
        
        # x-axis
        print(" " * 7 + "+" + "-" * width)
        print(" " * 8 + "0" + " " * (width // cycles - 1), end="")
        for cycle in range(1, cycles + 1):
            print(f"T{cycle}" + " " * (width // cycles - 2), end="")
        print()

# Demo Fourier series
print("Fourier Series Demonstration")
print("=" * 50)

# Square wave approximation
square = FourierSeries(10)
square.square_wave_coefficients()
square.plot_approximation(cycles=2)

# Sawtooth wave approximation
sawtooth = FourierSeries(10)
sawtooth.sawtooth_coefficients()
sawtooth.plot_approximation(cycles=2)

# Compare with different numbers of terms
for terms in [1, 3, 5, 10]:
    fs = FourierSeries(terms)
    fs.square_wave_coefficients()
    
    # Evaluate at specific point
    t = 0.25  # Quarter period
    value = fs.evaluate(t)
    print(f"Square wave at t={t} with {terms} terms: {value:.4f}")
```

### Example 5: Quantum Mechanics - Complex Wave Functions
```python
import cmath
import math

class QuantumWaveFunction:
    """Simple quantum wave function representation"""
    
    def __init__(self, mass=1.0, hbar=1.0):
        self.mass = mass
        self.hbar = hbar
    
    def plane_wave(self, x, k, t=0):
        """Plane wave: ψ = e^(i(kx - ωt))"""
        return cmath.exp(1j * (k * x - self.energy(k) * t))
    
    def energy(self, k):
        """Energy for given wave number"""
        return (self.hbar**2 * k**2) / (2 * self.mass)
    
    def gaussian_packet(self, x, x0=0, sigma=1, k0=5):
        """Gaussian wave packet"""
        envelope = math.exp(-((x - x0)**2) / (2 * sigma**2))
        oscillation = cmath.exp(1j * k0 * x)
        return envelope * oscillation
    
    def probability_density(self, psi):
        """Calculate |ψ|² (probability density)"""
        return abs(psi)**2
    
    def phase(self, psi):
        """Calculate phase of wave function"""
        return cmath.phase(psi)
    
    def expectation_value(self, psi_func, x_values):
        """Calculate expectation value of position"""
        numerator = 0
        denominator = 0
        
        for x in x_values:
            psi = psi_func(x)
            prob = self.probability_density(psi)
            numerator += x * prob
            denominator += prob
        
        return numerator / denominator if denominator != 0 else 0

# Demonstrate quantum mechanics concepts
print("Quantum Mechanics: Complex Wave Functions")
print("=" * 60)

qm = QuantumWaveFunction()

# Test different x positions
x_values = [x * 0.1 for x in range(-50, 51)]

# Plane wave
k = 5.0
print("\nPlane Wave (k=5):")
for x in [-2, -1, 0, 1, 2]:
    psi = qm.plane_wave(x, k)
    prob = qm.probability_density(psi)
    phase = qm.phase(psi)
    print(f"x={x:3.0f}: ψ = {psi.real:6.3f} + {psi.imag:6.3f}i, |ψ|²={prob:.3f}, φ={phase:.3f}")

# Gaussian wave packet
print("\nGaussian Wave Packet:")
packet_center = qm.expectation_value(lambda x: qm.gaussian_packet(x, x0=0, sigma=2, k0=3), x_values)
print(f"Expectation value of position: ⟨x⟩ = {packet_center:.3f}")

# Probability density plot
def plot_probability_density(x_values, psi_func):
    """ASCII plot of probability density"""
    width = 70
    height = 15
    
    y_values = [qm.probability_density(psi_func(x)) for x in x_values]
    y_max = max(y_values)
    
    print("\nProbability Density |ψ|²:")
    print("-" * width)
    
    for row in range(height):
        y_level = y_max * (1 - row / (height - 1))
        line = ""
        
        for y in y_values:
            if y >= y_level:
                line += "█"
            else:
                line += " "
        
        print(f"{line}")
    
    # x-axis
    print("-" * width)
    print(" " * (width // 2) + "x →")
    print(f"x range: [{x_values[0]:.1f}, {x_values[-1]:.1f}]")

# Plot Gaussian packet
plot_probability_density(x_values, lambda x: qm.gaussian_packet(x, x0=0, sigma=2, k0=3))

# Superposition principle
print("\n" + "=" * 60)
print("Superposition of Two Plane Waves:")

def superposition(x):
    psi1 = qm.plane_wave(x, k1=3)
    psi2 = qm.plane_wave(x, k2=5)
    return psi1 + psi2

prob_superposition = [qm.probability_density(superposition(x)) for x in x_values]
print(f"Max probability: {max(prob_superposition):.3f}")
print(f"Min probability: {min(prob_superposition):.3f}")
print("Interference pattern detected!")
```

### Example 6: Signal Processing with Complex Numbers
```python
import cmath
import math
import random

class SignalProcessor:
    """Signal processing using complex numbers"""
    
    @staticmethod
    def generate_signal(frequency, duration, sampling_rate=1000):
        """Generate sinusoidal signal"""
        times = []
        signal = []
        samples = int(duration * sampling_rate)
        
        for i in range(samples):
            t = i / sampling_rate
            times.append(t)
            # Complex exponential representation
            value = cmath.exp(1j * 2 * math.pi * frequency * t)
            signal.append(value)
        
        return times, signal
    
    @staticmethod
    def add_noise(signal, noise_level=0.1):
        """Add complex Gaussian noise to signal"""
        noisy = []
        for s in signal:
            noise = complex(
                random.gauss(0, noise_level),
                random.gauss(0, noise_level)
            )
            noisy.append(s + noise)
        return noisy
    
    @staticmethod
    def dft(signal):
        """Discrete Fourier Transform (naive implementation)"""
        N = len(signal)
        spectrum = []
        
        for k in range(N):
            sum_val = 0
            for n in range(N):
                angle = -2 * cmath.pi * k * n / N
                sum_val += signal[n] * cmath.exp(1j * angle)
            spectrum.append(sum_val)
        
        return spectrum
    
    @staticmethod
    def magnitude_spectrum(spectrum):
        """Calculate magnitude spectrum"""
        return [abs(s) for s in spectrum]
    
    @staticmethod
    def phase_spectrum(spectrum):
        """Calculate phase spectrum"""
        return [cmath.phase(s) for s in spectrum]
    
    @staticmethod
    def plot_spectrum(magnitudes, title="Spectrum"):
        """ASCII plot of magnitude spectrum"""
        height = 15
        width = 70
        
        max_mag = max(magnitudes)
        if max_mag == 0:
            return
        
        print(f"\n{title}")
        print("=" * width)
        
        for row in range(height):
            y_level = max_mag * (1 - row / (height - 1))
            line = ""
            
            for mag in magnitudes:
                if mag >= y_level:
                    line += "█"
                else:
                    line += " "
            
            print(f"{line}")
        
        print("-" * width)
        print("Frequency bins →")

# Signal processing demo
print("Signal Processing with Complex Numbers")
print("=" * 60)

sp = SignalProcessor()

# Generate signals
print("\nGenerating signals...")
freq1 = 50   # 50 Hz
freq2 = 120  # 120 Hz
duration = 1  # 1 second

_, signal1 = sp.generate_signal(freq1, duration)
_, signal2 = sp.generate_signal(freq2, duration)

# Combine signals
combined = [s1 + s2 for s1, s2 in zip(signal1, signal2)]

# Add noise
noisy_signal = sp.add_noise(combined, noise_level=0.2)

# Perform DFT
print("Computing DFT...")
spectrum = sp.dft(noisy_signal)

# Calculate spectra
magnitudes = sp.magnitude_spectrum(spectrum)
# phases = sp.phase_spectrum(spectrum)

# Plot results
sp.plot_spectrum(magnitudes[:200], "Frequency Spectrum (First 200 bins)")

# Find dominant frequencies
sorted_indices = sorted(range(len(magnitudes)), key=lambda i: magnitudes[i], reverse=True)
print(f"\nTop 3 frequency components:")
for i, idx in enumerate(sorted_indices[:3], 1):
    frequency = idx / duration  # Convert bin to frequency
    print(f"  {i}. Frequency: {frequency:.1f} Hz, Magnitude: {magnitudes[idx]:.2f}")

# Demodulation example
print("\n" + "=" * 60)
print("AM Demodulation:")

# Create AM signal
carrier_freq = 1000
message_freq = 50
_, carrier = sp.generate_signal(carrier_freq, duration)
_, message = sp.generate_signal(message_freq, duration)

# AM modulation: (1 + m(t)) * carrier
am_signal = [(1 + m.real) * c for c, m in zip(carrier, message)]

# Demodulate (multiply by carrier and low-pass filter)
demodulated = [am * c.conjugate() for am, c in zip(am_signal, carrier)]

# Extract real part (should recover message)
recovered = [d.real for d in demodulated]

print(f"Original message frequency: {message_freq} Hz")
print(f"Carrier frequency: {carrier_freq} Hz")
print("AM modulation and demodulation performed")
print("Recovered signal magnitude:", abs(recovered[0]))
```

## Complex Number Functions Reference

### Built-in Functions
```python
# Creation
z = complex(3, 4)     # (3+4j)

# Properties
z.real                # Real part
z.imag                # Imaginary part
z.conjugate()         # Complex conjugate

# Operations
abs(z)                # Magnitude
+z, -z                # Unary plus/minus
z1 + z2, z1 - z2      # Addition/subtraction
z1 * z2, z1 / z2      # Multiplication/division
z ** n                # Power (integer exponent)
```

### cmath Module Functions
```python
import cmath

# Constants
cmath.pi              # π
cmath.e               # e
cmath.tau             # 2π
cmath.inf             # Infinity
cmath.nan             # NaN

# Conversions
cmath.phase(z)        # Phase angle
cmath.polar(z)        # (r, phi)
cmath.rect(r, phi)    # Complex from polar

# Exponential and logs
cmath.exp(z)          # e^z
cmath.log(z)          # Natural log
cmath.log10(z)        # Base-10 log
cmath.sqrt(z)         # Square root

# Trigonometric
cmath.sin(z)          # Sine
cmath.cos(z)          # Cosine
cmath.tan(z)          # Tangent
cmath.asin(z)         # Arc sine
cmath.acos(z)         # Arc cosine
cmath.atan(z)         # Arc tangent

# Hyperbolic
cmath.sinh(z)         # Hyperbolic sine
cmath.cosh(z)         # Hyperbolic cosine
cmath.tanh(z)         # Hyperbolic tangent
cmath.asinh(z)        # Inverse hyperbolic sine
cmath.acosh(z)        # Inverse hyperbolic cosine
cmath.atanh(z)        # Inverse hyperbolic tangent

# Classification
cmath.isinf(z)        # Is infinite?
cmath.isnan(z)        # Is NaN?
cmath.isfinite(z)     # Is finite?
```

## Common Mistakes

### Mistake 1: Using i instead of j
```python
# Wrong
# z = 3 + 4i  # SyntaxError!

# Right
z = 3 + 4j   # Use j or J
z = 3 + 4J   # Also works
```

### Mistake 2: Comparing Complex Numbers
```python
# Wrong
z1 = 3 + 4j
z2 = 4 + 3j
# if z1 > z2:  # TypeError!

# Right - compare magnitudes
if abs(z1) > abs(z2):
    print("z1 has larger magnitude")

# Compare real/imag parts separately
if z1.real > z2.real:
    print("z1 has larger real part")
```

### Mistake 3: Division by Zero
```python
# Wrong
z1 = 3 + 4j
z2 = 0 + 0j
# result = z1 / z2  # ZeroDivisionError

# Right
if z2 != 0:
    result = z1 / z2
else:
    print("Cannot divide by zero")
```

### Mistake 4: Forgetting cmath for Complex Functions
```python
import math
import cmath

z = 3 + 4j

# Wrong - math functions work with floats only
# print(math.sqrt(z))  # TypeError!

# Right - use cmath for complex numbers
print(cmath.sqrt(z))    # (2+1j)

# Use math for real numbers only
print(math.sqrt(25))     # 5.0 (works with float)
```

### Mistake 5: Assuming Real/Imag are Integers
```python
z = 3 + 4j
print(type(z.real))  # <class 'float'>
print(type(z.imag))  # <class 'float'>

# Real and imaginary parts are always floats
```

## Performance Considerations

```python
import time

# Complex operations are slower than float operations
def performance_compare():
    iterations = 10_000_000
    
    # Float addition
    start = time.time()
    f = 0.0
    for i in range(iterations):
        f += 1.0
    float_time = time.time() - start
    
    # Complex addition
    start = time.time()
    c = 0 + 0j
    for i in range(iterations):
        c += 1 + 0j
    complex_time = time.time() - start
    
    print(f"Float addition: {float_time:.3f}s")
    print(f"Complex addition: {complex_time:.3f}s")
    print(f"Complex overhead: {(complex_time/float_time - 1)*100:.1f}%")

# performance_compare()
```

## Quick Reference Table

| Operation | Syntax | Example | Result |
|-----------|--------|---------|---------|
| Create | `a + bj` | `3 + 4j` | `(3+4j)` |
| Create | `complex(a, b)` | `complex(3, 4)` | `(3+4j)` |
| Real part | `z.real` | `(3+4j).real` | `3.0` |
| Imag part | `z.imag` | `(3+4j).imag` | `4.0` |
| Conjugate | `z.conjugate()` | `(3+4j).conjugate()` | `(3-4j)` |
| Magnitude | `abs(z)` | `abs(3+4j)` | `5.0` |
| Phase | `cmath.phase(z)` | `cmath.phase(3+4j)` | `0.927` |
| Polar | `cmath.polar(z)` | `cmath.polar(3+4j)` | `(5.0, 0.927)` |
| Rectangular | `cmath.rect(r, θ)` | `cmath.rect(5, 0.927)` | `(3+4j)` |
| Add | `z1 + z2` | `(1+2j)+(3+4j)` | `(4+6j)` |
| Multiply | `z1 * z2` | `(1+2j)*(3+4j)` | `(-5+10j)` |

## Summary

- **Complex numbers**: `a + bj` form (uses `j` not `i`)
- **Access**: `z.real` and `z.imag` (both are floats)
- **Conjugate**: `z.conjugate()` gives `a - bj`
- **Magnitude**: `abs(z)` = √(a² + b²)
- **Phase**: `cmath.phase(z)` = arctan(b/a)
- **Arithmetic**: Supports +, -, *, /, **
- **Comparisons**: Only `==` and `!=` (no <, >, <=, >=)
- **cmath module**: Math functions for complex numbers
- **Conversions**: `cmath.polar()` and `cmath.rect()`
- **Applications**: Signal processing, quantum mechanics, AC circuits

## Basic Template
```python
#!/usr/bin/env python3

import cmath
import math

# Create complex numbers
def create_complex():
    """Different ways to create complex numbers"""
    
    # Direct literal
    z1 = 3 + 4j
    print(f"z1 = {z1}")
    
    # Using complex() constructor
    z2 = complex(3, 4)
    print(f"z2 = {z2}")
    
    # From string
    z3 = complex("3+4j")
    print(f"z3 = {z3}")
    
    # Pure real
    z4 = complex(5)
    print(f"z4 = {z4}")
    
    # Pure imaginary
    z5 = complex(0, 5)
    print(f"z5 = {z5}")

# Access properties
def complex_properties(z):
    """Access real, imag, and conjugate"""
    
    print(f"z = {z}")
    print(f"Real part: {z.real}")
    print(f"Imaginary part: {z.imag}")
    print(f"Conjugate: {z.conjugate()}")
    print(f"Magnitude: {abs(z)}")
    print(f"Phase: {cmath.phase(z)} rad")
    print(f"Phase: {math.degrees(cmath.phase(z)):.1f}°")

# Complex arithmetic
def complex_arithmetic(z1, z2):
    """Perform arithmetic operations"""
    
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 - z2 = {z1 - z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1 / z2 = {z1 / z2}")
    print(f"z1 ** 2 = {z1 ** 2}")

# Polar coordinates
def polar_rectangular():
    """Convert between rectangular and polar"""
    
    # Rectangular to polar
    z = 3 + 4j
    r, theta = cmath.polar(z)
    print(f"Rectangular: {z}")
    print(f"Polar: r={r:.2f}, θ={theta:.2f} rad")
    
    # Polar to rectangular
    z2 = cmath.rect(r, theta)
    print(f"Back to rectangular: {z2}")

# Euler's formula
def euler_demo():
    """Demonstrate Euler's formula"""
    
    angles = [0, math.pi/4, math.pi/2, math.pi, 3*math.pi/2]
    
    print("Euler's Formula: e^(iθ) = cos(θ) + i·sin(θ)")
    print("-" * 50)
    
    for theta in angles:
        euler = cmath.exp(1j * theta)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        
        print(f"θ = {theta:5.2f} rad ({math.degrees(theta):3.0f}°)")
        print(f"  e^(iθ) = {euler.real:6.3f} + {euler.imag:6.3f}i")
        print(f"  cos(θ) = {cos_theta:6.3f}, sin(θ) = {sin_theta:6.3f}")
        print()

# Main demo
if __name__ == "__main__":
    print("=== CREATE COMPLEX NUMBERS ===")
    create_complex()
    
    print("\n=== COMPLEX PROPERTIES ===")
    complex_properties(3 + 4j)
    
    print("\n=== COMPLEX ARITHMETIC ===")
    complex_arithmetic(3 + 4j, 1 - 2j)
    
    print("\n=== POLAR CONVERSIONS ===")
    polar_rectangular()
    
    print("\n=== EULER'S FORMULA ===")
    euler_demo()
```

*This documentation belongs to https://github.com/InterCentury*