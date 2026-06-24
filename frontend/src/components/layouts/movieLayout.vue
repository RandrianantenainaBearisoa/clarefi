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
        "Title": "Les Gardiens de la Galaxie Vol. 2",
        "Genre": "Action, Aventure, Comédie",
        "Director": "James Gunn",
        "Writer": "James Gunn, Dan Abnett, Andy Lanning",
        "Actors": "Chris Pratt, Zoe Saldaña, Dave Bautista",
        "Plot": "Les Gardiens se battent pour rester unis en tant qu'équipe tout en gérant leurs problèmes familiaux personnels, notamment la rencontre de Star-Lord avec son père, l'ambitieux être céleste Ego.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BNWE5MGI3MDctMmU5Ni00YzI2LWEzMTQtZGIyZDA5MzQzNDBhXkEyXkFqcGc@._V1_QL75_UX380_CR0,1,380,562_.jpg"
    },
    {
        "Title": "Inception",
        "Genre": "Action, Science-fiction, Science-fiction",
        "Director": "Christopher Nolan",
        "Writer": "Christopher Nolan",
        "Actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
        "Plot": "Un voleur qui vole des secrets d'entreprise en utilisant la technologie de partage de rêves reçoit la tâche inverse de planter une idée dans l'esprit d'un P.D.G.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Le Chevalier Noir",
        "Genre": "Action, Criminel, Drame",
        "Director": "Christopher Nolan",
        "Writer": "Jonathan Nolan, Christopher Nolan, David S. Goyer",
        "Actors": "Christian Bale, Heath Ledger, Aaron Eckhart",
        "Plot": "Quand le Joker sème la terreur et le chaos à Gotham, Batman doit accepter l'un des plus grands défis psychologiques et physiques de sa capacité à combattre l'injustice.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Interstellar",
        "Genre": "Aventure, Drame, Science-fiction",
        "Director": "Christopher Nolan",
        "Writer": "Jonathan Nolan, Christopher Nolan",
        "Actors": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        "Plot": "Quand la Terre devient inhabitable, une équipe d'explorateurs traverse un trou de ver dans l'espace pour assurer la survie de l'humanité.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWYwXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Pulp Fiction",
        "Genre": "Criminel, Drame",
        "Director": "Quentin Tarantino",
        "Writer": "Quentin Tarantino, Roger Avary",
        "Actors": "John Travolta, Uma Thurman, Samuel L. Jackson",
        "Plot": "Les vies de deux tueurs à gages, d'un boxeur, d'un gangster et sa femme, et d'une paire de braqueurs de restaurant s'entrelacent en quatre histoires de violence et de rédemption.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYTViYTE3ZGQtNDFkNC00ODYyLTkxNjAtODExMWFjNDkwYzhkXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Spider-Man : New Generation",
        "Genre": "Animation, Action, Aventure",
        "Director": "Bob Persichetti, Peter Ramsey, Rodney Rothman",
        "Writer": "Phil Lord, Rodney Rothman",
        "Actors": "Shameik Moore, Jake Johnson, Hailee Steinfeld",
        "Plot": "Miles Morales, un ado, devient le Spider-Man de son univers et doit s'unir avec cinq individus dotés de pouvoirs araignées d'autres dimensions pour arrêter une menace pour tous les univers.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Tout Partout Tout à la Fois",
        "Genre": "Action, Aventure, Comédie",
        "Director": "Daniel Kwan, Daniel Scheinert",
        "Writer": "Daniel Kwan, Daniel Scheinert",
        "Actors": "Michelle Yeoh, Stephanie Hsu, Ke Huy Quan",
        "Plot": "Une immigrée chinoise d'âge moyen est entraînée dans une aventure insensée dans laquelle elle seule peut sauver l'existence en explorant d'autres univers et en se connectant aux vies qu'elle aurait pu vivre.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYTdiOTIyZTQtNmQ1OS00NjZlLWIyM2UtMjI2ZDRjODY2M2NjXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Matrix",
        "Genre": "Action, Science-fiction",
        "Director": "Lana Wachowski, Lilly Wachowski",
        "Writer": "Lana Wachowski, Lilly Wachowski",
        "Actors": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
        "Plot": "Quand une belle étrangère attire le hacker informatique Neo dans un monde souterrain redoutable, il découvre la vérité choquante - la vie qu'il connaît est la tromperie élaborée d'une cyber-intelligence malveillante.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BN2NmY2VhMTQtMDYyOS00YzQ0LWI2Y2QtOTU5MTYyNjA1NzcxXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Parasite",
        "Genre": "Drame, Thriller",
        "Director": "Bong Joon Ho",
        "Writer": "Bong Joon Ho, Jin Won Han",
        "Actors": "Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong",
        "Plot": "La cupidité et la discrimination de classe menacent la nouvelle relation symbiotique entre la riche famille Park et le clan Kim démuni.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwMWQ4ODhjXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    },
    {
        "Title": "Dune : Deuxième Partie",
        "Genre": "Action, Aventure, Drame",
        "Director": "Denis Villeneuve",
        "Writer": "Denis Villeneuve, Jon Spaihts, Frank Herbert",
        "Actors": "Timothée Chalamet, Zendaya, Rebecca Ferguson",
        "Plot": "Paul Atreides s'unit avec Chani et les Fremen tout en cherchant sa vengeance contre les conspirateurs qui ont détruit sa famille.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BODdjMjM3NGQtZDA5OC00NGEyLWIyZDAtZDg0NThjODQ0Nzk3XkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg"
    }
];

const currentMovie = useCurrentMovie()

const onPageChange = (new_page: number) => {
    currentMovie.change(new_page)
};
</script>