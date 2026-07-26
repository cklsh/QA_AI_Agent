import ScenarioCard from "./ScenarioCard";

interface Scenario {
    id: string;
    title: string;
    type: string;
    given: string[];
    when: string[];
    then: string[];
}


interface Props {
    scenarios: Scenario[];
}


export default function ScenarioList({
    scenarios,
}: Props) {


    if (!scenarios || scenarios.length === 0) {

        return (
            <p className="text-sm text-stone-500">
                No scenarios generated.
            </p>
        );

    }


    return (

        <div className="space-y-4">

            {scenarios.map((scenario) => (

                <ScenarioCard
                    key={scenario.id}
                    scenario={scenario}
                />

            ))}

        </div>

    );
}