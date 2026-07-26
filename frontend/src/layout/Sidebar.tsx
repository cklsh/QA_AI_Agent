export default function Sidebar() {
  return (
    <aside className="flex h-full flex-col">

      {/* Brand */}

      <div className="border-b border-stone-200 p-6">

        <h1 className="text-xl font-semibold text-stone-900">
          AI QA Workspace
        </h1>

        <p className="mt-2 text-sm leading-6 text-stone-500">
          Turn PRDs into QA assets using local AI.
        </p>

      </div>

      {/* Documents */}

      <div className="flex-1 p-6">

        <div className="flex items-center justify-between">

          <h2 className="text-sm font-medium uppercase tracking-wide text-stone-500">
            Documents
          </h2>

        </div>

        <button
          className="
            mt-4
            w-full
            rounded-xl
            border
            border-stone-200
            bg-amber-300
            px-4
            py-3
            text-sm
            font-medium
            text-stone-900
            transition
            hover:bg-yellow-400
          "
        >
          Upload PRD
        </button>

        <div className="mt-8">

          <p className="text-sm text-stone-400">
            No documents yet
          </p>

        </div>

      </div>

    </aside>
  );
}