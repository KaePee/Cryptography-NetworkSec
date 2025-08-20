# 🔐 Message Authentication Simulation

This project is a simple Python simulation that demonstrates **message authentication** using two different approaches:

1. **Regular Hashing (SHA-256)**  
2. **Message Authentication Code (MAC)**  

The simulation shows how an attacker can intercept and tamper with messages, and why **MAC provides stronger protection** compared to a basic hash.

---

## 📖 How It Works

When you run the program, you will:

1. **Choose a mode**  
   - `1` -> Regular Hash (only hashing the message)  
   - `2` -> MAC-based Hash (message + secret key)  

2. **Choose if an attacker is present**  
   - `yes` -> Attacker intercepts and replaces the message  
   - `no` -> Message is sent directly to the receiver  

3. **Sender enters the message**  
   - The program shows the message and its hash/MAC.  

4. **Attacker (if present)**  
   - Can replace the message and generate a fake hash/MAC.  

5. **Receiver**  
   - Recomputes the hash/MAC and checks authenticity.  
   - With regular hashing: attacker goes undetected ❌  
   - With MAC: attacker is caught unless they know the secret key ✅  

---

## 🛠️ Requirements

- Python 3.7+  
- No external dependencies

---

## 🚀 Running the Program

Clone the repository and run:

```bash
cd hash_mac
python hash_mac_simulation.py
```