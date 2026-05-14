# Project 01: Personal Finance Calculator

### Key Concepts to Apply

1. **Type Annotations**: Ensure your variables are declared with types, e.g., `salary: float = float(input(...))`.
2. **The F-String "Mini-Language"**:
   - To add commas to thousands: `{amount:,}`
   - To fix decimals to 2 places: `{amount:.2f}`
   - To align text: `{text:<20}` (left) or `{text:>20}` (right).
   - Combined: `f"₦{amount:>15,.2f}"`
3. **Currency Symbol**: You can use the Naira symbol `₦` directly in your strings.
4. **Validation**: Use `sys.exit(1)` to stop the program immediately if the user enters invalid data.

### Bonus Hint: The 12-Month Projection
To handle the months for the bonus challenge without a third-party library, consider creating a list:
`months = ["January", "February", "March", ...]`
and loop through it using a `for` loop, adding the monthly savings to a `running_total` variable each time.