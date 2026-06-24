<template>
    <div class="img-container">
        <img :src="prop.poster_url" onerror="this.onerror=null; this.src='./assets/imgs/placeholder.png';" alt="Affiche de film">
    </div>
</template>

<script setup lang="ts">
interface Props {
    poster_url: string
}
const prop = defineProps<Props>()
</script>

<style scoped>
.img-container {
    height: 100%;
    max-width: 250px;
    overflow: hidden;

    img {
        height: 100%;
    }
}
</style>