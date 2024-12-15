# 🧑‍💻 Directory Brute Force Script 🔓

This Python script is designed to perform a **directory brute-force attack** on a target website. It uses a wordlist to try various directory names on the target website, checking for common status codes like `200`, `403`, and `404`. This tool is useful for **penetration testing** and discovering hidden directories on web servers.

## 📑 Table of Contents
- [🔍 Overview](#overview)
- [💻 Requirements](#requirements)
- [🛠️ Usage](#usage)
- [⚙️ Customization](#customization)
- [⚖️ Disclaimer](#disclaimer)

## 🔍 Overview

The script performs a **directory brute-force attack** using the specified wordlist and checks the target website's response for valid directories. It is designed to handle common HTTP status codes:
- `✅ 200 OK`: Directory found.
- `⛔ 403 Forbidden`: Access to the directory is restricted.
- `❌ 404 Not Found`: Directory not found.

## 💻 Requirements

- 🐍 **Python 3.x**
- 📦 **requests** library (can be installed using `pip install requests`)

## 🛠️ Usage

1. **Clone or Download the Script**:
   - Download the Python script to your local machine.

2. **Prepare the Wordlist**:
   - The script uses a wordlist (`common.txt`) to try different directories. Ensure that your wordlist is present at the location specified in the script. If you want to use your own wordlist, update the `wordlist` variable in the script.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script with the following command:
   
     ```bash
     python directory_brute.py
     ```

4. **Input the Target Website URL**:
   - When prompted, enter the target website's URL (e.g., `http://example.com`).

5. **View Results**:
   - The script will output the response codes for each directory it tests (e.g., `✅ 200`, `⛔ 403`).

## ⚙️ Customization

- **Wordlist Location**: The script is set to use a wordlist located at `path/to/common,txt`. You can modify this path or update the wordlist to point to a different file.
  
- **Timeout**: The `timeout=5` in the `requests.get()` function can be adjusted to change the wait time before a request times out.

- **Error Handling**: The script includes basic error handling to ensure smooth operation. If the wordlist file is not found, or if there is an issue with the request, the script will print the error message.

## ⚖️ Disclaimer

This tool is intended for **ethical hacking** and **penetration testing** purposes only. Ensure that you have **permission** from the website owner before testing their website. Unauthorized access to computer systems is **illegal** and punishable by law.

---

🌟 **Contributions**: If you find this project useful, feel free to fork it, contribute, or open issues for improvements! ✨
