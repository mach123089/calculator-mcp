from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Basic operations with floats")

# Existing tool definitions (unchanged)
@mcp.tool()
def add_float(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def sub_float(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def mul_float(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def div_float(a: float, b: float) -> float:
    """Divide two numbers (returns floating point result)"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":                                                                  
    mcp.run(transport="stdio")