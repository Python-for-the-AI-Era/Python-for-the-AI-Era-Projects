import sys

def main():
    print("\n--- Personal Finance Data Entry ---")
    
    # 1. INPUT SECTION
    # TODO: Collect inputs using input(). 
    # Hint: Remember to convert strings to float!
    
    # 2. VALIDATION
    # TODO: If total_income <= 0, sys.exit(1)
    # TODO: Ensure all expenses are >= 0
    
    # 3. CALCULATIONS
    # TODO: Calculate totals, net savings, and savings rate
    # formula: (net_savings / total_income) * 100
    
    # 4. CATEGORIZATION
    # TODO: Use if/elif/else to determine if status is 'Excellent', 'Good', or 'Needs Work'
    
    # 5. FORMATTED REPORT
    # TODO: Print the summary using f-string alignment.
    # Example: f"{'Salary:':<15} ₦{salary:>12,.2f}"
    
    print("\nMonthly Finance Summary")
    print("════════════════════════════════")
    # ... student prints formatted data here ...

if __name__ == "__main__":
    main()