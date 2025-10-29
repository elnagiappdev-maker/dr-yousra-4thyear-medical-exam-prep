# Quick Start Guide

Get the Medical Exam Prep app running in 5 minutes!

## Option 1: Automated Setup (Recommended)

```bash
# Make setup script executable (if not already)
chmod +x setup.sh

# Run the setup script
./setup.sh

# Activate virtual environment
source venv/bin/activate

# Run the app
streamlit run app.py
```

Open your browser to: **http://localhost:8501**

## Option 2: Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open your browser to: **http://localhost:8501**

## Option 3: Docker

```bash
# Using Docker Compose
docker-compose up --build
```

Open your browser to: **http://localhost:8501**

## Option 4: Deploy to Streamlit Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository
5. Set main file: `app.py`
6. Click "Deploy"

Your app will be live at: `https://[username]-[repo]-[branch].streamlit.app`

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8501
lsof -i :8501
kill -9 <PID>
```

### Dependencies Not Installing
```bash
# Upgrade pip first
pip install --upgrade pip
pip install -r requirements.txt
```

### Python Version Issues
Make sure you have Python 3.8 or higher:
```bash
python3 --version
```

## What's Included

- 📚 **123 Medical Questions** across 6 systems
- 📝 **60 SBA Questions** with detailed explanations
- 📋 **60 MCQ Questions** with answer keys
- 🔬 **3 EMQ Question Sets** with clinical scenarios
- 📖 **24 Study Notes** for quick revision

## Need Help?

- Check **README.md** for detailed documentation
- See **DEPLOYMENT.md** for deployment options
- Review **FIXES.md** to see what was fixed
- Open an issue on GitHub

---

**Ready to study? Run the app and start preparing for your exams!** 🎓
