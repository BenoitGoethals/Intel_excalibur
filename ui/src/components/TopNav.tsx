import { useEffect, useRef, useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { ENTITY_CONFIGS, groupedEntities, type EntityConfig } from '../config/entities';

const CATEGORY_ICONS: Record<string, string> = {
  Intelligence:          '🔍',
  HUMINT:                '👤',
  'Cyber & OSINT':       '💻',
  'SIGINT / MASINT':     '📡',
  'GEO & IMINT':         '🗺',
  'Financial & Counter': '💰',
  'Medical & Tech':      '⚕',
  'Social & News':       '📰',
  'People & Sources':    '🧑',
  Cases:                 '📁',
  Operations:            '⚔',
  Management:            '📋',
};

// Categories with their own separate menus
const CASES_CATEGORY = 'Cases';
const INVESTIGATION_CATEGORY = 'Investigations';

// ── Grouped mega-dropdown (shows category sections inside) ────────────────
interface MegaDropdownProps {
  label: string;
  icon: string;
  groups: Record<string, EntityConfig[]>;
  isOpen: boolean;
  onToggle: () => void;
  onClose: () => void;
}

function MegaDropdown({ label, icon, groups, isOpen, onToggle, onClose }: MegaDropdownProps) {
  const ref = useRef<HTMLDivElement>(null);
  const location = useLocation();

  const allEntities = Object.values(groups).flat();
  const hasActive = allEntities.some((e) => location.pathname === `/entity/${e.key}`);

  useEffect(() => {
    if (!isOpen) return;
    const handler = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) onClose();
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, [isOpen, onClose]);

  return (
    <div ref={ref} className="topmenu-item">
      <button
        className={`topmenu-btn ${isOpen ? 'open' : ''} ${hasActive ? 'has-active' : ''}`}
        onClick={onToggle}
      >
        <span className="tmenu-icon">{icon}</span>
        <span>{label}</span>
        <span className={`caret ${isOpen ? 'up' : ''}`}>▾</span>
      </button>

      {isOpen && (
        <div className="dropdown-panel mega-panel">
          {Object.entries(groups).map(([cat, entities]) => (
            <div key={cat} className="dropdown-section">
              <div className="dropdown-section-header">
                <span>{CATEGORY_ICONS[cat] ?? '▸'}</span>
                <span>{cat}</span>
              </div>
              {entities.map((e) => (
                <NavLink
                  key={e.key}
                  to={`/entity/${e.key}`}
                  className={({ isActive }) => `dropdown-item ${isActive ? 'active' : ''}`}
                  onClick={onClose}
                >
                  <span className="dropdown-dot" />
                  {e.label}
                </NavLink>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

// ── Simple flat dropdown (for Investigations) ─────────────────────────────
interface SimpleDropdownProps {
  label: string;
  icon: string;
  entities: EntityConfig[];
  isOpen: boolean;
  onToggle: () => void;
  onClose: () => void;
}

function SimpleDropdown({ label, icon, entities, isOpen, onToggle, onClose }: SimpleDropdownProps) {
  const ref = useRef<HTMLDivElement>(null);
  const location = useLocation();

  const hasActive = entities.some((e) => location.pathname === `/entity/${e.key}`);

  useEffect(() => {
    if (!isOpen) return;
    const handler = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) onClose();
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, [isOpen, onClose]);

  return (
    <div ref={ref} className="topmenu-item">
      <button
        className={`topmenu-btn ${isOpen ? 'open' : ''} ${hasActive ? 'has-active' : ''}`}
        onClick={onToggle}
      >
        <span className="tmenu-icon">{icon}</span>
        <span>{label}</span>
        <span className={`caret ${isOpen ? 'up' : ''}`}>▾</span>
      </button>

      {isOpen && (
        <div className="dropdown-panel">
          <div className="dropdown-header">{label}</div>
          {entities.map((e) => (
            <NavLink
              key={e.key}
              to={`/entity/${e.key}`}
              className={({ isActive }) => `dropdown-item ${isActive ? 'active' : ''}`}
              onClick={onClose}
            >
              <span className="dropdown-dot" />
              {e.label}
            </NavLink>
          ))}
        </div>
      )}
    </div>
  );
}

// ── Top nav ───────────────────────────────────────────────────────────────
export function TopNav() {
  const [open, setOpen] = useState<string | null>(null);

  const toggle = (key: string) => setOpen((prev) => (prev === key ? null : key));
  const close = () => setOpen(null);

  // Split entities into menus
  const allGroups = groupedEntities();
  const intelGroups: Record<string, EntityConfig[]> = {};
  for (const [cat, entities] of Object.entries(allGroups)) {
    if (cat !== INVESTIGATION_CATEGORY && cat !== CASES_CATEGORY) intelGroups[cat] = entities;
  }
  const casesEntities = ENTITY_CONFIGS.filter(
    (e) => e.category === CASES_CATEGORY,
  );
  const investigationEntities = ENTITY_CONFIGS.filter(
    (e) => e.category === INVESTIGATION_CATEGORY,
  );

  return (
    <header className="topnav">
      <div className="topnav-brand">
        <span className="brand-sword">⚔</span>
        <span className="brand-name">Intel Excalibur</span>
      </div>

      <nav className="topnav-menu">
        {/* Dashboard — always first, direct link */}
        <NavLink
          to="/"
          end
          className={({ isActive }) => `topmenu-btn dashboard-btn ${isActive ? 'has-active' : ''}`}
          onClick={close}
        >
          <span className="tmenu-icon">◈</span>
          Dashboard
        </NavLink>

        {/* All Intel — consolidated view */}
        <NavLink
          to="/all-intel"
          className={({ isActive }) => `topmenu-btn ${isActive ? 'has-active' : ''}`}
          onClick={close}
        >
          <span className="tmenu-icon">📊</span>
          All Intel
        </NavLink>

        {/* Intel — one menu, all entity categories as sections */}
        <MegaDropdown
          label="Intel"
          icon="🗂"
          groups={intelGroups}
          isOpen={open === 'intel'}
          onToggle={() => toggle('intel')}
          onClose={close}
        />

        {/* Cases — separate menu */}
        <SimpleDropdown
          label="Cases"
          icon="📁"
          entities={casesEntities}
          isOpen={open === 'cases'}
          onToggle={() => toggle('cases')}
          onClose={close}
        />

        {/* Investigations — separate menu */}
        <SimpleDropdown
          label="Investigations"
          icon="🔎"
          entities={investigationEntities}
          isOpen={open === 'investigations'}
          onToggle={() => toggle('investigations')}
          onClose={close}
        />
      </nav>

      <div className="topnav-right">
        <span className="version-badge">v0.1.0</span>
      </div>
    </header>
  );
}
