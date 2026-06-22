<script setup lang="ts">
import { rateLayouts } from '.';
</script>

<template>
    <PrimevueScrollPanel style="width: 100%; height: 400px">
        <div class="intrduction-wrapper">
            <h1 class="movie-title">Movie Title </h1>
            <div class="movie-plot">
                [Synopsys]Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit magni, molestias vitae earum
                cupiditate reiciendis commodi neque iste explicabo. Illum laudantium ratione magnam accusantium error
                eligendi provident deleniti libero labore?
                [Synopsys]Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit magni, molestias vitae earum
                cupiditate reiciendis commodi neque iste explicabo. Illum laudantium ratione magnam accusantium error
                eligendi provident deleniti libero labore?
                [Synopsys]Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit magni, molestias vitae earum
                cupiditate reiciendis commodi neque iste explicabo. Illum laudantium ratione magnam accusantium error
                eligendi provident deleniti libero labore?
                [Synopsys]Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit magni, molestias vitae earum
                cupiditate reiciendis commodi neque iste explicabo. Illum laudantium ratione magnam accusantium error
                eligendi provident deleniti libero labore?
            </div>
            <dl>
                <dt>Genre</dt>
                <dd>Action, Drame</dd>
                <dt>Réalisateur</dt>
                <dd>James Wan</dd>
                <dt>Scénariste</dt>
                <dd>Jean-Claude Van Damme</dd>
                <dt>Acteur(s)</dt>
                <dd>Jean-Claude Van Damme, Bruce Lee</dd>
            </dl>
            <rate-layouts />
        </div>
    </PrimevueScrollPanel>
</template>

<style scoped>
.intrduction-wrapper {
    padding: 10px;

    .movie-title {
        margin: 5px;
    }

    dl dt {
        font-weight: bold;
    }

    .movie-plot {
        text-align: justify;
    }
}
</style>