import { createMemoryHistory, createRouter } from 'vue-router'
import { useLoading } from '@/stores/useLoader';

const routes = [
  { path: '/', component: () => import("@/views/reviewsPage.vue") },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const loader = useLoading();
  loader.start_loading();
  next();
});

router.afterEach(() => {
  const loader = useLoading();
  loader.stop_loading();
});

export default router