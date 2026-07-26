import { useState } from "react";

import UploadBox from "../components/documents/UploadBox";
import Card from "../components/common/Card";
import { LoaderCircle } from "lucide-react";

import { uploadPdf } from "../services/api";
import ScenarioList from "../components/scenarios/ScenarioList";
import AnalysisSummary from "../components/analysis/AnalysisSummary";

export default function Dashboard() {

    // =====================
    // State
    // =====================

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState<any>(null);

    const [error, setError] = useState<string | null>(null);

    const scenarioCount =
    result?.data?.scenarios?.scenarios?.length ?? 0;


    // =====================
    // Functions
    // =====================

    async function handleUpload(file: File) {

        try {

            setLoading(true);

            setError(null);

            const response = await uploadPdf(file);

            setResult(response);

        } catch (err) {

            console.error(err);

            setError("Failed to process document.");

        } finally {

            setLoading(false);

        }

    }


    // =====================
    // UI
    // =====================

    return (

        <div className="space-y-8">

            {/* Upload */}
            <UploadBox
                loading={loading}
                onUpload={handleUpload}
            />

            {/* Loading */}
            {loading ? (
                <>
                    <LoaderCircle
                        className="animate-spin flex items-center justify-center"
                    />
                </>
            ) : (
                "Process Document"
            )}

            {/* Error */}
            {error && (
                <p>{error}</p>
            )}

            {/* Temporary Debug */}
            {
            result && (

            <AnalysisSummary

                feature={
                    result.data.scenarios.feature
                }

                scenarios={
                    result.data.scenarios.scenarios
                }

            />

            )}
            <Card title="Test Cases">

                <ScenarioList
                    scenarios={
                        result?.data?.scenarios?.scenarios || []
                    }
                />

            </Card>

            <Card title="Summary">
                <p>Upload a PRD to generate a summary.</p>
            </Card>

            <Card title="Automation">
                <p>No automation generated.</p>
            </Card>

        </div>

    );

}