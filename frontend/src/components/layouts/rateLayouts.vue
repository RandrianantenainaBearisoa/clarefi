<script setup lang="ts">
import { useReviews } from '@/stores/useReviews';
import { ref } from 'vue';

const reviews = useReviews()
const reviews_numbers = ref(reviews.get_reviews_numbers)
</script>

<template>
    <div class="rate-layout">
        <div>Critiques: </div>
        <div class="count" :title="`${reviews_numbers.pos} Critiques Positives`">
            <PrimevueBadge :value="reviews_numbers.pos" size="xlarge" severity="success"/>
        </div>
        <div class="count" :title="`${reviews_numbers.neg} Critiques Négatives`">
            <PrimevueBadge :value="reviews_numbers.neg" size="xlarge" severity="danger"/>
        </div>
    </div>
</template>

<style scoped>
.rate-layout {
    display: flex;
    align-items: center;
    gap: 15px;
    
    .count {
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }

    &>div {
        font-weight: bold;
    }
}
</style>