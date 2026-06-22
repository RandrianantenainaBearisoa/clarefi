<script setup lang="ts">
import { movieLayout, reviewLayout } from '@/components/layouts';
</script>

<template>
    <div class="content-wrapper">
        <div class="movie-container">
            <movieLayout />
        </div>

        <div class="reviews-container">
            <reviewLayout />
        </div>
    </div>
</template>

<style scoped>
.content-wrapper {
    display: flex;
    justify-content: space-between;

    .movie-container, .reviews-container {
        border: 1px solid black;
        width: 49%;
    }
}
</style>