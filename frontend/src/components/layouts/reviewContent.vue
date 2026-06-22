<template>
    <div class="review-content-wrapper">
        <!-- nom, Date, Commentaire, Positive/negative -->
        <dl>
            <dt class="review-info">
                Anonymiah (date)
                <div class="predicted-class positive" v-tooltip.left="{ value: 'Predicted as Positive Review', autoHide: false }">
                    <!-- <i class="pi pi-minus-circle"></i> -->
                    <i class="pi pi-plus-circle"></i>
                </div>
            </dt>
            <dd>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis, excepturi vel eaque temporibus
                incidunt laborum repellat autem veniam iure quisquam tempora saepe quae quos atque vitae eos labore!
                Velit, consectetur!
            </dd>
        </dl>
        <hr>
    </div>
</template>

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