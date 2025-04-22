# Musulmon.uz

> **Qu'ron oyatlari tarjimasi va Namoz vaqtlari**

A Django web‑app for searching and displaying Quran verses (with audio recitations), calculating prayer times, and tracking qazo (missed prayers) for major cities in Uzbekistan. Originally deployed on PythonAnywhere (no longer active), this project can be redeployed on any Django‑compatible hosting platform.

---

## 🌟 Features

- **Quran Search & Translation**: Lookup by sura name or number; view text and translation.
- **Audio Recitation**: Play recitation for each ayah directly in the browser.
- **Prayer Times**: Fetch and display daily prayer times for selected Uzbek cities.
- **Qazo Tracker**: Mark and count missed prayers (qazo) per time period.
- **Autocomplete Search**: Instant suggestions powered by a JSON surahs list.
- **Responsive Design**: Built with Semantic UI, custom CSS/LESS, and vanilla JS.

---

## 🛠 Tech Stack

- **Backend**: Django 4.x, Python 3.9+
- **Database**: SQLite3 (development); easily swap with PostgreSQL for production
- **Templating**: Django Templates
- **Frontend**: HTML5, CSS/LESS, Semantic UI, jQuery
- **Static Files**: Managed via `static/` and `staticfiles/` folders
- **Audio**: HTML5 `<audio>` element sourcing MP3 URLs
- **Deployment**: PythonAnywhere (legacy), alternative: Heroku/Gunicorn + Whitenoise

---

## 🚀 Quickstart

1. **Clone & enter project**
   ```bash
   git clone https://github.com/habiboffdev/Musilman.uz.git
   cd Musilman.uz
   ```
2. **Create & activate virtualenv**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: `venv\\Scripts\\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install pipenv
   pipenv install --dev
   ```
4. **Configure environment**
   - Copy `.env.example` to `.env` and set:
     ```env
     SECRET_KEY=your_django_secret
     DEBUG=True
     ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
     ```
5. **Apply migrations & run**
   ```bash
   pipenv run python manage.py migrate
   pipenv run python manage.py runserver
   ```
6. **Access in browser**: `http://127.0.0.1:8000/`

---

## ⚙️ Configuration

- **Cities & Times**: Defined in `views.py`; extend `city_list` for new locations.
- **Surah Data**: `templates/base.html` loads `templates/static/surahslist.json` for search.
- **Audio URLs**: Provided in `search` view mapping ayah numbers to MP3 links.

---

## 🐛 Troubleshooting PythonAnywhere

> _Deployment is no longer live on PythonAnywhere._ To redeploy:

1. Ensure **Python version** matches (3.9+) and install requirements.
2. Configure **WSGI file** to point at `config.wsgi`.
3. Collect static files: `python manage.py collectstatic` and set `STATIC_ROOT`.
4. Add your domain to **ALLOWED_HOSTS**.
5. Check file permissions and reload the web app.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m "Add <feature>"
4. Push: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📜 License

This project is MIT licensed. See [LICENSE](LICENSE) for details.

---

_Last updated: April 22, 2025_

