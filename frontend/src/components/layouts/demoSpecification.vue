<template>
    <div class="demo-spec-container">
        <PrimevueButton label="Info sur la DEMO" severity="danger" @click="visible = true" />
        <PrimevueDialog v-model:visible="visible" modal header="Spécificités de la version démo"
            :style="{ width: '70%' }">
            <div class="demo-spec-content">
                <dl>
                    <div class="spec-item">
                        <dt>Objectif de la démo</dt>
                        <dd>
                            Cette version a pour vocation de démontrer le flux complet d’analyse d’un commentaire, de
                            l’entrée utilisateur jusqu’à l’affichage du résultat de prédiction (validation
                            fonctionnelle, preuve de concept).
                        </dd>
                    </div>

                    <div class="spec-item">
                        <dt>Exécution locale</dt>
                        <dd>
                            L’application est exécutée côté navigateur (client-side) et ne nécessite pas de backend
                            dédié pour le traitement principal.
                        </dd>
                    </div>

                    <div class="spec-item">
                        <dt>Modèle de prédiction</dt>
                        <dd>
                            La classification des commentaires repose sur un modèle ONNX chargé localement à partir des
                            assets du projet (inference on edge, runtime web).
                        </dd>
                    </div>

                    <div class="spec-item">
                        <dt>Persistance des données</dt>
                        <dd>
                            Aucune donnée utilisateur n’est sauvegardée de manière permanente (no persistence,
                            session-only).
                        </dd>
                    </div>

                    <div class="spec-item">
                        <dt>Langue utilisée</dt>
                        <dd>
                            L'application est en français car elle est conçue pour traiter des commentaires rédigés en
                            français. Le modèle a été entrainé à partir de données cette langue. Ce choix permet
                            d’obtenir une
                            compréhension plus naturelle et cohérente des textes soumis dans le contexte de
                            l’application.
                        </dd>
                    </div>

                    <div class="spec-item">
                        <dt>Modèle ML/IA</dt>
                        <dd>
                            Le système repose sur un modèle de machine learning / intelligence artificielle utilisé pour
                            la classification des commentaires. Comme tout modèle prédictif, il peut produire des
                            résultats erronés, notamment sur des phrases ambiguës, sarcastiques ou hors domaine.
                        </dd>
                    </div>

                    <div class="spec-item">
                        <dt>Indications</dt>
                        <dd>
                            <ul>
                                <li>Pour tester , laissez un commentaire et cliquez sur "Poster".</li>
                                <li>Les noms d'utilisateur sont générés aléatoirement.</li>
                                <li>
                                    Le résultat de la prédiction pour une critique est en haut à droite:
                                    <ul>
                                        <li>
                                            <i class="pi pi-plus-circle" style="color: green;"></i> pour les critiques
                                            positives.
                                        </li>
                                        <li>
                                            <i class="pi pi-minus-circle" style="color: red;"></i> pour les critiques
                                            négatives.
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </dd>
                    </div>
                </dl>
            </div>
        </PrimevueDialog>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const visible = ref(false)
</script>

<style scoped>
.demo-spec-container {
    position: absolute;
    top: 0;
    right: 0;
}
</style>