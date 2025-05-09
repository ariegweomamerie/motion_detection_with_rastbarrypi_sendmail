# 📷 Raspberry Pi Motion Detection System

This project uses a Raspberry Pi and an IR sensor to detect motion. When motion is detected, it:

- Logs the event (with timestamp) into an SQLite database
- Sends an email alert using SMTP

---

## 🛠️ Hardware Required

| Component          | Quantity |
|-------------------|----------|
| Raspberry Pi (any model with GPIO) | 1        |
| IR Motion Sensor (PIR)             | 1        |
| Jumper Wires                       | 3        |
| Breadboard (optional)             | 1        |
| Internet connection (for SMTP)    | 1        |

---

## ⚡ Wiring Diagram

IR Sensor Pin → Raspberry Pi GPIO
VCC → 5V
GND → GND
OUT → GPIO17 (BCM mode)