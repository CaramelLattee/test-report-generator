# ============================================
# main.py
# Project : Test Report Generator
# Author  : Muhammad Hafizul
# ============================================

from test_engine import TestEngine
from reporter   import Reporter

def get_float_input(prompt, min_val, max_val):
    """Get validated float input from user"""
    while True:
        try:
            value = float(input(prompt))
            if not min_val <= value <= max_val:
                print(f"❌ Must be {min_val} - {max_val}!")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number!")

def main():
    print("=" * 45)
    print("   TEST REPORT GENERATOR v1.0")
    print("=" * 45)

    # Get session info
    product  = input("Product name  : ")
    station  = input("Station ID    : ")
    operator = input("Operator name : ")

    engine   = TestEngine(product, station, operator)
    reporter = Reporter()

    print("\n📊 Enter test readings")
    print("(type 'done' when finished)\n")

    while True:
        print(f"--- Unit {len(engine.units)+1} ---")

        # Check if done
        volt_input = input("Voltage (V) or 'done': ")
        if volt_input.lower() == "done":
            if len(engine.units) == 0:
                print("❌ No units tested!")
                continue
            break

        try:
            voltage = float(volt_input)
            current = get_float_input(
                "Current (A)    : ", 0, 10)
            temperature = get_float_input(
                "Temperature (C): ", -50, 150)

            unit = engine.add_unit(
                voltage, current, temperature)

            if unit:
                print(f"→ {unit}")

        except ValueError:
            print("❌ Invalid voltage — try again!")
            continue

    # Print summary
    engine.print_summary()

    # Print all results
    print("\n--- ALL RESULTS ---")
    for unit in engine.units:
        print(unit)

    # Save reports
    print("\n--- SAVING REPORTS ---")
    reporter.save_csv(engine)
    reporter.save_txt(engine)

    print("\n✅ Done! Check output/ folder for reports")
    print("   Open CSV in Excel for best view! 📊")

if __name__ == "__main__":
    main()