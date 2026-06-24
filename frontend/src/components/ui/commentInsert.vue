<template>
    <div class="comment-insert">
        <PrimevueFloatLabel variant="on">
            <PrimevueTextarea v-model.lazy.trim="comment" id="over_label" rows="2" cols="40" style="resize: none" />
            <label for="over_label">Laisser un commentaire</label>
        </PrimevueFloatLabel>
        <PrimevueButton label="Poster" icon="pi pi-comment" iconPos="right" @click="add_review" />
    </div>
</template>

<script setup lang="ts">
import { useReviews } from '@/stores/useReviews';
import { useCurrentMovie } from '@/stores/currentMovie';
import { ref } from 'vue';
import { predict } from '@/static/api/apis';

const reviews = useReviews()
const current_movie = useCurrentMovie()

const comment = ref("")

const getRandomInt = (min: number, max: number) => {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const make_username = () => {
    const french_names = [
        "Arthur", "Juliette", "Thomas", "Camille", "Lucas",
        "Emma", "Gabriel", "Chloé", "Louis", "Léa",
        "Hugo", "Manon", "Raphaël", "Zoé", "Mathis",
        "Alice", "Maël", "Inès", "Enzo", "Clara"
    ];
    const french_eeks = [
        "La Buse", "Gros", "Le Parrain", "Doc", "La Mouche",
        "Max", "Rocky", "Le Shérif", "Le Chat", "Trinity",
        "Forest", "Le Grand", "Mary Poppins", "Le Professeur",
        "Jack", "Indiana", "Amélie", "Le Pianiste", "Zorro", "Yoda",
    ];
    const f_name = french_names[getRandomInt(0, 19)]
    const f_eek = french_eeks[getRandomInt(0, 19)]
    return f_name + " " + f_eek + getRandomInt(1, 10000)
}

const add_review = async () => {
    if (comment.value.length > 0) {
        const username = make_username();
        const date_now = new Date().toISOString().split('T')[0];
        predict(String(comment.value)).then((prediction: any) => {
            if (prediction) {
                const label = Number(Array.from(prediction)[0]);
                const sentiment = label ? "positive" : "negative"
                const new_review = { "username": username, "date": date_now ?? "1970-01-01", "text": String(comment.value), "label": label, "sentiment": sentiment };
                reviews.add_review(new_review, current_movie.index.value)
                comment.value = ""
            }
        });
    }
}


</script>

<style scoped>
.comment-insert {
    --p-floatlabel-focus-color: #a1a1aa;

    height: 100%;
    display: flex;
    align-items: center;
    gap: 10px;
}
</style>