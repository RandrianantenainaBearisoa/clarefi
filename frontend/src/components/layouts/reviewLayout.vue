<script setup lang="ts">
import { reviewContent } from '.';
import { commentInsert } from '../ui';
import { useCurrentMovie } from '@/stores/currentMovie';
import { useReviews } from '@/stores/useReviews';

const currentMovie = useCurrentMovie()
</script>

<template>
    <div class="reviews-content-wrapper">
        <h1 class="reviews-header">
            Reviews
        </h1>
        <div class="reviews-container">
            <PrimevueScrollPanel style="width: 100%; height: 100%">
                <template v-for="review in movieReviews[currentMovie.index.value]">
                    <reviewContent :review="review" />
                </template>
            </PrimevueScrollPanel>
        </div>
        <div class="text-area-container">
            <commentInsert />
        </div>
    </div>
</template>

<script lang="ts">
const movieReviews = useReviews().list;
</script>

<style scoped>
.reviews-content-wrapper {
    padding: 5px;
    height: 600px;
    
    .reviews-header {
        margin: 5px;
    }

    .reviews-container {
        height: 400px;
    }

    .text-area-container {
        height: 100px;
    }
}
</style>