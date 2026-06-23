import { reactive, computed } from "vue";

const current_movie = reactive({
    index: 0
});

export const useCurrentMovie = () => {
  const change = (new_index: number) => {
    current_movie.index = new_index;
  };

  return {
    index: computed(() => current_movie.index),
    change
  };
};