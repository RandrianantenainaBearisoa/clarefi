<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { loadingPage } from './views';
import { useLoading } from './stores/useLoader';

const loader= useLoading()
</script>

<template>
  <div>
    <loadingPage v-if="loader.isLoading.value" />
    <div v-show="!loader.isLoading.value" >
      <RouterView/>
    </div>
  </div>
</template>

<style scoped></style>

<style>
body {
  font-family: 'Saira Stencil Variable', system-ui;
  box-sizing: border-box;
}
</style>