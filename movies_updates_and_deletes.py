import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue. . .")

    # create cursor connection
    cursor = db.cursor()

    def show_films():
        query = "SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio " \
                "Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON " \
                "film.studio_id = studio.studio_id "
				
#use fetchall() 

        cursor.execute(query)
        films = cursor.fetchall()
        for film in films:
		
            print("Film Name: ", film[0])
			
            print("Director: ", film[1])
			
            print("Genre Name ID: ", film[2])
			
            print("Studio Name: ", film[3])
			
            print("  ")
			
#print films

    print("\n-- DISPLAYING FILMS --")
    show_films()

    print("\n-- DISPLAYING FILMS AFTER INSERT --")
    query = "INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)" \
            "VALUES ('Star Wars', 'George Lucas', 2, 1, 1977, 121) "
    cursor.execute(query)
    db.commit()
    show_films()

    print("\n-- DISPLAYING FILMS AFTER UPDATE --")
    query = "UPDATE film SET genre_id = 1 WHERE film_id = 2"
    cursor.execute(query)
    db.commit()
    show_films()

    print("\n-- DISPLAYING FILMS AFTER DELETE --")
    query = "DELETE FROM film WHERE film_id = 1"
    cursor.execute(query)
    db.commit()
    show_films()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
