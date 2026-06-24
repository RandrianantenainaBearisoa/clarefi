<template>
    <header>
        <h1>
            Clarefi
        </h1>
        <p>Classificateur de critique sur les films.</p>
    </header>
    <main>
        <slot />
    </main>
    <footer>
        <p>&copy; 2026 Clarefi. All rights reserved.</p>
    </footer>
</template>

<style scoped>
header {
    text-align: center;
    padding: 30px 20px;
    background-color: #1a1a1a;
    color: #e0e0e0;
    border-bottom: 1px solid #333;
}

header h1 {
    margin: 0 0 10px 0;
    font-size: 32px;
    color: #ffffff;
}

header p {
    margin: 0;
    font-size: 14px;
    color: #b0b0b0;
}

footer {
    text-align: center;
    padding: 20px;
    background-color: #1a1a1a;
    color: #808080;
    border-top: 1px solid #333;
    font-size: 13px;
    margin-top: 40px;
}

footer p {
    margin: 0;
}
</style>