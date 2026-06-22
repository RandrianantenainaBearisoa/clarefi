<script setup lang="ts">
</script>

<template>
    <div class="comment-insert">
        <PrimevueFloatLabel variant="on">
            <Textarea id="over_label" rows="4" cols="60" style="resize: none" />
            <label for="over_label">Laisser un commentaire</label>
        </PrimevueFloatLabel>
        <PrimevueButton label="Poster" icon="pi pi-comment" iconPos="right" />
    </div>
</template>

<style scoped>
.comment-insert {
    --p-floatlabel-focus-color: #a1a1aa;

    height: 100%;
    display: flex;
    align-items: center;
    gap: 10px;
}
</style>