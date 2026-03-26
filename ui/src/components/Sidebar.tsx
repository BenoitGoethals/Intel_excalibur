import { NavLink, useLocation } from 'react-router-dom';
import { groupedEntities } from '../config/entities';

const CATEGORY_ICONS: Record<string, string> = {
  Intelligence: '🔍',
  HUMINT: '👤',
  'Cyber & OSINT': '💻',
  'SIGINT / MASINT': '📡',
  'GEO & IMINT': '🗺',
  'Financial & Counter': '💰',
  'Medical & Tech': '⚕',
  'Social & News': '📰',
  'People & Sources': '🧑‍🤝‍🧑',
  Operations: '⚔',
  Management: '📋',
};

export function Sidebar() {
  const location = useLocation();
  const groups = groupedEntities();

  return (
    <nav className="sidebar">
      <div className="sidebar-brand">
        <span className="brand-icon">⚔</span>
        <span className="brand-text">Intel Excalibur</span>
      </div>

      <NavLink to="/" end className={({ isActive }) => `nav-item nav-dashboard ${isActive ? 'active' : ''}`}>
        <span className="nav-icon">◈</span>
        <span>Dashboard</span>
      </NavLink>

      <div className="nav-divider" />

      {Object.entries(groups).map(([cat, entities]) => (
        <div key={cat} className="nav-group">
          <div className="nav-group-label">
            <span>{CATEGORY_ICONS[cat] ?? '▸'}</span>
            <span>{cat}</span>
          </div>
          {entities.map((e) => (
            <NavLink
              key={e.key}
              to={`/entity/${e.key}`}
              className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
            >
              <span className="nav-item-dot" />
              <span>{e.label}</span>
            </NavLink>
          ))}
        </div>
      ))}

      <div className="sidebar-footer">
        <span className="version-tag">v0.1.0</span>
      </div>
    </nav>
  );
}
