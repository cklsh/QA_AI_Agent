import { useState } from "react";

interface Props {
    onUpload(file: File): Promise<void>;
    loading: boolean;
}

export default function UploadBox({
    onUpload,
    loading,
}: Props) {

    const [file, setFile] = useState<File | null>(null);

    async function handleProcess() {

        if (!file) return;

        await onUpload(file);

    }

    return (

        <div className="rounded-xl border border-stone-200 bg-white p-8">

            <h2 className="text-xl font-semibold text-stone-900">
                New Analysis
            </h2>

            <p className="mt-2 text-sm text-stone-500">
                Upload a PRD PDF to start analysis.
            </p>
            <div className="mt-6 flex flex-col gap-3">
              <input
                id="pdf-upload"
                type="file"
                accept=".pdf"
                className="hidden"
                onChange={(e) => {
                    if (!e.target.files?.length) return;
                    setFile(e.target.files[0]);
                }}
            />

            <label
                htmlFor="pdf-upload"
                className={`
                    inline-flex
                    w-full
                    cursor-pointer
                    rounded-xl
                    border
                    border-stone-300
                    bg-white
                    px-5
                    py-2.5
                    text-sm
                    font-medium
                    transition
                    hover:bg-stone-100
                    ${loading ? "pointer-events-none opacity-50" : ""}
              `}
            >
                Browse PDF
            </label>

            <div className="mt-3 rounded-lg border border-stone-200 bg-stone-50 px-4 py-3">

                <p className="text-xs uppercase tracking-wide text-stone-400">
                    Selected File
                </p>

                <p className="mt-1 text-sm font-medium text-stone-700">
                    {file ? file.name : "No PDF selected yet."}
                </p>

            </div>

            <button
                disabled={!file || loading}
                onClick={handleProcess}
                className="
                    w-full
                    rounded-xl
                    bg-amber-300
                    px-6
                    py-3
                    font-medium
                    transition
                    hover:bg-yellow-400
                    disabled:opacity-50
                "
            >
                {loading ? "Processing..." : "Process Document"}
            </button>
          </div>

        </div>

    );

}