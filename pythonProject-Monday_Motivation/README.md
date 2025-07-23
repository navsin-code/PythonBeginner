# Monday Motivation Email Sender 💌

## Features ✨
- **Automated Weekly Email**: Sends a motivational quote every Monday.
- **Random Quote Selection**: Picks one quote from a local `quotes.txt` file.
- **Secure Email Sending**: Uses `smtplib` and TLS encryption to send email via Gmail's SMTP server.
- **Scheduled Behavior**: Sends the email only if the current day is Monday.

## Installation 🛠️
1. Ensure Python 3.x is installed.
2. Enable **"Less secure app access"** or create an **App Password** for your Gmail account.
3. Place the following in the same directory:
   - `quotes.txt` — a file containing motivational quotes, one per line.
   - `motivation_email.py` — your script file.

4. Install no external libraries; this script uses built-in Python modules:
   - `smtplib`
   - `datetime`
   - `random`

## Usage 🚀
1. Save the code in a file (e.g. `motivation_email.py`).
2. Add your Gmail address and an **App Password** (not your real Gmail password) in the script:
   ```python
   my_email = "your_email@gmail.com"
   password = "your_app_password"

3. Run the script manually:

   ```bash
   python motivation_email.py
   ```
4. Or schedule it to run every Monday using a task scheduler:

   * **Windows**: Task Scheduler
   * **macOS/Linux**: `cron`

## How It Works 🧩

* The script gets the current day using `datetime.datetime.now().weekday()`, where Monday is `0`.
* If it’s Monday, it:

  * Reads a random quote from `quotes.txt`.
  * Connects to Gmail's SMTP server on port 587 using `smtplib.SMTP`.
  * Secures the connection with `starttls()`, logs in, and sends an email to the recipient.
* The subject line is **"Motivational Quote"** and the body contains the selected quote.
* The script uses a `with` block to auto-close the SMTP connection after sending the email.


