import media
import fresh_tomatoes

#toy_story = media.Movie()

ghost_in_the_shell = media.Movie("Ghost in the shell (2015)",
	r'''In the year 2027, a year following the end of the non-nuclear World War IV, a bomb has gone off in Newport City, killing a major arms dealer who may have ties with the mysterious 501 Organization. Public Security official Daisuke Aramaki hires full-body cyber prosthesis user and hacker extraordinaire, Motoko Kusanagi, to investigate.''',
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMTY1MDk4MDU5MF5BMl5BanBnXkFtZTgwMTE5MjQxNzE@._V1_SY1000_CR0,0,772,1000_AL_.jpg",
	"https://www.youtube.com/watch?v=b5g1xubyuVs")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

batman = media.Movie("Batman v Superman: Dawn of Justice",
	'''The general public is concerned over having Superman on their planet and letting the "Dark Knight" - Batman - pursue the streets of Gotham.''',
	"https://images-na.ssl-images-amazon.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
	"https://www.youtube.com/watch?v=0WWzgGyAH6Y")

movies = [avatar, ghost_in_the_shell, batman]
fresh_tomatoes.open_movies_page(movies)

