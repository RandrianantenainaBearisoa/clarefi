<script setup lang="ts">
import { moviePoster } from '../ui';
import { movieIntro } from '.';
import type Movie from '@/static/interfaces/movieData';

interface Props {
  movie: Movie
}
const prop = defineProps<Props>()
</script>

<template>
  <div class="movie-layout">
    <div class="movie-poster-container">
      <movie-poster :poster_url="prop.movie.Poster" />
    </div>
    <div class="movie-intro-container">
      <movie-intro :movie="prop.movie"/>
    </div>
  </div>
</template>

<style scoped>
.movie-layout {
  display: flex;
  padding: 5px;
  gap: 10px;
  height: 400px;
  border: 1px solid white;
  overflow: hidden;

  .movie-poster-container {
    width: 50%;
    display: flex;
    justify-content: center;
  }
}
</style>