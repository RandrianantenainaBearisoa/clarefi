import { createMemoryHistory, createRouter } from 'vue-router'
import { reviewsPage } from '@/views'

const routes = [
  { path: '/', component: reviewsPage },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router