import requests

# Step 1: Upload PDF
with open("C:/Users/shekh/Downloads/sample.pdf", "rb") as f:
    res = requests.post(
        "http://127.0.0.1:5000/upload",
        files={"file": f}
    )
    print("Upload Response:", res.json())

# Step 2: Ask Question
res = requests.post(
    "http://127.0.0.1:5000/ask",
    json={"question": "What is AI?"}
)

print("Answer Response:", res.json())