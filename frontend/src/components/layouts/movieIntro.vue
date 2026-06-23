<script setup lang="ts">
import { rateLayouts } from '.';
import type Movie from '@/static/interfaces/movieData';

interface Props {
  movie: Movie
}
const prop = defineProps<Props>()
</script>

<template>
    <PrimevueScrollPanel style="width: 100%; height: 400px">
        <div class="introduction-wrapper">
            <h1 class="movie-title">{{ prop.movie.Title }}</h1>
            <div class="movie-plot">
                {{ prop.movie.Plot }}
            </div>
            <dl>
                <dt>Genre</dt>
                <dd>{{ prop.movie.Genre }}</dd>
                <dt>Réalisateur</dt>
                <dd>{{ prop.movie.Director }}</dd>
                <dt>Scénariste</dt>
                <dd>{{ prop.movie.Writer }}</dd>
                <dt>Acteur(s)</dt>
                <dd>{{ prop.movie.Actors }}</dd>
            </dl>
            <rate-layouts />
        </div>
    </PrimevueScrollPanel>
</template>

<style scoped>
.introduction-wrapper {
    padding: 10px;

    .movie-title {
        margin: 5px;
    }

    dl dt {
        font-weight: bold;
    }

    .movie-plot {
        text-align: justify;
    }
}
</style>