export interface Scenario {
    id: string;
    name: string;
    type: "positive" | "negative" | "edge";
    businessRule?: string;
    priority?: "High" | "Medium" | "Low";
    steps: string[];
    expected_result: string;
}
export interface ScenarioResponse {
  feature: string;
  scenarios: Scenario[];
}

export interface TestCase {
    id: string;
    scenarioId?: string;
    title: string;
    precondition?: string;
    testData?: string;
    steps: string[];
    expected_result: string;
    status?: "AI Generated" | "Edited";
}

export interface TestCaseResponse {
  feature?: string;
  test_cases: TestCase[];
}

export interface PipelineResult {
  scenarios: ScenarioResponse | null;
  test_cases: TestCaseResponse | null;
  code: string | null;
  issues: string[];
}

export interface GenerateResponse {
  success: boolean;
  filename?: string;
  extracted_length?: number;
  data: PipelineResult;
}

export interface Document {
    id: string;
    name: string;
    uploadedAt: string;
    summary?: string;
    scenarios?: Scenario[];
    testCases?: TestCase[];
}