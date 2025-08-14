
# CIDR2IP

**CIDR2IP** is a multi-threaded Python tool for expanding CIDR ranges into full lists of IP addresses.  
It supports both single CIDR input and bulk CIDR lists from a file, with output saved to your chosen directory.

---

## 🚀 Features
- 🔹 **Multi-threaded processing** for speed.
- 🔹 Accepts **single CIDR** or **CIDR list file**.
- 🔹 Saves results to a text file in a chosen directory.
- 🔹 Automatically creates output directories.
- 🔹 ASCII banner for a professional look.

---

## 📦 Requirements
Python 3.x (Tested on Python 3.8+)

No external libraries required — it uses Python's built-in:
- `ipaddress`
- `os`
- `concurrent.futures`

---

## 📥 Installation
```bash
git clone https://github.com/NightfallSecDev/CIDR2IP.git
cd CIDR2IP
````

---

## 💻 Usage

### **Single CIDR Mode**

```bash
python3 cidr2ip.py
```

* Select **1** when prompted.
* Enter a CIDR (e.g., `202.44.112.0/22`).
* Choose an output directory.
* The tool will generate all usable IPs and save them.

### **Multiple CIDRs from File**

```bash
python3 cidr2ip.py
```

* Select **2** when prompted.
* Provide a file path with CIDRs (one per line).
* Choose an output directory.
* The tool will process all CIDRs in parallel.

Example CIDR file (`cidrs.txt`):

```
202.44.112.0/22
192.168.0.0/24
10.0.0.0/30
```

---

## 📂 Output

* The tool saves IPs in `ip_list.txt` inside your chosen output directory.
* Only usable host addresses are included (no network or broadcast).

---

## 📜 License

MIT License – free to use and modify.

---

## ✨ Credits

Created by **NightfallSecDev**.

```


