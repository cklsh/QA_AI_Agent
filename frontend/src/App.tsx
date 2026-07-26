// 


import AppLayout from "./layout/AppLayout";
import Dashboard from "./pages/Dashboard";
import Sidebar from "./layout/Sidebar";
import Header from "./layout/Header";

export default function App() {
  return (
    <AppLayout
      // sidebar={<Sidebar />}
      header={<Header />}
    >
      <Dashboard />
    </AppLayout>
  );
}