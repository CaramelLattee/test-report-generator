# ============================================
# test_engine.py
# Project : Test Report Generator
# Author  : Muhammad Hafizul
# ============================================

from datetime import datetime

# ── SPEC LIMITS ──
VOLT_LSL = 4.5
VOLT_USL = 5.5
CURR_LSL = 0.8
CURR_USL = 1.2
TEMP_LSL = 20.0
TEMP_USL = 35.0

class TestUnit:
    """Represents a single unit under test"""

    def __init__(self, unit_id, voltage,
                 current, temperature):
        self.unit_id     = unit_id
        self.voltage     = voltage
        self.current     = current
        self.temperature = temperature
        self.status      = "UNTESTED"
        self.fail_reason = []
        self.timestamp   = datetime.now().strftime(
                           "%Y-%m-%d %H:%M:%S")

    def run_test(self):
        """Run all parameter tests"""
        self.fail_reason = []

        volt_ok = VOLT_LSL <= self.voltage <= VOLT_USL
        curr_ok = CURR_LSL <= self.current <= CURR_USL
        temp_ok = TEMP_LSL <= self.temperature <= TEMP_USL

        if not volt_ok:
            self.fail_reason.append(
                "Volt_LOW" if self.voltage < VOLT_LSL
                else "Volt_HIGH")
        if not curr_ok:
            self.fail_reason.append(
                "Curr_LOW" if self.current < CURR_LSL
                else "Curr_HIGH")
        if not temp_ok:
            self.fail_reason.append(
                "Temp_LOW" if self.temperature < TEMP_LSL
                else "Temp_HIGH")

        self.status = "PASS" if not self.fail_reason \
                      else "FAIL"
        return self.status

    def to_dict(self):
        """Convert to dictionary for reporting"""
        return {
            "timestamp"  : self.timestamp,
            "unit_id"    : self.unit_id,
            "voltage"    : self.voltage,
            "current"    : self.current,
            "temperature": self.temperature,
            "status"     : self.status,
            "fail_reason": ", ".join(self.fail_reason)
        }

    def __str__(self):
        reason = f" | {', '.join(self.fail_reason)}" \
                 if self.fail_reason else ""
        return (f"Unit {self.unit_id:<3} "
                f"| {self.voltage}V "
                f"| {self.current}A "
                f"| {self.temperature}C "
                f"| {self.status}{reason}")


class TestEngine:
    """Manages complete test session"""

    def __init__(self, product, station, operator):
        self.product   = product
        self.station   = station
        self.operator  = operator
        self.units     = []
        self.start_time = datetime.now().strftime(
                          "%Y-%m-%d %H:%M:%S")

    def add_unit(self, voltage, current, temperature):
        """Add and test a unit"""
        try:
            # Validate inputs
            if not isinstance(voltage,
                              (int, float)):
                raise TypeError("Voltage must be number!")
            if not isinstance(current,
                              (int, float)):
                raise TypeError("Current must be number!")
            if not isinstance(temperature,
                              (int, float)):
                raise TypeError("Temperature must be number!")

            unit_id = len(self.units) + 1
            unit    = TestUnit(unit_id, voltage,
                               current, temperature)
            unit.run_test()
            self.units.append(unit)
            return unit

        except TypeError as e:
            print(f"❌ Invalid input: {e}")
            return None

    def get_passed(self):
        return [u for u in self.units
                if u.status == "PASS"]

    def get_failed(self):
        return [u for u in self.units
                if u.status == "FAIL"]

    def get_fpy(self):
        if not self.units: return 0.0
        return len(self.get_passed()) / \
               len(self.units) * 100

    def get_stats(self):
        """Get voltage statistics"""
        if not self.units:
            return {}
        voltages = [u.voltage for u in self.units]
        currents = [u.current for u in self.units]
        return {
            "volt_max" : max(voltages),
            "volt_min" : min(voltages),
            "volt_avg" : sum(voltages)/len(voltages),
            "curr_max" : max(currents),
            "curr_min" : min(currents),
            "curr_avg" : sum(currents)/len(currents),
        }

    def print_summary(self):
        """Print test summary to screen"""
        passed = len(self.get_passed())
        failed = len(self.get_failed())
        total  = len(self.units)
        fpy    = self.get_fpy()

        print("\n" + "=" * 45)
        print(f"  TEST SUMMARY")
        print("=" * 45)
        print(f"Product  : {self.product}")
        print(f"Station  : {self.station}")
        print(f"Operator : {self.operator}")
        print("-" * 45)
        print(f"Total    : {total} units")
        print(f"Pass     : {passed} units")
        print(f"Fail     : {failed} units")
        print(f"FPY      : {fpy:.1f}%")

        if   fpy >= 95: rating = "EXCELLENT ⭐⭐⭐"
        elif fpy >= 80: rating = "GOOD ⭐⭐"
        elif fpy >= 60: rating = "ACCEPTABLE ⭐"
        else:           rating = "POOR ❌"
        print(f"Rating   : {rating}")
        print("=" * 45)