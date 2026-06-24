<template>
    <div class="review-content-wrapper">
        <dl>
            <dt class="review-info">
                {{ prop.review.username }} ({{ prop.review.date }}) <PrimevueBadge v-if="prop.review.added" value="(votre commentaire)" severity="success"></PrimevueBadge>
                <div class="predicted-class positive" :class="{ negative: prop.review.label==0 }" v-tooltip.left="{ value: 'Predicted as Positive Review', autoHide: false }">
                    <template v-if="prop.review.label==0">
                        <i class="pi pi-minus-circle"></i>
                    </template>
                    <template v-else>
                        <i class="pi pi-plus-circle"></i>
                    </template>
                </div>
            </dt>
            <dd>
                {{ prop.review.text }}
            </dd>
        </dl>
        <hr>
    </div>
</template>

<script lang="ts" setup>
import type Review from '@/static/interfaces/reviewData';

interface Props {
    review: Review
}

const prop = defineProps<Props>()
</script>

<style scoped>
.review-content-wrapper {
    .review-info {
        position: relative;
        
        .predicted-class{
            position: absolute;
            top: 0;
            right: 0;

            &.positive {
                color: green;
            }
            &.negative {
                color: red;
            }
        }
    }

    hr {
        width: 50%;
    }
}
</style>