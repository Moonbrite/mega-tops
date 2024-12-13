<h1 align="center"><strong>Mega-Tops Burger</strong></h1>
<h2>Index</h2>
<p>1. Description du projet</p>
<p>2. Fonctionnalités principales</p>
<p>3. Approche de développement</p>
<p>4. Scénario de démonstration</p>
<p>5. Livrables attendus</p>
<p>6. Installation et utilisation</p>
<p>7. Contributeurs</p>

<h2>1. Description du projet</h2>
<p>Mega-Tops Burger, un restaurant de taille moyenne, souhaite moderniser la gestion de ses commandes pour offrir une meilleure expérience client et améliorer l'efficacité de son personnel. Actuellement, les commandes sont prises sur papier, ce qui entraîne des retards en cuisine, des erreurs et des difficultés pour gérer les factures et les stocks.</p>
<p>Ce projet vise à développer une application intuitive permettant de centraliser et de simplifier la gestion des commandes, depuis leur prise jusqu'au paiement.</p>

<h2>2. Fonctionnalités principales</h2>
<p><strong>1. Prise de commandes sur tablettes ou smartphones</strong></p>
<p>Les serveurs peuvent enregistrer les commandes directement sur un appareil numérique.</p>
<p><strong>2. Transmission en temps réel</strong></p>
<p>Les commandes sont envoyées instantanément à la cuisine.</p>
<p><strong>3. Calcul automatique des factures</strong></p>
<p>Le total est calculé automatiquement avec taxes et remises éventuelles.</p>
<p><strong>4. Gestion des stocks</strong></p>
<p>Les ingrédients sont d´écrémentés en fonction des plats commandés.</p>
<p><strong>5. Rapports journaliers</strong></p>
<p>Génère un résumé des ventes quotidiennes.</p>

<h2>3. Approche de développement</h2>
<p><strong>1. Compréhension et analyse du besoin</strong></p>
<p>Discussion d'équipe : Identifier les problémetiques et besoins.</p>
<p>Diagrammes UML : Création d'un diagramme de cas d'utilisation.</p>
<p><strong>2. Conception et architecture</strong></p>
  <p>Base de données : </p>
    <li>Table : id, numéro, état</li>
    <li>Commande : id, table_id, statut, montant, payé</li>
    <li>Stock : id, ingrédient_id, quantité</li>
    <li>Plat_Commandé : id, plat_id, commande_id, quantité</li>
    <li>Custom_Plat_Commandé : id, custom_plat_id, commande_id, quantité</li>
    <li>Ingrédient : id, name</li>
    <li>Plat : id, name, description</li>
    <li>Custom_Plat : id, name</li>
    <li>Custom_Plat_Ingrédient : id, custom_plat_id, ingredient_id</li>
    <li>Plat_Ingrédient : id, plat_id, ingredient_id</li>
<br>
<p>Interfaces utilisateur : Conception de maquettes haute fidélité sur Figma</p>

<p><strong>3. Développement</strong></p>
<p>Implémentation de la version 1 sans interface utilisateur graphique.</p>

<h2>4. Scénario de démonstration</h2>
<p>1. Un serveur prend une commande pour une table (3 clients).</p>
<p>2. La commande inclut des plats personnalisés.</p>
<p>3. Les cuisiniers reçoivent la commande en temps réel et la marquent comme "Prête".</p>
<p>4. Le serveur génère la facture et consulte les stocks restants en fin de journée.</p>

<h2>5. Livrables attendus</h2>
  <li>Diagrammes UML pour la conception.</li>
  <li>Code source de l'application.</li>
  <li>Instructions d'installation et d'utilisation (README).</li>
  <li> Démonstration avec un scénario réaliste.</li>

<h2>6. Installation et utilisation</h2>
<p><strong>Prérequis</strong></p>
  <li>Python 3.12.3</li>
  <li>Base de données : MySQL</li>
<br>

<p><strong>Instructions</strong></p>

  <ul>1. Cloner le dépôt :</ul>
  <p>bash</p>
  <strong>git clone https://github.com/nom-utilisateur/mega-tops-burger.git</strong>
<br>
<br>
  <ul>2. Installer les dépendances :</ul>
  <strong>pip install -r requirements.txt  </strong>
<br>  
<br>
  <ul>3. Configurer la base de données : </ul>
    <li>Modifier le fichier config.py avec les informations de connexion pour MySQL.</li>
    <li>Initialiser la base de données : </li>
    <strong>python init_db.py </strong> 
<br>
<br>
  <ul>4. Lancer l'application :</ul>
  <strong>python app.py </strong> 
  

<h2>7. Contributeurs</h2>
<li>Fouziya Koudanne</li>
<li>Équipe de développement : José Miguel  Vale Costa, Sébastien Reynaud, Moukhammad Otcherkhadjiev, Rejda Qati, Maria del Mar Sevilla Escobar</li>
  
