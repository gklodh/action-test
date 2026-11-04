# ColorBurst 🎨

A colorful, animated Flask webapp — glassmorphism cards, floating gradient
orbs, rainbow text, and a working contact form.

## Project structure
```
colorburst/
├── app.py               # Flask application (routes + form handling)
├── requirements.txt     # Python dependencies
├── Procfile             # Deployment command (Heroku / Render / Railway)
├── runtime.txt          # Python version
├── templates/
│   ├── base.html        # Shared layout (nav + footer)
│   ├── index.html       # Home page
│   ├── features.html    # Features page
│   ├── about.html       # About page
│   ├── contact.html     # Contact form (GET/POST)
│   └── 404.html         # Custom error page
└── static/
    ├── css/style.css    # All styles & animations
    └── js/main.js       # Small interactive touches
```

## Run locally
```bash
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000
```

## Deploy
1. **Render / Railway** — push this folder to GitHub, create a new Web
   Service, build command `pip install -r requirements.txt`,
   start command `gunicorn app:app`.
2. **Heroku** — `git push heroku main` (Procfile is included).
3. **Any VPS** — `gunicorn -w 4 -b 0.0.0.0:8000 app:app`.

Remember to change `app.secret_key` before going live!

## Making it accessible from other machines

The dev server (`python app.py`) only listens on localhost. Pick one:

### Option 1 — Quick test on your LAN (1 minute)
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
Others on the same network open `http://<your-LAN-IP>:8000`.
(Find your IP: `ip addr` on Linux, `ipconfig` on Windows.)

### Option 2 — Free public hosting (recommended, no server needed)
- **Render** — https://render.com → New Web Service → connect GitHub repo.
  Build: `pip install -r requirements.txt` · Start: `gunicorn app:app`
  You get a free HTTPS URL like `https://colorburst.onrender.com`.
- **Railway** — https://railway.app → Deploy from GitHub (Procfile auto-detected).
- **PythonAnywhere** — upload files, create a Flask web app pointing at `app.py`.

### Option 3 — Temporary public URL from your own machine
```bash
pip install pyngrok
ngrok http 8000        # gives you a https://xyz.ngrok.io URL
# or: cloudflared tunnel --url http://localhost:8000
```

### Option 4 — Your own VPS (full control, production-grade)
```bash
# 1. On the server
sudo apt install python3-venv nginx
sudo mkdir -p /var/www/colorburst && sudo chown $USER /var/www/colorburst
cd /var/www/colorburst
python3 -m venv venv && source venv/bin/activate
# copy your project files here, then:
pip install -r requirements.txt

# 2. Run as a background service
sudo cp deploy/colorburst.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now colorburst

# 3. Put nginx in front (port 80, static files, stability)
sudo cp deploy/nginx.conf /etc/nginx/sites-available/colorburst
sudo ln -s /etc/nginx/sites-available/colorburst /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```
Open `http://your-server-ip` from any browser. Add HTTPS later with
`sudo apt install certbot python3-certbot-nginx && sudo certbot --nginx`.

### Firewall note
If the server has a firewall, allow the port:
```bash
sudo ufw allow 80        # nginx
sudo ufw allow 8000      # direct gunicorn, if not using nginx
# cloud servers (AWS/GCP): also open the port in the security group / VPC rules
```
