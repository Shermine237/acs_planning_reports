# Guide d'Installation - ACS Planning Reports Extension

## Prérequis

Avant d'installer ce module, assurez-vous que les modules suivants sont installés et configurés :

1. **acs_planning** - Module de planification des employés par AlmightyCS
2. **site_ange_security** - Module de gestion des sites
3. **hr** - Module de gestion des ressources humaines (Odoo standard)

## Étapes d'Installation

### 1. Copier le module

Copiez le dossier `acs_planning_reports` dans le répertoire des addons de votre instance Odoo :

```bash
# Exemple de chemin
/opt/odoo/custom-addons/acs_planning_reports
```

### 2. Mettre à jour la liste des modules

1. Connectez-vous à Odoo en tant qu'administrateur
2. Activez le mode développeur :
   - Allez dans **Paramètres**
   - En bas de page, cliquez sur **Activer le mode développeur**

3. Mettez à jour la liste des applications :
   - Allez dans **Applications**
   - Cliquez sur le menu (☰) en haut à gauche
   - Sélectionnez **Mettre à jour la liste des applications**

### 3. Installer le module

1. Dans le menu **Applications**, recherchez "ACS Planning Reports"
2. Cliquez sur **Installer**
3. Attendez la fin de l'installation

## Vérification de l'Installation

### Vérifier les Smart Buttons

#### Dans le formulaire Employé :
1. Allez dans **Employés**
2. Ouvrez la fiche d'un employé qui a des plannings
3. Vous devriez voir un smart button **Planning** avec le nombre de plannings

#### Dans le formulaire Site :
1. Allez dans **Sites**
2. Ouvrez la fiche d'un site avec des agents affectés
3. Vous devriez voir un smart button **Plannings** avec le nombre total de plannings

### Vérifier les Rapports

#### Rapport Planning Employé :
1. Ouvrez la fiche d'un employé
2. Cliquez sur le menu **Imprimer** (icône imprimante)
3. Sélectionnez **Planning Agent**
4. Un PDF devrait se télécharger avec le planning de l'employé

#### Rapport Planning Site :
1. Ouvrez la fiche d'un site
2. Cliquez sur le menu **Imprimer**
3. Sélectionnez **Planning Site**
4. Un PDF devrait se télécharger avec les plannings de tous les agents du site

## Dépendances Techniques

Le module dépend des modèles suivants :

- `hr.employee` - Employés
- `hr.employee.public` - Employés (vue publique)
- `site.site` - Sites
- `acs.planning` - Plannings
- `acs.planning.request` - Demandes de planning

## Droits d'Accès

Par défaut, tous les utilisateurs peuvent :
- Lire les plannings
- Générer les rapports PDF

Les droits d'écriture, création et suppression sont hérités du module `acs_planning`.

## Personnalisation

### Modifier les Rapports

Les templates de rapport se trouvent dans :
- `reports/employee_planning_report.xml` - Rapport employé
- `reports/site_planning_report.xml` - Rapport site

Vous pouvez les personnaliser en créant des modules héritant de ces templates.

### Ajouter des Champs

Pour ajouter des champs dans les rapports :

1. Étendez les modèles dans `models/hr_employee.py` ou `models/site.py`
2. Ajoutez les champs dans les templates XML
3. Mettez à jour le module

## Dépannage

### Le smart button n'apparaît pas

**Cause** : Aucun planning n'existe pour l'employé/site
**Solution** : Créez au moins un planning pour voir apparaître le bouton

### Erreur lors de la génération du PDF

**Cause** : Problème avec wkhtmltopdf
**Solution** : 
```bash
# Installer wkhtmltopdf
sudo apt-get install wkhtmltopdf
```

### Les données ne s'affichent pas dans le rapport

**Cause** : Problème de droits d'accès
**Solution** : Vérifiez que l'utilisateur a les droits de lecture sur les modèles acs.planning

### Erreur "Module not found"

**Cause** : Le module parent n'est pas installé
**Solution** : Installez d'abord `acs_planning` et `site_ange_security`

## Désinstallation

Pour désinstaller le module :

1. Allez dans **Applications**
2. Recherchez "ACS Planning Reports"
3. Cliquez sur **Désinstaller**

**Note** : Cela ne supprimera pas les données de planning, seulement les rapports et smart buttons.

## Support

Pour toute question ou problème :
- Consultez la documentation du module
- Contactez votre administrateur système
- Vérifiez les logs Odoo pour les erreurs détaillées

## Changelog

### Version 18.0.1.0.0
- Version initiale
- Rapport PDF planning employé
- Rapport PDF planning site
- Smart buttons dans formulaires employé et site
- Statistiques de plannings
