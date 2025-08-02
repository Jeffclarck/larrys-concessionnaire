
# Larry's Concessionnaire 🚗

Projet Flask hébergeable sur Render, permettant d'ajouter des véhicules et générer automatiquement des fiches HTML.

## Démarrage local
```bash
pip install -r requirements.txt
python app.py
```

## Déploiement Render
- Connecte ce dossier à un dépôt GitHub
- Va sur https://render.com
- Crée un nouveau Web Service
- Render détectera `render.yaml` et déploiera automatiquement

## Structure
- `app.py` : serveur Flask
- `generate_fiches()` intégré pour créer les fiches
- `vehicules.json` : base de données
- `static/interface.html` : interface web
- `vehicules/` : fiches générées automatiquement
