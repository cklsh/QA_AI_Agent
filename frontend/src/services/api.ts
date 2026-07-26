import axios from "axios";
import type { GenerateResponse } from "../types/qa";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export async function uploadPdf(
    file: File
): Promise<GenerateResponse> {

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post<GenerateResponse>(
        "/generate-pdf",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}

export default api;