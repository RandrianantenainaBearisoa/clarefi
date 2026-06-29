import { postJson } from "../services/services";
import { API_URL } from "../constants/constants";

export async function predict(comment: string) {
    const payload = {
        input: comment
    }
    const endpoint = "/predict"
    const prediction = postJson(`"${API_URL}${endpoint}"`, payload)
    return prediction
}