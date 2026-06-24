export async function postJson<T = unknown, U = unknown>(url: string, payload?: U, init: RequestInit = {}): Promise<T | null> {
    try {
        const response = await fetch(
            url,
            {
                ...init,
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: payload ? JSON.stringify(payload) : undefined
            }
        );

        if (!response.ok) {
            throw new Error(`Error : ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
        return null;
    }
}