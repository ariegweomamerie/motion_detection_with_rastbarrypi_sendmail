#  Raspberry Pi Motion Detection with Email Alerts + SQLite Logging

This project enables a Raspberry Pi to detect motion using an IR sensor, log events into a local SQLite database, and send real-time email alerts when motion is detected. Ideal for basic home security or IoT monitoring systems.

---

## 🛠️ Features

- 🔍 Motion detection using an IR sensor
- 📬 Sends email notifications via SMTP
- 🗃️ Logs motion events to a local SQLite database
- 📅 Timestamped records for every event
- 🐍 Built with Python 3

---

## 💡 How It Works

1. IR sensor detects motion.
2. Event is logged in `motion_data.db`.
3. Email alert is sent to the configured recipient.

---

## 📁 Project Structure

oma_project/
├── motion_detection.py # Main script for sensor detection and alert
├── email_utils.py # Handles SMTP email configuration and sending
├── database_utils.py # SQLite functions (create table, insert event)
├── motion_data.db # SQLite database storing events
├── README.md # Project overview

---

## 🧰 Requirements

- Raspberry Pi (any model with GPIO)
- IR motion sensor (PIR)
- Python 3.x
- Internet connection (for sending emails)

### Python Libraries:

Install dependencies using:

pip install smtplib sqlite3 RPi.GPIO
(Note: smtplib and sqlite3 are built-in with Python, no extra install usually needed)

🚀 Setup & Usage
Clone the repository:


git clone git@github.com:ariegweomamerie/motion_detection_with_rastbarrypi_sendmail.git
cd motion_detection_with_rastbarrypi_sendmail
Configure email credentials in email_utils.py:

EMAIL_ADDRESS = "youremail@example.com"
EMAIL_PASSWORD = "your_app_password"
Use an App Password if using Gmail.

Run the script:

python3 motion_detection.py
🧪 Example Output
bash
Copy
Edit
Motion detected!
Event logged at 2025-05-07 18:00
Email sent to you@example.com
📜 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Omamerie Ariegwe
📧 ariegweomamerie@gmail.com
