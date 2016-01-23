import fresh_tomatoes
import media

#Creating instances of the class 'Movie' al the movies will be kept in the list movies
toy_story = media.Movie("Toy Story", "A story of a boy and his toys come to live", "img/toy_story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar","A marine on an alien planet","img/avatar.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
school_of_rock = media.Movie("School of Rock", " Struggling rock singer and guitarist", "img/school_of_rock.jpg", "https://www.youtube.com/watch?v=LqEszt5wG9I")
ratatouille = media.Movie("Ratatouille", " Remy, who dreams of becoming a chef and tries to achieve his goal by forming an alliance with a Parisian restaurant's garbage boy","img/ratatouille.jpg" ,"https://www.youtube.com/watch?v=KQUpZqshj7M")
midnight_in_paris = media.Movie("Midnight in paris", "Gil Pender, a screenwriter, who is forced to confront the shortcomings of his relationship with his materialistic fiancée and their divergent goals", "img/midnight_in_paris.jpg","https://www.youtube.com/watch?v=BYRWfS2s2v4")
hunger_games = media.Movie("Hunger Games","The Hunger Games universe is a dystopia set in \"Panem\", a country consisting of the wealthy Capitol and twelve districts in varying states of poverty", "img/hunger_games.jpg", "https://www.youtube.com/watch?v=n-7K_OjsDCQ" )
forrest_gump = media.Movie("Forrest Gump", "The story depicts several decades in the life of Forrest Gump, a slow-witted and naïve, but good-hearted and athletically prodigious man from Alabama", "img/Forrest_Gump.jpg","https://www.youtube.com/watch?v=uPIEn0M8su0")
clueless = media.Movie("Clueless", "A rich high school student tries to boost a new pupil's popularity, but reckons without affairs of the heart getting in the way", "img/Clueless.jpg", "https://www.youtube.com/watch?v=yHDcD_xhwAo")
mad_max_fury_road = media.Movie("Mad Max: Fury Road", "A woman rebels against a tyrannical ruler in post apocalyptic Australia in search for her homeland with the help of a group of female prisoners, a psychotic worshiper, and a drifter named Max", "img/mad_max.jpg", "https://www.youtube.com/watch?v=hEJnMQG9ev8")
bridge_of_spies = media.Movie("Bridge of Spies", "During the Cold War, an American lawyer is recruited to defend an arrested Soviet spy in court, and then help the CIA facilitate an exchange of the spy for the Soviet captured American U2 spy plane pilot, Francis Gary Powers", "img/bridge_of_spies.jpg","https://www.youtube.com/watch?v=mBBuzHrZBro")
catch_me_if_you_can = media.Movie ("Catch Me If You Can", "A true story about Frank Abagnale Jr., who, before his 19th birthday, successfully conned millions of dollars' worth of checks as a Pan Am pilot, doctor, and legal prosecutor", "img/catch_me_if_you_can.jpg", "https://www.youtube.com/watch?v=hFj3OXVL_wQ")
amelie = media.Movie("Amelie", "Amelie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love", "img/amelie.jpg", "https://www.youtube.com/watch?v=B-uxeZaM-VM")

#Adding all the instances of the class Movie to the list movies
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, forrest_gump, clueless, mad_max_fury_road, bridge_of_spies, catch_me_if_you_can, amelie]

#Calling the open_movies_page function to generate the HTML page with the data in the list movies
fresh_tomatoes.open_movies_page(movies)
