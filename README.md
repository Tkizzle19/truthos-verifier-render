# TruthOS Verifier 🧠

A symbolic claim analysis engine that scores input statements for consistency, entropy, contradiction, ambiguity, and symbolic coherence.

Built using Streamlit and spaCy. Easily deployable on [Render.com](https://render.com) with zero backend experience.

---

## 🚀 Features

- Truth scoring via FFT, entropy, and recursion logic
- Named Entity Recognition using spaCy
- Contradiction and ambiguity checks
- Clear verdict scale: `T`, `Δ`, `◬`, `?`, `⊗`, `⊘`
- Clean, user-friendly interface with Streamlit
- One-click deployment

---

## 📦 Folder Structure

```
.
├── app.py                # Streamlit frontend
├── upgraded_truthos.py  # Core TruthOS logic
├── requirements.txt      # Python dependencies
└── postBuild             # Render build script to install spaCy model
```

---

## 📥 Local Setup (Optional)

```bash
git clone https://github.com/YOUR_USERNAME/truthos-verifier.git
cd truthos-verifier
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

---

## ☁️ Render Deployment (No Code Needed)

1. Create a free account at [render.com](https://render.com)
2. Click **"New → Web Service"**
3. Connect your GitHub repo with this code
4. Set these options:
   - **Runtime:** Python 3
   - **Start Command:** `streamlit run app.py`
5. Wait ~1 min for it to build and run. That's it!

---

## 🧪 Verdict Scale

| Symbol | Meaning                                |
|--------|----------------------------------------|
| `T`    | High confidence truth                  |
| `Δ`    | Likely true, minor ambiguity           |
| `◬`    | Ideological contradiction detected     |
| `?`    | Unclear / Ambiguous                    |
| `⊗`    | Low coherence or symbolic inconsistency|
| `⊘`    | Logical contradiction / Hard falsehood |

---

## 🛠 Dependencies

- `streamlit`
- `spacy`
- `numpy`
- Python ≥ 3.8

---

## 📜 License

MIT License