export default function Header() {
  return (
    <header className="flex h-full items-center justify-between px-8 border-b border-stone-100 bg-white/80 backdrop-blur">
      <div>

        <h1 className="text-2xl font-semibold text-stone-900">
          Requirement Analysis
        </h1>

        <p className="mt-1 text-sm text-stone-500">
          Analyze requirements and generate QA artifacts.
        </p>

      </div>

    </header>
  );
}