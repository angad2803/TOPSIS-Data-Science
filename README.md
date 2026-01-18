# Topsis-ANGAD-102313005

**TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) - A multi-criteria decision-making tool by **ANGAD SINGH MADHOK** (Roll 102313005).

---

## 1. 📋 Methodology

TOPSIS is a multi-criteria decision-making (MCDM) method that ranks alternatives based on their geometric distance from the ideal solution. The algorithm:

1. **Normalizes** the decision matrix using vector normalization
2. **Applies weights** to each criterion based on importance
3. **Identifies ideal best and worst** solutions for each criterion
4. **Calculates Euclidean distances** to ideal best and worst
5. **Computes relative closeness** (TOPSIS score: 0-1 range)
6. **Ranks alternatives** where Rank 1 = best choice

---

## 2. 📝 Description

This project provides both a **command-line tool** and a **web interface** for performing TOPSIS analysis. Users can:

- Upload CSV data with alternatives and multiple criteria
- Assign weights to reflect criterion importance
- Specify impacts (beneficial or cost) for each criterion
- Get ranked results with TOPSIS scores
- Download results or receive them via email

Built with NumPy for fast vectorized computations and Pandas for robust data handling.

---

## 3. 📥 Input / Output

### Input

- **CSV File**: First column = alternative names, remaining columns = numeric criteria values
- **Weights**: Comma-separated numbers (e.g., `2.3,1.7,3.1,0.9,2.6`)
- **Impacts**: Comma-separated `+` (beneficial) or `-` (cost) for each criterion (e.g., `+,-,+,-,+`)

### Output

- **CSV File**: Original data + two new columns:
  - `Topsis Score`: Relative closeness coefficient (0-1)
  - `Rank`: Ranking based on score (1 = best)

---

## 4. 🌐 Live Link

**🚀 Live Demo:** [https://topsis-data-science-bghplnmn7wfrzxw8hbepcc.streamlit.app/](https://topsis-data-science-bghplnmn7wfrzxw8hbepcc.streamlit.app/)

**Local Development:** Run `streamlit run app.py` → http://localhost:8501

---

## 5. 📸 Screenshot of Interface

![TOPSIS Web Interface](D:\TOPSIS\image.png)

---

## 📦 Repository

<https://github.com/angad2803/TOPSIS-Data-Science>

---

## 🚀 Installation & Setup

## 🚀 Installation & Setup

### Prerequisites

```bash
python >= 3.9
pip
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Web App (Streamlit)

```bash
streamlit run app.py
```

### Run CLI

```bash
python -m topsis_angad example_data.csv "2.3,1.7,3.1,0.9,2.6" "+,-,+,-,+" output.csv
```

---

## 📋 Usage Examples

## � Usage Examples

### Example Data (example_data.csv)

```csv
Fund Name,P1,P2,P3,P4,P5
Alpha,0.72,0.51,5.8,38.4,11.23
Beta,0.58,0.41,4.2,47.6,13.85
Gamma,0.79,0.63,4.5,58.7,15.92
```

### Command

```bash
python -m topsis_angad example_data.csv "2.3,1.7,3.1,0.9,2.6" "+,-,+,-,+" result.csv
```

### Result

| Fund Name | P1   | P2   | P3  | P4   | P5    | Topsis Score | Rank |
| --------- | ---- | ---- | --- | ---- | ----- | ------------ | ---- |
| Zeta      | 0.66 | 0.46 | 6.1 | 52.9 | 13.45 | 0.6216       | 1    |
| Eta       | 0.81 | 0.59 | 5.1 | 55.8 | 14.98 | 0.5669       | 2    |
| Alpha     | 0.72 | 0.51 | 5.8 | 38.4 | 11.23 | 0.5337       | 3    |

---

## 🚀 Deployment

### Streamlit Cloud

1. Push to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy `app.py`

### Render / Heroku

Use `requirements.txt` and set start command:

```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

---

If using the web service (topsis_web.py), create a `.env` file in the project root:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**Never commit your .env file!**

## 🐍 Publishing to PyPI

Build and upload:

```bash
python -m build
python -m twine upload dist/*
```

Test install:

```bash
pip install Topsis-ANGAD-102313005
topsis-cli --help
```

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 👤 Author

ANGAD SINGH MADHOK - Roll No. 102313005
