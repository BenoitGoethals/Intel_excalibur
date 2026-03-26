import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import { TopNav } from './components/TopNav';
import { DashboardPage } from './pages/DashboardPage';
import { EntityPage } from './pages/EntityPage';

export function App() {
  return (
    <BrowserRouter>
      <div className="app-shell">
        <TopNav />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<DashboardPage />} />
            <Route path="/entity/:entityKey" element={<EntityPage />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
