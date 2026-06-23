<template>
    <div>
        Loading ...
        <span class="loader"></span>
    </div>
</template>

<style scoped>
div {
    width: 98vw;
    height: 98vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;

    .loader {
        width: 100px;
        height: 100px;
        position: absolute;
        border-radius: 50%;
        border-style: dotted dashed solid;
        animation: looping 400ms ease-in-out infinite normal;
    }
}

@keyframes looping {
    0% {
        transform: rotate(0deg);
    }

    25% {
        transform: rotate(90deg);
    }

    50% {
        transform: rotate(180deg);
    }

    75% {
        transform: rotate(270deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>