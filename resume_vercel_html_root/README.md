# Resume (Vercel-ready) — HTML at Root + Download PDF

- `index.html` lives at the **project root** and `{% extends 'base.html' %}` continues to work.
- `base.html` remains in `templates/`.
- Flask Jinja loader searches both locations.
- Serverless routing via `api/index.py` and `vercel.json`.

## Local
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py

## Deploy
npm i -g vercel
vercel
vercel --prod
