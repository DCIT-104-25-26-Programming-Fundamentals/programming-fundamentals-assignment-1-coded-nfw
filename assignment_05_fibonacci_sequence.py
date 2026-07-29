# =============================================================================
def generate_fibonacci():
    print("\n--- Fibonacci Sequence Generator ---")
    try:
        n_terms = int(input("Enter the number of terms: "))
        
        if n_terms <= 0:
            print("Please enter a positive integer.")
            return

        fib_sequence = []
        a, b = 0, 1
        
        for _ in range(n_terms):
            fib_sequence.append(a)
            a, b = b, a + b
            
        print(f"Fibonacci Sequence ({n_terms} terms): {fib_sequence}")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    generate_fibonacci()