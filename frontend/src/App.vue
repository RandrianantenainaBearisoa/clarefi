<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { loadingPage } from './views';
import { useLoading } from './stores/useLoader';
import { demoSpecification } from './components/layouts';

const loader = useLoading()
</script>

<template>
  <div class="global-container">
    <loadingPage v-if="loader.isLoading.value" />
    <div v-show="!loader.isLoading.value">
      <RouterView />
    </div>
    <demoSpecification />
  </div>
</template>

<style scoped>
.global-container {
  position: relative;
}
</style>

<style>
body {
  font-family: 'Saira Stencil Variable', system-ui;
  box-sizing: border-box;
}
</style>