# API TODO - CI/CD

[![Multi-Env Deploy](https://github.com/MaelSouv/api-todo-ci/actions/workflows/deploy-multi-env.yml/badge.svg)](https://github.com/MaelSouv/api-todo-ci/actions/workflows/deploy-multi-env.yml)

API TODO avec déploiement automatique via GitHub Actions et Render.

## Fonctionnalités

- CRUD complet pour les todos
- Tests unitaires (9 tests)
- CI/CD automatique (Multi-environnement)
- Déploiement automatique sur Render

## API Déployée

**Production :** https://api-todo-ci-1-mael.onrender.com
**Staging :** https://api-todo-ci-mael-staging.onrender.com

## Endpoints

| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/` | Infos de l'API |
| GET | `/todos` | Liste tous les todos |
| GET | `/todos/:id` | Un todo spécifique |
| POST | `/todos` | Créer un todo |
| PUT | `/todos/:id` | Modifier un todo |
| DELETE | `/todos/:id` | Supprimer un todo |
| GET | `/health` | Status de l'API |
| GET | `/stats` | Statistiques de l'API |

## Exemples d'utilisation

### Récupérer tous les todos
```bash
curl https://api-todo-ci-1-mael.onrender.com/todos
```

### Statistiques (Staging)
```bash
curl https://api-todo-ci-mael-staging.onrender.com/stats
```

### Créer un todo
```bash
curl -X POST https://api-todo-ci-1-mael.onrender.com/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Apprendre le CI/CD"}'
```

### Health check
```bash
curl https://api-todo-ci-1-mael.onrender.com/health
```

## Développement Local
```bash
# Installer les dépendances
npm install

# Lancer le serveur
npm start

# Lancer les tests
npm test
```

## Pipeline CI/CD

Le pipeline s'exécute automatiquement à chaque push :

1. **Test** : Exécution des 9 tests unitaires
2. **Deploy Staging** : Déploiement sur Render (branche `develop`)
3. **Deploy Production** : Déploiement sur Render (branche `main`)
4. **Release** : Création automatique de Release sur tag `v*`

## Projet réalisé dans le cadre du cours CI/CD

**MyDigitalSchool - Janvier 2026**
