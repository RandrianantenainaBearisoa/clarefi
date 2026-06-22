<script setup lang="ts">
</script>

<template>
    <div class="rate-layout">
        <div>Critiques: </div>
        <div class="count" title="8 Critiques Positives">
            <PrimevueBadge value="8" size="xlarge" severity="success"/>
        </div>
        <div class="count" title="6 Critiques Négatives">
            <PrimevueBadge value="6" size="xlarge" severity="danger"/>
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