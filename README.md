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
