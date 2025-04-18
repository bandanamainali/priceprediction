import nbformat

try:
    with open("housepriceprediction.ipynb", "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    print("✅ Notebook is valid!")
except Exception as e:
    print("❌ Invalid Notebook:", e) 