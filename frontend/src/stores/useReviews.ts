import { ref } from 'vue'
import type Review from '@/static/interfaces/reviewData'

const list = ref([
  // 1. Guardians of the Galaxy Vol. 2
  [
    { "username": "GamerGroot_99", "date": "2023-05-14", "text": "Une excellente suite, l'humour est omniprésent et la bande originale est fantastique. On ne s'ennuie pas une seconde !", "label": 1, "sentiment": "positive" },
    { "username": "CinePhile_Mada", "date": "2023-08-22", "text": "Visuellement c'est très beau, mais l'histoire familiale traîne en longueur. Moins surprenant que le premier opus.", "label": 0, "sentiment": "negative" },
    { "username": "StarLord_Fan", "date": "2024-01-10", "text": "Baby Groot est adorable et les scènes d'action dynamiques sauvent un scénario un peu trop prévisible.", "label": 1, "sentiment": "positive" },
    { "username": "Rayan_K", "date": "2024-06-05", "text": "Trop d'humour lourd qui désamorce les enjeux dramatiques. Une déception par rapport au volume 1.", "label": 0, "sentiment": "negative" }
  ],
  // 2. Inception
  [
    { "username": "Nolan_Addict", "date": "2022-11-03", "text": "Un chef-d'œuvre absolu de la science-fiction. Le concept des rêves emboîtés est brillant et la réalisation est parfaite.", "label": 1, "sentiment": "positive" },
    { "username": "DreamWatcher", "date": "2023-04-19", "text": "Scénario inutilement complexe et alambiqué. On passe plus de temps à essayer de comprendre qu'à apprécier le film.", "label": 0, "sentiment": "negative" },
    { "username": "Mal_Cob", "date": "2024-09-12", "text": "Leonardo DiCaprio est magistral dans ce thriller psychologique intense. La fin laisse sans voix.", "label": 1, "sentiment": "positive" }
  ],
  // 3. The Dark Knight
  [
    { "username": "Gotham_Knight", "date": "2021-07-25", "text": "La performance de Heath Ledger en Joker est légendaire. Le meilleur film de super-héros jamais réalisé.", "label": 1, "sentiment": "positive" },
    { "username": "Harvey_D", "date": "2022-02-14", "text": "Un film policier sombre et captivant d'un bout à l'autre. Une tension psychologique incroyable.", "label": 1, "sentiment": "positive" },
    { "username": "Bane_91", "date": "2023-10-30", "text": "C'est beaucoup trop long et la dernière partie avec Double-Face gâche un peu le rythme de l'intrigue.", "label": 0, "sentiment": "negative" },
    { "username": "CineCritik", "date": "2024-03-08", "text": "Une réalisation impeccable et une ambiance réaliste qui révolutionne le genre.", "label": 1, "sentiment": "positive" }
  ],
  // 4. Interstellar
  [
    { "username": "Cooper_Murph", "date": "2022-05-29", "text": "Une claque visuelle et émotionnelle monumentale. La bande son de Hans Zimmer donne des frissons à chaque scène.", "label": 1, "sentiment": "positive" },
    { "username": "Astro_Aina", "date": "2023-01-15", "text": "Les concepts scientifiques sont fascinants, mais la fin sombre dans un mysticisme un peu ridicule et mielleux.", "label": 0, "sentiment": "negative" },
    { "username": "Tars_Robot", "date": "2024-07-22", "text": "Le meilleur film sur l'espace depuis 2001 l'Odyssée de l'espace. Bouleversant et grandiose.", "label": 1, "sentiment": "positive" }
  ],
  // 5. Pulp Fiction
  [
    { "username": "Vincent_Vega", "date": "2020-09-04", "text": "Des dialogues cultes, une narration non-linéaire maîtrisée et des acteurs au sommet de leur art. Du pur Tarantino.", "label": 1, "sentiment": "positive" },
    { "username": "Mia_Wallace", "date": "2021-12-11", "text": "Une violence gratuite et beaucoup trop de bavardages inutiles. Je n'ai jamais compris l'engouement autour de ce film.", "label": 0, "sentiment": "negative" },
    { "username": "RoyaleWithCheese", "date": "2023-06-27", "text": "La bande originale est incroyable et l'ambiance des années 90 est parfaitement retranscrite. Un classique instantané.", "label": 1, "sentiment": "positive" },
    { "username": "Butch_C", "date": "2024-02-18", "text": "Une mise en scène stylée mais l'histoire décousue m'a laissé totalement indifférent.", "label": 0, "sentiment": "negative" }
  ],
  // 6. Spider-Man: Into the Spider-Verse
  [
    { "username": "Miles_M", "date": "2021-04-12", "text": "Une révolution visuelle ! L'animation donne l'impression de voir un comic book prendre vie sous nos yeux.", "label": 1, "sentiment": "positive" },
    { "username": "Gwen_Stacy", "date": "2022-08-01", "text": "L'histoire de Miles Morales est touchante et pleine de fraîcheur. Bien supérieure aux versions live-action récentes.", "label": 1, "sentiment": "positive" },
    { "username": "Noire_Vibe", "date": "2023-11-20", "text": "L'esthétique graphique est trop agressive pour les yeux, le style saccadé m'a donné un mal de tête terrible.", "label": 0, "sentiment": "negative" }
  ],
  // 7. Everything Everywhere All at Once
  [
    { "username": "Waymond_Verse", "date": "2022-10-09", "text": "Un dille créatif total, à la fois hilarant, absurde et profondément émouvant. Michelle Yeoh mérite amplement ses éloges.", "label": 1, "sentiment": "positive" },
    { "username": "Jobu_Tupaki", "date": "2023-03-24", "text": "C'est un chaos fatigant. Le film en fait des caisses pendant deux heures, ça devient vite insupportable et indigeste.", "label": 0, "sentiment": "negative" },
    { "username": "Bagel_Eater", "date": "2023-07-14", "text": "Une originalité folle qui explore le concept du multivers avec beaucoup plus de cœur et d'idées que Marvel.", "label": 1, "sentiment": "positive" },
    { "username": "Alpha_Verse", "date": "2024-01-05", "text": "L'humour absurde tombe souvent à plat et l'action frénétique masque un manque de profondeur évident.", "label": 0, "sentiment": "negative" }
  ],
  // 8. The Matrix
  [
    { "username": "Neo_Chose", "date": "2020-03-11", "text": "Un chef-d'œuvre cyberpunk révolutionnaire. Les effets spéciaux du bullet-time ont marqué l'histoire du cinéma.", "label": 1, "sentiment": "positive" },
    { "username": "Cypher_Steak", "date": "2021-10-02", "text": "Une philosophie de comptoir enveloppée dans des combats d'arts martiaux. Ça a très mal vieilli visuellement.", "label": 0, "sentiment": "negative" },
    { "username": "Trinity_Kick", "date": "2023-05-25", "text": "Le scénario pose d'excellentes questions sur la réalité et la technologie. Une claque absolue pour son époque.", "label": 1, "sentiment": "positive" }
  ],
  // 9. Parasite
  [
    { "username": "Kim_Ki_Taek", "date": "2020-06-20", "text": "Une satire sociale grinçante et brillante. Le basculement de ton en plein milieu du film est un coup de génie.", "label": 1, "sentiment": "positive" },
    { "username": "Mr_Park", "date": "2021-01-14", "text": "Une mise en scène millimétrée. Bong Joon Ho signe une oeuvre captivante et cruellement réaliste.", "label": 1, "sentiment": "positive" },
    { "username": "Jessica_Illinois", "date": "2022-09-08", "text": "Une tension étouffante qui monte crescendo jusqu'à un final mémorable. Palme d'or totalement méritée.", "label": 1, "sentiment": "positive" },
    { "username": "Basement_Ghost", "date": "2023-11-12", "text": "Les ficelles du scénario sont un peu grosses et les personnages riches sont trop caricaturaux pour être crédibles.", "label": 0, "sentiment": "negative" }
  ],
  // 10. Dune: Part Two
  [
    { "username": "Muad_Dib24", "date": "2024-03-15", "text": "Un spectacle visuel et sonore d'une puissance rare. Denis Villeneuve maîtrise l'univers de Frank Herbert à la perfection.", "label": 1, "sentiment": "positive" },
    { "username": "Harkonnen_Blade", "date": "2024-04-20", "text": "La photographie est splendide mais le rythme est d'une lenteur mortelle. Les combats manquent cruellement d'énergie.", "label": 0, "sentiment": "negative" },
    { "username": "Chani_Sietch", "date": "2024-05-02", "text": "Timothée Chalamet est impérial. Un opéra spatial grandiose qui surpasse le premier volet en termes d'action.", "label": 1, "sentiment": "positive" },
    { "username": "Gurney_Man", "date": "2024-06-18", "text": "Le traitement des personnages secondaires est bâclé et la fin est trop abrupte. Décevant au vu de l'attente.", "label": 0, "sentiment": "negative" }
  ]
])

export const useReviews = () => {
    return {
        list,
        add_review : (new_review: Review, movie_index: number) => {
            list.value[movie_index]?.unshift(new_review)
        }

    }
}