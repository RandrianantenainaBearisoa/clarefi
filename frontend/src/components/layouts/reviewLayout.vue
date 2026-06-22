<script setup>
import { reviewContent } from '.';
import { commentInsert } from '../ui';
</script>

<template>
    <div class="reviews-content-wrapper">
        <h1 class="reviews-header">
            Reviews
        </h1>
        <div class="reviews-container">
            <PrimevueScrollPanel style="width: 100%; height: 100%">
                <reviewContent />
                <reviewContent />
                <reviewContent />
                <reviewContent />
                <reviewContent />
            </PrimevueScrollPanel>
        </div>
        <div class="text-area-container">
            <commentInsert />
        </div>
    </div>
</template>

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