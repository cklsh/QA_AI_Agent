interface AppLayoutProps {
  sidebar: React.ReactNode;
  header: React.ReactNode;
  children: React.ReactNode;
}

export default function AppLayout({
  sidebar,
  header,
  children,
}: AppLayoutProps) {
  return (
    <div className="flex h-screen bg-stone-50">

      {/* Sidebar */}
      {/* <aside className="w-72 border-r border-stone-200 bg-white">
        {sidebar}
      </aside> */}

      {/* Main */}
      <div className="flex flex-1 flex-col">

        {/* Header */}
        <header className="h-16 border-b border-stone-200 bg-white">
          {header}
        </header>

        {/* Content */}
        <main className="flex-1 overflow-auto p-8">
          {children}
        </main>

      </div>

    </div>
  );
}