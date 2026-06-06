# ============================================
# reporter.py
# Project : Test Report Generator
# Author  : Muhammad Hafizul
# ============================================

import csv
import os
from datetime import datetime

class Reporter:
    """Generates CSV and TXT reports"""

    def __init__(self, output_folder="output"):
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

    def save_csv(self, engine):
        """Save test results to CSV"""
        filename = os.path.join(
            self.output_folder,
            f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        try:
            with open(filename, "w", newline="") as f:
                fieldnames = [
                    "Timestamp", "UnitID",
                    "Voltage", "Current",
                    "Temperature", "Status",
                    "FailReason"
                ]
                writer = csv.DictWriter(
                    f, fieldnames=fieldnames)
                writer.writeheader()

                for unit in engine.units:
                    d = unit.to_dict()
                    writer.writerow({
                        "Timestamp"  : d["timestamp"],
                        "UnitID"     : d["unit_id"],
                        "Voltage"    : d["voltage"],
                        "Current"    : d["current"],
                        "Temperature": d["temperature"],
                        "Status"     : d["status"],
                        "FailReason" : d["fail_reason"]
                    })

            print(f"✅ CSV saved: {filename}")
            return filename

        except Exception as e:
            print(f"❌ CSV Error: {e}")
            return None

    def save_txt(self, engine):
        """Save formatted TXT report"""
        filename = os.path.join(
            self.output_folder,
            f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        try:
            stats  = engine.get_stats()
            passed = len(engine.get_passed())
            failed = len(engine.get_failed())
            total  = len(engine.units)
            fpy    = engine.get_fpy()

            with open(filename, "w") as f:
                f.write("=" * 50 + "\n")
                f.write("       FUNCTIONAL TEST REPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"Date     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Product  : {engine.product}\n")
                f.write(f"Station  : {engine.station}\n")
                f.write(f"Operator : {engine.operator}\n")
                f.write(f"Spec V   : 4.5V - 5.5V\n")
                f.write(f"Spec I   : 0.8A - 1.2A\n")
                f.write(f"Spec T   : 20C - 35C\n")
                f.write("-" * 50 + "\n")
                f.write(f"{'Unit':<6}{'Volt':<8}"
                        f"{'Curr':<8}{'Temp':<8}"
                        f"{'Status':<8}{'Reason'}\n")
                f.write("-" * 50 + "\n")

                for unit in engine.units:
                    d = unit.to_dict()
                    f.write(
                        f"{d['unit_id']:<6}"
                        f"{d['voltage']:<8}"
                        f"{d['current']:<8}"
                        f"{d['temperature']:<8}"
                        f"{d['status']:<8}"
                        f"{d['fail_reason']}\n")

                f.write("-" * 50 + "\n")
                f.write(f"TOTAL    : {total} units\n")
                f.write(f"PASS     : {passed} units\n")
                f.write(f"FAIL     : {failed} units\n")
                f.write(f"FPY      : {fpy:.1f}%\n")

                if stats:
                    f.write("-" * 50 + "\n")
                    f.write("STATISTICS:\n")
                    f.write(f"Volt Max : {stats['volt_max']}V\n")
                    f.write(f"Volt Min : {stats['volt_min']}V\n")
                    f.write(f"Volt Avg : {stats['volt_avg']:.2f}V\n")
                    f.write(f"Curr Max : {stats['curr_max']}A\n")
                    f.write(f"Curr Min : {stats['curr_min']}A\n")
                    f.write(f"Curr Avg : {stats['curr_avg']:.2f}A\n")

                f.write("=" * 50 + "\n")

            print(f"✅ TXT saved: {filename}")
            return filename

        except Exception as e:
            print(f"❌ TXT Error: {e}")
            return None