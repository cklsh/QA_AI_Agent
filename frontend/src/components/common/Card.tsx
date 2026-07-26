import type { ReactNode } from "react";

interface CardProps {
  title: string;
  children?: ReactNode;
}

export default function Card({
  title,
  children,
}: CardProps) {
  return (
    <section className="rounded-xl border border-stone-200 bg-white p-6 shadow-none">

      <h2 className="text-lg font-semibold text-stone-900">
        {title}
      </h2>

      <div className="mt-4">
        {children}
      </div>

    </section>
  );
}