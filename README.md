# 🔐 Cybersecurity & Network Tools Suite

Welcome to the **Cybersecurity & Network Tools Suite** — a Python-powered collection of utilities designed for ethical hacking, network scanning, API fuzzing, secure password management, XSS simulation, and more. Each tool demonstrates core cybersecurity concepts and modern web techniques.

---

## 🛠️ Tools Included

### 1. 🐞 API Fuzzer
Test and explore undocumented or hidden REST API endpoints using fuzzed inputs.

- **Tech Used**: `Python`, `requests`, `sys`
- 🔗 Targets example API: `https://jsonplaceholder.typicode.com/`
- 📌 Purpose: Discover valid endpoints and test API response behavior.

```bash
cat wordlist.txt | python3 api_fuzzer.py

### 2. 🌐 Flask Web App with Reflected XSS Demo

This project is a simple Flask-based web application designed to demonstrate **Reflected Cross-Site Scripting (XSS)** — a common web security vulnerability. It provides a hands-on environment to test how unsanitized user input can be exploited to inject malicious scripts.

🔐 **Use Case**: Ethical hacking practice, web security demos, educational purposes  
⚠️ **Note**: This app is intentionally vulnerable and should never be used in production environments.



