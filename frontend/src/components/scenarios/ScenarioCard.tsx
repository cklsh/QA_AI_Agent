interface Scenario {
    id: string;
    title: string;
    type: string;
    given: string[];
    when: string[];
    then: string[];
}

interface Props {
    scenario: Scenario;
}


export default function ScenarioCard({ scenario }: Props) {

    const type = scenario.type.trim().toLowerCase();

    const badgeStyle =
        type === "positive"
            ? "bg-green-100 text-green-700"
            : "bg-red-100 text-red-700";


    return (

        <div className="rounded-xl border border-stone-200 bg-white p-5">

            {/* Header */}
            <div className="flex items-center justify-between">

                <div>

                    <p className="text-xs text-stone-400">
                        {scenario.id}
                    </p>

                    <h3 className="text-base font-semibold text-stone-800">
                        {scenario.title}
                    </h3>

                </div>


                <span
                    className={`rounded-full px-3 py-1 text-xs font-medium ${badgeStyle}`}
                >
                    {type.charAt(0).toUpperCase() + type.slice(1)}
                </span>

            </div>



            {/* Given */}

            <div className="mt-5">

                <p className="text-sm font-bold text-stone-700">
                    Given
                </p>


                <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-stone-600">

                    {scenario.given.map((item, index) => (

                        <li key={index}>
                            {item}
                        </li>

                    ))}

                </ul>

            </div>




            {/* When */}

            <div className="mt-5">

                <p className="text-sm font-bold text-stone-700">
                    When
                </p>


                <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-stone-600">

                    {scenario.when.map((item, index) => (

                        <li key={index}>
                            {item}
                        </li>

                    ))}

                </ul>

            </div>





            {/* Then */}

            <div className="mt-5">

                <p className="text-sm font-bold text-stone-700">
                    Then
                </p>


                <ul className="mt-2 list-disc space-y-1 pl-5 text-sm text-stone-600">

                    {scenario.then.map((item, index) => (

                        <li key={index}>
                            {item}
                        </li>

                    ))}

                </ul>

            </div>


        </div>

    );
}