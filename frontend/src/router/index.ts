import { createMemoryHistory, createRouter } from 'vue-router'
import { useLoading } from '@/stores/useLoader';

const routes = [
  { path: '/', component: () => import("@/views/reviewsPage.vue") },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router