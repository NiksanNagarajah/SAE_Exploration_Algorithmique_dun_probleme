import requetes as req

#Voici le ficiher test pour les fonctions nécessitant des vérifications (avec le fichier créé réduit pour accélérer le temps des tests -> "./data_100.json"):

# tests collaborateurs_communs
G = req.json_vers_nx("./donnees/data_100.json")

def test_collaborateurs_communs():
    assert req.collaborateurs_communs(G, "Edward Grover", "Bernard Barrow") == {'Ted Beniades', 'M. Emmet Walsh', 'Barbara Eda-Young', 'Al Pacino', 'Joseph Bova', 'Tony Roberts', 'F. Murray Abraham', 'Allan Rich', 'John Randolph', 'Woodie King Jr.', 'James Tolkan', 'Nathan George', 'Biff McGuire', 'Cornelia Sharpe', 'Albert Henderson', 'Jack Kehoe', 'Judd Hirsch'}
    assert req.collaborateurs_communs(G, "Charles Durning", "Robert Duvall") == {'Teri Garr', 'Richard Bright', 'John Cazale', 'Robert De Niro', 'Allen Garfield', 'Gene Hackman', 'John Travolta', 'Al Pacino', 'Robert Redford', 'Michael Higgins', 'Dominic Chianese', 'James Caan'}
    assert req.collaborateurs_communs(G, "Daryl Hannah", "Hy Pyke") is None
    assert req.collaborateurs_communs(G, "Melvyn Douglas", "Allen Garfield") == {'Charles Durning'}
    assert req.collaborateurs_communs(G, "Floyd L. Peterson", "Bruce D. Price") == {'Paul Hirsch', 'Jennifer Salt', 'Lara Parker', 'Allen Garfield', 'Paul Bartel', 'Gerrit Graham', 'Andy Parker', 'Ricky Parker', 'Robert De Niro', 'Charles Durning', 'Joseph King'}

# tests collaborateurs_proches

def test_collaborateurs_proches():
    assert req.collaborateurs_proches(G, "Rutger Hauer", 3) is None
    assert req.collaborateurs_proches(G, "Diane Venora", 1) == {'Rip Torn', 'Kim Staunton', 'Ray Buktenica', 'Natalie Portman', 'Tom Sizemore', 'Philip Baker Hall', 'William Fichtner', 'Kevin Gage', 'Henry Rollins', 'Gary Sandy', 'Gina Gershon', 'Bruce McGill', 'Ashley Judd', 'Jerry Trimble', 'Amy Brenneman', 'Al Pacino', 'Cliff Curtis', 'Danny Trejo', 'Mike Moore', 'Robert De Niro', 'Dennis Haysbert', 'Xander Berkeley', 'Colm Feore', 'Tom Noonan', 'Russell Crowe', 'Mykelti Williamson', 'Ted Levine', 'Jeremy Piven', 'Tone Loc', 'Debi Mazar', 'Lindsay Crouse', 'Jack Palladino', 'Stephen Tobolowsky', 'Val Kilmer', 'Christopher Plummer', 'Hallie Kate Eisenberg', 'Diane Venora', 'Michael Gambon', 'Hank Azaria', 'Jon Voight', 'Roger Bart', 'Ricky Harris', 'Wes Studi', 'Renee Olstead', 'Susan Traylor'}
    assert req.collaborateurs_proches(G, "Robert MacLeod", 0) == {"Robert MacLeod"} 
    assert req.collaborateurs_proches(G, "Jay Mohr", 1) == {'Winona Ryder', 'Jason Schwartzman', 'Pruitt Taylor Vince', 'Elias Koteas', 'Catherine Keener', 'Rebecca Romijn', 'Joel Heyman', 'Evan Rachel Wood', 'Jay Mohr', 'Rachel Roberts', 'Kelly Anna Cox', 'Al Pacino'}
    assert req.collaborateurs_proches(G, "Ken Baker", 1) is None
   
# tests est_proche

def test_est_proche():
    assert req.est_proche(G, "Diane Venora", "Philip Baker Hall") is True
    assert req.est_proche(G, "Jay Mohr", "Al Pacino") is True
    assert req.est_proche(G, "Michael P. Moran", "Mary Davenport") is False
    assert req.est_proche(G, "Catherine Gaffigan", "Julia Stiles") is False
    assert req.est_proche(G, "Vicki Wauchope", "Dave Goelz") is False

# tests distance_proche

def test_distance_naive():
    assert req.distance_naive(G, "Rutger Hauer", "Sean Young") is None #un ou plusieurs acteurs n'existent pas dans le graphe
    assert req.distance_naive(G, "Elliott Gould", "Elliott Gould") == 0
    assert req.distance_naive(G, "Randi Brooks", "Milton Berle") == 2
    assert req.distance_naive(G, "Charles Durning", "Dom DeLuise") == 1
    assert req.distance_naive(G, "Sam Raimi", "Anne Francis") == 3

# tests distance

def test_distance():
    assert req.distance(G, "Rutger Hauer", "Sean Young") is None
    assert req.distance(G, "Donnie Wahlberg", "James Broderick") == 2
    assert req.distance(G, "Judy Tucker", "Marcia Jean Kurtz") == 2
    assert req.distance(G, "Neal McDonough", "Neal McDonough") == 0 #ce sont les mêmes acteurs donc la distance est à 0
    assert req.distance(G, "Ben McKenzie", "Elizabeth Hubbard") == 3 

    assert req.distance(G, "Elliott Gould", "Elliott Gould") == 0
    assert req.distance(G, "Randi Brooks", "Milton Berle") == 2
    assert req.distance(G, "Charles Durning", "Dom DeLuise") == 1
    assert req.distance(G, "Sam Raimi", "Anne Francis") == 3

# tests centralite

def test_centralite():
    assert req.centralite(G, "John Hofman") is None #il n'existe pas dans le graphe
    assert req.centralite(G, "Robert Gerringer") == 3
    assert req.centralite(G, "Richard Cox") == 3
    assert req.centralite(G, "Gene Hackman") == 3
    assert req.centralite(G, "Al Pacino") == 2

# tests centre_hollywood

def test_centre_hollywood():
    assert req.centre_hollywood(G) == "Al Pacino"
    assert req.centre_hollywood(G) != "Robert De Niro"

# tests  eloignement_max

def test_eloignement_max():
    assert req.eloignement_max(G) == 3
    # assert req.eloignement_max(req.json_vers_nx("./data.json")) == ??? # Trop long, essayer à l'IUT

### Attention la visualisation est graphe ne fonctionne pas. A remédier

