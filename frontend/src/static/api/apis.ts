import { postJson } from "../services/services";

export async function predict(comment: string) {
    const payload = {
        input: comment
    }
    const prediction = postJson("http://127.0.0.1:8000/predict", payload)
    return prediction
}