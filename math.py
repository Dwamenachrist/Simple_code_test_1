import math

# --- Simple Functions ---

def add(x: int, y: int) -> int:
    """Adds two integers."""
    return x + y

def subtract(x: int, y: int) -> int:
    """Subtracts second integer from the first."""
    return x - y

def greet(name: str) -> str:
    """Returns a greeting string."""
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"

# --- Function with Conditional Logic and Potential Error ---

def divide(numerator: float, denominator: float) -> float:
    """Divides numerator by denominator. Raises ValueError for division by zero."""
    if denominator == 0:
        raise ValueError("Cannot divide by zero!")
    return numerator / denominator

# --- Function using an external (standard library) module ---

def calculate_circle_area(radius: float) -> float:
    """Calculates the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

# --- A Simple Class ---

class Calculator:
    """A simple calculator class."""

    def __init__(self, initial_value: float = 0):
        self.current_value = initial_value

    def add(self, value_to_add: float) -> None:
        """Adds a value to the current value."""
        self.current_value += value_to_add

    def multiply(self, value_to_multiply: float) -> None:
        """Multiplies the current value by a given value."""
        if value_to_multiply == 0:
            self.current_value = 0 # Multiplying by zero results in zero
        elif self.current_value == 0:
            pass # Zero multiplied by anything (other than zero) is still zero
        else:
            self.current_value *= value_to_multiply

    def get_value(self) -> float:
        """Returns the current value."""
        return self.current_value

    def reset(self) -> None:
        """Resets the current value to zero."""
        self.current_value = 0

# --- Another function with different types of edge cases ---
def process_user_data(user: dict) -> str:
    """Processes user data dictionary and returns a status string."""
    if not isinstance(user, dict):
        raise TypeError("Input must be a dictionary.")
    
    name = user.get("name")
    age = user.get("age")
    is_active = user.get("is_active", False) # Default to False if not present

    if not name:
        return "Error: User name is missing."
    
    status_message = f"User: {name}"
    if age is not None:
        if not isinstance(age, int):
            return f"Error: Age for {name} must be an integer."
        if age < 0:
            return f"Error: Age for {name} cannot be negative."
        status_message += f", Age: {age}"
    
    status_message += f", Active: {is_active}"
    return status_message

if __name__ == '__main__':
    # Example usages (not for testing by the agent, just for illustration)
    print(add(5, 3))
    print(greet("Alice"))
    print(greet(""))
    
    try:
        print(divide(10, 2))
        print(divide(10, 0))
    except ValueError as e:
        print(e)
        
    print(calculate_circle_area(5))

    calc = Calculator()
    calc.add(10)
    calc.multiply(3)
    print(f"Calculator value: {calc.get_value()}") # Expected: 30

    user1 = {"name": "Bob", "age": 30, "is_active": True}
    user2 = {"name": "Charlie"}
    user3 = {"name": "Dave", "age": "thirty"} # Invalid age type
    user4 = {} # Missing name
    print(process_user_data(user1))
    print(process_user_data(user2))
    print(process_user_data(user3))
    print(process_user_data(user4))
