from config import IR_SENSOR_PIN
from sensor.ir_sensor import IRSensor
from database.db_manager import DatabaseManager
from emailer.smtp_client import send_email
from utils.timestamp import get_timestamp
import time

def main():
    ir = IRSensor(IR_SENSOR_PIN)
    db = DatabaseManager()

    try:
        print("Monitoring started... Press CTRL+C to stop.")
        while True:
            if ir.detect_motion():
                timestamp = get_timestamp()
                message = f"Motion detected at {timestamp}"
                print(message)
                
                db.insert_event(timestamp, message)
                send_email("Motion Detected", message)
                time.sleep(5)  # Debounce interval
    except KeyboardInterrupt:
        print("Terminating...")
    finally:
        ir.cleanup()

if __name__ == "__main__":
    main()
