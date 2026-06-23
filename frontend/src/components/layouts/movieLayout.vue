<script setup lang="ts">
import { movieCard } from '.';
import { useCurrentMovie } from '@/stores/currentMovie';
</script>

<template>
    <div class="movie-layout-container">
        <PrimevueCarousel :value="movies" :numVisible="1" :numScroll="1" orientation="vertical"
            verticalViewPortHeight="400px" containerClass="flex items-center" circular @update:page="onPageChange">
            <template #item="slotProps">
                <movieCard :movie="slotProps.data"/>
            </template>
        </PrimevueCarousel>
    </div>
</template>

<script lang="ts">
const movies = [
    {
        "Title": "Guardians of the Galaxy Vol. 2",
        "Genre": "Action, Adventure, Comedy",
        "Director": "James Gunn",
        "Writer": "James Gunn, Dan Abnett, Andy Lanning",
        "Actors": "Chris Pratt, Zoe Saldaña, Dave Bautista",
        "Plot": "The Guardians struggle to keep together as a team while dealing with their personal family issues, notably Star-Lord's encounter with his father, the ambitious celestial being Ego.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BNWE5MGI3MDctMmU5Ni00YzI2LWEzMTQtZGIyZDA5MzQzNDBhXkEyXkFqcGc@._V1_QL75_UX380_CR0,1,380,562_.jpg"
    },
    {
        "Title": "Inception",
        "Genre": "Action, Sci-Fi, Sci-Fi",
        "Director": "Christopher Nolan",
        "Writer": "Christopher Nolan",
        "Actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
        "Plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "The Dark Knight",
        "Genre": "Action, Crime, Drama",
        "Director": "Christopher Nolan",
        "Writer": "Jonathan Nolan, Christopher Nolan, David S. Goyer",
        "Actors": "Christian Bale, Heath Ledger, Aaron Eckhart",
        "Plot": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Interstellar",
        "Genre": "Adventure, Drama, Sci-Fi",
        "Director": "Christopher Nolan",
        "Writer": "Jonathan Nolan, Christopher Nolan",
        "Actors": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        "Plot": "When Earth becomes uninhabitable, a team of explorers travels through a wormhole in space in an attempt to ensure humanity's survival.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWYwXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Pulp Fiction",
        "Genre": "Crime, Drama",
        "Director": "Quentin Tarantino",
        "Writer": "Quentin Tarantino, Roger Avary",
        "Actors": "John Travolta, Uma Thurman, Samuel L. Jackson",
        "Plot": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYTViYTE3ZGQtNDFkNC00ODYyLTkxNjAtODExMWFjNDkwYzhkXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Spider-Man: Into the Spider-Verse",
        "Genre": "Animation, Action, Adventure",
        "Director": "Bob Persichetti, Peter Ramsey, Rodney Rothman",
        "Writer": "Phil Lord, Rodney Rothman",
        "Actors": "Shameik Moore, Jake Johnson, Hailee Steinfeld",
        "Plot": "Teen Miles Morales becomes the Spider-Man of his universe and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Everything Everywhere All at Once",
        "Genre": "Action, Adventure, Comedy",
        "Director": "Daniel Kwan, Daniel Scheinert",
        "Writer": "Daniel Kwan, Daniel Scheinert",
        "Actors": "Michelle Yeoh, Stephanie Hsu, Ke Huy Quan",
        "Plot": "A middle-aged Chinese immigrant is swept up into an insane adventure in which she alone can save existence by exploring other universes and connecting with the lives she could have led.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYTdiOTIyZTQtNmQ1OS00NjZlLWIyM2UtMjI2ZDRjODY2M2NjXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "The Matrix",
        "Genre": "Action, Sci-Fi",
        "Director": "Lana Wachowski, Lilly Wachowski",
        "Writer": "Lana Wachowski, Lilly Wachowski",
        "Actors": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
        "Plot": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BN2NmY2VhMTQtMDYyOS00YzQ0LWI2Y2QtOTU5MTYyNjA1NzcxXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Parasite",
        "Genre": "Drama, Thriller",
        "Director": "Bong Joon Ho",
        "Writer": "Bong Joon Ho, Jin Won Han",
        "Actors": "Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong",
        "Plot": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwMWQ4ODhjXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Dune: Part Two",
        "Genre": "Action, Adventure, Drama",
        "Director": "Denis Villeneuve",
        "Writer": "Denis Villeneuve, Jon Spaihts, Frank Herbert",
        "Actors": "Timothée Chalamet, Zendaya, Rebecca Ferguson",
        "Plot": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BODdjMjM3NGQtZDA5OC00NGEyLWIyZDAtZDg0NThjODQ0Nzk3XkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    }
];

const currentMovie = useCurrentMovie()

const onPageChange = (new_page: number) => {
    currentMovie.change(new_page)
};
</script>