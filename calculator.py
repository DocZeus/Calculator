import tkinter as tk
from operations import add, subtract, multiply, divide, exponent

def on_click(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        elif operation == 'exponent':
            result = exponent(num1, num2)
            
        label_result.config(text=f"Result: {result}")
        
    except ValueError: # exception for catching errors when input cannot be converted to a number
        label_result.config(text="Please enter valid numbers!")
    except Exception as e: # exception for catching any strings or any other errors
        label_result.config(text=str(e)) # str(e) converts the error message into a readable string
        
def main():
    global entry_num1, entry_num2, label_result
    
    root = tk.Tk()
    root.title("Calculator")

    root.geometry("300x250")
    root.resizable(False, False)

    # Entering inputs
    label_num1 = tk.Label(root, text="First number:")
    label_num1.grid(row=0, column=0, padx=10, pady=10)

    entry_num1 = tk.Entry(root)
    entry_num1.grid(row=0, column=1, padx=10, pady=10)

    label_num2 = tk.Label(root, text="Second number:")
    label_num2.grid(row=1, column=0, padx=10, pady=10)

    entry_num2 = tk.Entry(root)
    entry_num2.grid(row=1, column=1, padx=10, pady=10)

    # Operations
    button_add = tk.Button(root, text="Add", command=lambda: on_click('add'))
    button_add.grid(row=2, column=0, padx=10, pady=5)

    button_subtract = tk.Button(root, text="Subtract", command=lambda: on_click('subtract'))
    button_subtract.grid(row=2, column=1, padx=10, pady=5)

    button_multiply = tk.Button(root, text="Multiply", command=lambda: on_click('multiply'))
    button_multiply.grid(row=3, column=0, padx=10, pady=5)

    button_divide = tk.Button(root, text="Divide", command=lambda: on_click('divide'))
    button_divide.grid(row=3, column=1, padx=10, pady=5)

    button_exponent = tk.Button(root, text="Exponent", command=lambda: on_click('exponent'))
    button_exponent.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    # Results
    label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
    label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()