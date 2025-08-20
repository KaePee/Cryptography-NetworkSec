import hashlib
import sys
import time

def hash_message(message: str) -> str:
    """Generate SHA-256 hash of a message."""
    return hashlib.sha256(message.encode()).hexdigest()

def mac_message(message: str, secret: str) -> str:
    """Generate SHA-256 hash of message+secret (simple MAC simulation)."""
    return hashlib.sha256((message + secret).encode()).hexdigest()

def regular_hash_flow(attacker_present: bool):
    # Sender always enters message first
    message = input("Sender: Enter the message to send ")
    sender_digest = hash_message(message)
    print(f"[Sender] Sending message: '{message}' with hash: {sender_digest}")

    if not attacker_present:
        # Receiver side
        print("\n[Receiver] Receiving message...")
        time.sleep(2)
        recv_digest = hash_message(message)
        print(f"[Receiver] Message: {message} with Computed hash: {recv_digest}")
        if recv_digest == sender_digest:
            print("[Receiver] ✅ Message is verified (no tampering detected).")
        else:
            print("[Receiver] ❌ Message has been tampered!")
    else:
        # Attacker intercepts and changes message
        attacker_msg = input("Attacker (hacker101): Enter a fake message to replace  ")
        attacker_digest = hash_message(attacker_msg)
        print(f"[Attacker] Replaced message with: '{attacker_msg}' and hash: {attacker_digest}")

        # Receiver side
        print("\n[Receiver] Receiving message...")
        time.sleep(2)
        recv_digest = hash_message(attacker_msg)
        print(f"[Receiver] Message: {message} with Computed hash: {recv_digest}")
        print("[Receiver] ✅ Message is verified (BUT it was from attacker!)")
        print("⚠️ Problem: Regular hash cannot detect attacker interception.")

def mac_hash_flow(attacker_present: bool):
    # Sender always enters message first
    message = input("Sender: Enter the message to send  ")
    secret = input("Sender: Enter the secret key  ")
    sender_digest = mac_message(message, secret)
    print(f"[Sender] Sending message: '{message}' with MAC: {sender_digest}")

    if not attacker_present:
        # Receiver side
        print("\n[Receiver] Receiving message...")
        time.sleep(2)
        recv_digest = mac_message(message, secret)
        print(f"[Receiver] Message: {message} with Computed MAC: {recv_digest}")
        if recv_digest == sender_digest:
            print("[Receiver] ✅ Message is verified (authentic and intact).")
        else:
            print("[Receiver] ❌ Message has been tampered!")
    else:
        # Attacker intercepts and changes message
        attacker_msg = input("Attacker: Enter a fake message to replace: ")
        fake_digest = mac_message(attacker_msg, "123456")  # attacker uses wrong key
        print(f"[Attacker] Replaced message with: '{attacker_msg}' and fake MAC: {fake_digest}")

        # Receiver side
        print("\n[Receiver] Receiving message...")
        time.sleep(2)
        recv_digest = mac_message(attacker_msg, secret)
        print(f"[Receiver] Message: {message} with Computed MAC: {recv_digest}")
        if recv_digest == fake_digest:
            print("[Receiver] ✅ Message is verified (authentic).")
        else:
            print("[Receiver] ❌ Message has been tampered or forged!")

def main():
    print("==== Secure Messaging Simulation ====")
    print("Choose mode:")
    print("1. Regular Hash")
    print("2. MAC-based Hash")

    choice = input("Enter choice (1 or 2): ")
    if choice not in ["1", "2"]:
        print("❌ Invalid choice. Exiting.")
        sys.exit()

    attacker = input("Is attacker present? (yes/no): ").lower()
    if attacker not in ["yes", "no"]:
        print("❌ Invalid choice. Exiting.")
        sys.exit()

    attacker_present = attacker == "yes"

    if choice == "1":
        print("\n=== Regular Hash Mode Selected ===")
        regular_hash_flow(attacker_present)
    else:
        print("\n=== MAC-based Hash Mode Selected ===")
        mac_hash_flow(attacker_present)

if __name__ == "__main__":
    main()
