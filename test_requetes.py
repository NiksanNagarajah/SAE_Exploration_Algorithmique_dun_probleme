import requetes as req

#Voici le ficiher test pour les fonctions nécessitant des vérifications (avec le fichier créé réduit pour accélérer le temps des tests -> "./data_100.json"):

# tests collaborateurs_communs

def test_collaborateurs_communs():
    assert req.collaborateurs_communs(req.json_vers_nx("./data_100.json"), "Edward Grover", "Bernard Barrow") == {'Ted Beniades', 'M. Emmet Walsh', 'Barbara Eda-Young', 'Al Pacino', 'Joseph Bova', 'Tony Roberts', 'F. Murray Abraham', 'Allan Rich', 'John Randolph', 'Woodie King Jr.', 'James Tolkan', 'Nathan George', 'Biff McGuire', 'Cornelia Sharpe', 'Albert Henderson', 'Jack Kehoe', 'Judd Hirsch'}
    assert req.collaborateurs_communs(req.json_vers_nx("./data_100.json"), "Charles Durning", "Robert Duvall") == {'Teri Garr', 'Richard Bright', 'John Cazale', 'Robert De Niro', 'Allen Garfield', 'Gene Hackman', 'John Travolta', 'Al Pacino', 'Robert Redford', 'Michael Higgins', 'Dominic Chianese', 'James Caan'}
    assert req.collaborateurs_communs(req.json_vers_nx("./data_100.json"), "Daryl Hannah", "Hy Pyke") is None
    assert req.collaborateurs_communs(req.json_vers_nx("./data_100.json"), "Melvyn Douglas", "Allen Garfield") == {'Charles Durning'}
    assert req.collaborateurs_communs(req.json_vers_nx("./data_100.json"), "Floyd L. Peterson", "Bruce D. Price") == {'Paul Hirsch', 'Jennifer Salt', 'Lara Parker', 'Allen Garfield', 'Paul Bartel', 'Gerrit Graham', 'Andy Parker', 'Ricky Parker', 'Robert De Niro', 'Charles Durning', 'Joseph King'}

# tests collaborateurs_proches

def test_collaborateurs_proches():
    assert req.collaborateurs_proches(req.json_vers_nx("./data_100.json"), "Rutger Hauer", 3) is None
    assert req.collaborateurs_proches(req.json_vers_nx("./data_100.json"), "Diane Venora", 1) == {'Rip Torn', 'Kim Staunton', 'Ray Buktenica', 'Natalie Portman', 'Tom Sizemore', 'Philip Baker Hall', 'William Fichtner', 'Kevin Gage', 'Henry Rollins', 'Gary Sandy', 'Gina Gershon', 'Bruce McGill', 'Ashley Judd', 'Jerry Trimble', 'Amy Brenneman', 'Al Pacino', 'Cliff Curtis', 'Danny Trejo', 'Mike Moore', 'Robert De Niro', 'Dennis Haysbert', 'Xander Berkeley', 'Colm Feore', 'Tom Noonan', 'Russell Crowe', 'Mykelti Williamson', 'Ted Levine', 'Jeremy Piven', 'Tone Loc', 'Debi Mazar', 'Lindsay Crouse', 'Jack Palladino', 'Stephen Tobolowsky', 'Val Kilmer', 'Christopher Plummer', 'Hallie Kate Eisenberg', 'Diane Venora', 'Michael Gambon', 'Hank Azaria', 'Jon Voight', 'Roger Bart', 'Ricky Harris', 'Wes Studi', 'Renee Olstead', 'Susan Traylor'}
    assert req.collaborateurs_proches(req.json_vers_nx("./data_100.json"), "Robert MacLeod", 0) == {"Robert MacLeod"} #set() #
    assert req.collaborateurs_proches(req.json_vers_nx("./data_100.json"), "Jay Mohr", 1) == {'Winona Ryder', 'Jason Schwartzman', 'Pruitt Taylor Vince', 'Elias Koteas', 'Catherine Keener', 'Rebecca Romijn', 'Joel Heyman', 'Evan Rachel Wood', 'Jay Mohr', 'Rachel Roberts', 'Kelly Anna Cox', 'Al Pacino'}
    assert req.collaborateurs_proches(req.json_vers_nx("./data_100.json"), "Ken Baker", 1) is None
   
# tests est_proche

def test_est_proche():
    assert req.est_proche(req.json_vers_nx("./data_100.json"), "Diane Venora", "Philip Baker Hall") is True
    assert req.est_proche(req.json_vers_nx("./data_100.json"), "Jay Mohr", "Al Pacino") is True
    assert req.est_proche(req.json_vers_nx("./data_100.json"), "Michael P. Moran", "Mary Davenport") is False
    assert req.est_proche(req.json_vers_nx("./data_100.json"), "Catherine Gaffigan", "Julia Stiles") is False
    assert req.est_proche(req.json_vers_nx("./data_100.json"), "Vicki Wauchope", "Dave Goelz") is False

# tests distance_proche

def test_distance_naive():
    assert req.distance_naive(req.json_vers_nx("./data_100.json"), "Rutger Hauer", "Sean Young") is None #un ou plusieurs acteurs n'existent pas dans le graphe
    assert req.distance_naive(req.json_vers_nx("./data_100.json"), "Elliott Gould", "Elliott Gould") == 1
    assert req.distance_naive(req.json_vers_nx("./data_100.json"), "Randi Brooks", "Milton Berle") == 2
    assert req.distance_naive(req.json_vers_nx("./data_100.json"), "Charles Durning", "Dom DeLuise") == 1
    assert req.distance_naive(req.json_vers_nx("./data_100.json"), "Sam Raimi", "Anne Francis") == 3

# tests distance

def test_distance():
    assert req.distance(req.json_vers_nx("./data_100.json"), "Rutger Hauer", "Sean Young") is None
    assert req.distance(req.json_vers_nx("./data_100.json"), "Donnie Wahlberg", "James Broderick") == 2
    assert req.distance(req.json_vers_nx("./data_100.json"), "Judy Tucker", "Marcia Jean Kurtz") == 2
    assert req.distance(req.json_vers_nx("./data_100.json"), "Neal McDonough", "Neal McDonough") == 0 #ce sont les mêmes acteurs donc la distance est à 0
    assert req.distance(req.json_vers_nx("./data_100.json"), "Ben McKenzie", "Elizabeth Hubbard") == 3 

# tests centralite

# def test_centralite():
#     assert req.centralite(req.json_vers_nx("./data_100.json"), "John Hofman") == [] #il n'existe pas dans le graphe
#     assert req.centralite(req.json_vers_nx("./data_100.json"), "Robert Gerringer") == 12
#     assert req.centralite(req.json_vers_nx("./data_100.json"), "Richard Cox") == 26
#     assert req.centralite(req.json_vers_nx("./data_100.json"), "Gene Hackman") == 35
#     assert req.centralite(req.json_vers_nx("./data_100.json"), "Al Pacino") == 814

# tests centre_hollywood

