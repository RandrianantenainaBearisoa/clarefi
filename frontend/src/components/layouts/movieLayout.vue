<script setup lang="ts">
import { moviePoster } from '../ui';
import { movieIntro } from '.';
</script>

<template>
    <div class="movie-layout">
        <div class="movie-poster-container">
            <movie-poster />
        </div>
        <div class="movie-intro-container">
            <movie-intro />
        </div>
    </div>
</template>

<style scoped>
.movie-layout {
    display: flex;
    padding: 5px;
    gap: 10px;
    height: 400px;

    .movie-poster-container {
        width: 50%;
        display: flex;
        justify-content: center;
    }
}
</style>