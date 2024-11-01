source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init 
API_URL=https://link-bio-if4n.onrender.com reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate