<script setup lang="ts">
import { movieLayout, reviewLayout, bodyLayout } from '@/components/layouts';
</script>

<template>
    <body-layout>
        <div class="content-wrapper">
            <div class="movie-container">
                <movieLayout />
            </div>

            <div class="reviews-container">
                <reviewLayout />
            </div>
        </div>
    </body-layout>
</template>

<style scoped>
.content-wrapper {
    display: flex;
    justify-content: space-between;

    .movie-container,
    .reviews-container {
        width: 49%;
    }
}
</style>