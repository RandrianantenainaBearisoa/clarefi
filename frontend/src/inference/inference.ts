import * as ort from 'onnxruntime-web'

ort.env.wasm.wasmPaths = 'https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/';

export class Inference {
    private session: ort.InferenceSession

    private constructor(session: ort.InferenceSession) {
        this.session = session
    }

    public static async initialize(): Promise<Inference> {
        try {
            const session = await ort.InferenceSession.create('/assets/model_artifact/current_model.onnx');
            return new Inference(session);
        } catch (error) {
            console.error("Error when loading the onnx model :", error);
            throw new Error("Cannot initialize prediction session.");
        }
    }

    public async predict(comment: string) {
        try {
            const textTensor = new ort.Tensor('string', [comment], [1, 1]);
            const feeds = { text_input: textTensor };
            const firstOutputName = this.session.outputNames[0];
            if (!firstOutputName) {
                throw new Error("Le modèle ONNX chargé ne possède aucune porte de sortie valide.");
            }
            const results = await this.session.run(feeds, [firstOutputName]);
            return Number(results[firstOutputName]?.data[0]); 
        } catch (error) {
            console.error("Error during inference:", error);
            throw error;
        }
    }
}