interface Scenario {
    id: string;
    title: string;
    type: string;
}


interface Props {
    feature: string;
    scenarios: Scenario[];
}


export default function AnalysisSummary({
    feature,
    scenarios,
}: Props) {


    const positiveCount =
        scenarios.filter(
            (scenario) =>
                scenario.type.toLowerCase() === "positive"
        ).length;


    const negativeCount =
        scenarios.filter(
            (scenario) =>
                scenario.type.toLowerCase() === "negative"
        ).length;



    return (

        <div className="rounded-xl border border-stone-200 bg-white p-6">

            <p className="text-sm text-stone-500">
                Analysis Complete
            </p>


            <h2 className="mt-1 text-xl font-semibold text-stone-800">
                {feature}
            </h2>


            <p className="mt-3 text-sm text-stone-600">
                {scenarios.length} test cases generated
            </p>



            <div className="mt-5 flex gap-3">


                <div className="rounded-lg bg-green-100 px-4 py-2">

                    <p className="text-xs text-green-700">
                        Positive
                    </p>

                    <p className="text-lg font-semibold text-green-700">
                        {positiveCount}
                    </p>

                </div>



                <div className="rounded-lg bg-red-100 px-4 py-2">

                    <p className="text-xs text-red-700">
                        Negative
                    </p>

                    <p className="text-lg font-semibold text-red-700">
                        {negativeCount}
                    </p>

                </div>


            </div>

        </div>

    );

}