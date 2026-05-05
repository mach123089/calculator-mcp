from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("Advanced Calculator")

# Existing tool definitions (unchanged)
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def sub(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def mul(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def div(a: float, b: float) -> float:
    """Divide two numbers (returns floating point result)"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise a number to a power"""
    return math.pow(base, exponent)

@mcp.tool()
def square_root(x: float) -> float:
    """Calculate square root of a number"""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

@mcp.tool()
def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

@mcp.tool()
def log(x: float, base: float = math.e) -> float:
    """Calculate logarithm of a number with optional base (default: natural log)"""
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(x, base)

@mcp.tool()
def sin(x: float) -> float:
    """Calculate sine of an angle in radians"""
    return math.sin(x)

@mcp.tool()
def cos(x: float) -> float:
    """Calculate cosine of an angle in radians"""
    return math.cos(x)

@mcp.tool()
def tan(x: float) -> float:
    """Calculate tangent of an angle in radians"""
    return math.tan(x)

@mcp.tool()
def degrees_to_radians(degrees: float) -> float:
    """Convert degrees to radians"""
    return math.radians(degrees)

@mcp.tool()
def radians_to_degrees(radians: float) -> float:
    """Convert radians to degrees"""
    return math.degrees(radians)

@mcp.tool()
def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two integers"""
    return math.gcd(a, b)

@mcp.tool()
def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two integers"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

@mcp.tool()
def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

@mcp.tool()
def quadratic_roots(a: float, b: float, c: float) -> tuple:
    """
    Solve quadratic equation ax² + bx + c = 0
    Returns a tuple of roots (real or complex)
    """
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)


if __name__ == "__main__":
    mcp.run(transport="stdio")