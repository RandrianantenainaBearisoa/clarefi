import { ref } from "vue";

const isLoading = ref(false)

export const useLoading = () => {
    return {
        isLoading,
        start_loading : () => {isLoading.value = true; },
        stop_loading : () => {isLoading.value = false; }
    };
};