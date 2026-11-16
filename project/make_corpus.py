"""Build a synthetic support-reply corpus (raw.txt) with PII, then clean it (corpus.txt).
Synthetic on purpose: no real customer data is used."""
import random, re
from pathlib import Path

HERE = Path(__file__).parent
rng = random.Random(0)

OPEN = ["Thanks for contacting us", "Thank you for reaching out", "Sorry for the trouble", "I am sorry to hear that",
        "Thanks for your patience", "Happy to help you today"]
BODY = [
    "I have checked order {o} and it will ship within two business days",
    "I have checked order {o} and it was delivered yesterday",
    "Your refund for order {o} has been issued and should appear in five days",
    "I can see order {o} is delayed and I have escalated it to the warehouse team",
    "Please reply to {e} with a photo of the damaged item",
    "I have sent a return label to {e} so you can send the item back",
    "You can reach us on {p} if you need anything else",
    "I have updated the delivery address on order {o}",
    "Your replacement for order {o} will arrive next week",
    "I have applied a discount to your next order as an apology",
]
CLOSE = ["Let me know if there is anything else I can do", "Please let us know if you have any other questions",
         "Have a great day", "We appreciate your business", "Thanks again for shopping with us"]

def pii(s):
    return s.format(o=f"#{rng.randint(10000, 99999)}", e=f"user{rng.randint(1, 99)}@example.com",
                    p=f"555-{rng.randint(100, 999)}-{rng.randint(1000, 9999)}")

def clean(text):
    "Anonymize and normalise: mask emails, phones, order ids; lowercase; collapse spaces."
    text = re.sub(r"\S+@\S+", "emailaddr", text)
    text = re.sub(r"\b\d{3}-\d{3}-\d{4}\b", "phonenum", text)
    text = re.sub(r"#\d+", "orderid", text)
    return re.sub(r"\s+", " ", text).strip().lower()

if __name__ == "__main__":
    raw = [pii(f"{rng.choice(OPEN)}. {rng.choice(BODY)}. {rng.choice(CLOSE)}.") for _ in range(400)]
    (HERE / "raw.txt").write_text("\n".join(raw))
    out = "\n".join(clean(r) for r in raw)
    (HERE / "corpus.txt").write_text(out)
    assert not re.search(r"@|#\d|\d{3}-\d{3}", out)  # no PII left
    print("raw:", len(raw), "lines | cleaned corpus:", len(out.split()), "tokens")
