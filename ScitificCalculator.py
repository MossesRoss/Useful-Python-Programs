import math
import numpy as np

def scientific_calculator():
    print("Scientific Calculator")

    while True:
        expression = input("Enter an expression (type 'quit' to exit): ")

        if expression.lower() == 'quit':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Using eval for basic arithmetic and math functions
            result = eval(expression)
            
            # Using numpy for more advanced mathematical operations
            result_np = np.array(eval(expression), dtype=np.float64)

            print("Result (using eval):", result)
            print("Result (using numpy):", result_np)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    scientific_calculator()
