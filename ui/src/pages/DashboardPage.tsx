import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api/client';
import { ENTITY_CONFIGS, CATEGORY_ORDER } from '../config/entities';
import { useActivity } from '../hooks/useActivity';

interface Stat {
  key: string;
  label: string;
  count: number | null;
  error?: boolean;
}

const ACTION_ICON: Record<string, string> = {
  created: '＋',
  updated: '✎',
  deleted: '✕',
};
const ACTION_CLASS: Record<string, string> = {
  created: 'act-created',
  updated: 'act-updated',
  deleted: 'act-deleted',
};

function formatRelative(iso: string): string {
  const diff = (Date.now() - new Date(iso).getTime()) / 1000;
  if (diff < 60) return 'just now';
  if (diff < 3600) return `${Math.floor(diff / 60)}m ago`;
  if (diff < 86400) return `${Math.floor(diff / 3600)}h ago`;
  return `${Math.floor(diff / 86400)}d ago`;
}

export function DashboardPage() {
  const [stats, setStats] = useState<Stat[]>([]);
  const [loading, setLoading] = useState(true);
  const { entries, clear } = useActivity();
  const abortRef = useRef<AbortController | null>(null);

  useEffect(() => {
    abortRef.current?.abort();
    const ac = new AbortController();
    abortRef.current = ac;

    const initial = ENTITY_CONFIGS.map((e) => ({
      key: e.key,
      label: e.label,
      count: null as number | null,
    }));
    setStats(initial);
    setLoading(true);

    let done = 0;
    ENTITY_CONFIGS.forEach((entity) => {
      api
        .list(entity.apiPath)
        .then((rows) => {
          if (ac.signal.aborted) return;
          setStats((prev) =>
            prev.map((s) =>
              s.key === entity.key ? { ...s, count: rows.length } : s,
            ),
          );
        })
        .catch(() => {
          if (ac.signal.aborted) return;
          setStats((prev) =>
            prev.map((s) =>
              s.key === entity.key ? { ...s, count: 0, error: true } : s,
            ),
          );
        })
        .finally(() => {
          done++;
          if (done === ENTITY_CONFIGS.length) setLoading(false);
        });
    });

    return () => ac.abort();
  }, []);

  const totalRecords = stats.reduce((sum, s) => sum + (s.count ?? 0), 0);
  const loadedCount = stats.filter((s) => s.count !== null).length;

  // Group stats by category
  const grouped: Record<string, Stat[]> = {};
  for (const cat of CATEGORY_ORDER) {
    const keys = ENTITY_CONFIGS.filter((e) => e.category === cat).map((e) => e.key);
    const catStats = stats.filter((s) => keys.includes(s.key));
    if (catStats.length > 0) grouped[cat] = catStats;
  }

  return (
    <div className="dashboard">
      <div className="dash-header">
        <div>
          <h1>Dashboard</h1>
          <p className="dash-subtitle">
            Intel Excalibur — {loading ? `Loading ${loadedCount}/${ENTITY_CONFIGS.length}…` : `${totalRecords.toLocaleString()} total records across ${ENTITY_CONFIGS.length} entities`}
          </p>
        </div>
      </div>

      {/* Summary strip */}
      <div className="summary-strip">
        <div className="summary-card">
          <span className="summary-number">{totalRecords.toLocaleString()}</span>
          <span className="summary-label">Total Records</span>
        </div>
        <div className="summary-card">
          <span className="summary-number">{ENTITY_CONFIGS.length}</span>
          <span className="summary-label">Entity Types</span>
        </div>
        <div className="summary-card">
          <span className="summary-number">{entries.length}</span>
          <span className="summary-label">Recent Operations</span>
        </div>
        <div className="summary-card">
          <span className="summary-number">{entries.filter((e) => e.action === 'created').length}</span>
          <span className="summary-label">Records Created</span>
        </div>
      </div>

      <div className="dash-body">
        {/* Stats grid */}
        <div className="dash-main">
          {Object.entries(grouped).map(([cat, catStats]) => (
            <section key={cat} className="stat-section">
              <h3 className="stat-section-title">{cat}</h3>
              <div className="stat-grid">
                {catStats.map((s) => (
                  <Link
                    key={s.key}
                    to={`/entity/${s.key}`}
                    className={`stat-card ${s.error ? 'stat-error' : ''}`}
                  >
                    <div className="stat-count">
                      {s.count === null ? (
                        <span className="stat-loading">…</span>
                      ) : (
                        s.count.toLocaleString()
                      )}
                    </div>
                    <div className="stat-label">{s.label}</div>
                  </Link>
                ))}
              </div>
            </section>
          ))}
        </div>

        {/* Activity feed */}
        <aside className="activity-feed">
          <div className="feed-header">
            <h3>Recent Activity</h3>
            {entries.length > 0 && (
              <button className="btn-link" onClick={clear}>
                Clear
              </button>
            )}
          </div>
          {entries.length === 0 ? (
            <div className="feed-empty">No activity yet. Start creating records.</div>
          ) : (
            <ul className="feed-list">
              {entries.slice(0, 25).map((e) => (
                <li key={e.id} className="feed-item">
                  <span className={`feed-icon ${ACTION_CLASS[e.action]}`}>
                    {ACTION_ICON[e.action]}
                  </span>
                  <div className="feed-body">
                    <Link to={`/entity/${e.entityKey}`} className="feed-entity">
                      {e.entityLabel}
                    </Link>
                    <span className="feed-name">{e.recordName || e.recordId.slice(0, 8)}</span>
                    <span className={`feed-action ${ACTION_CLASS[e.action]}`}>
                      {e.action}
                    </span>
                  </div>
                  <span className="feed-time">{formatRelative(e.timestamp)}</span>
                </li>
              ))}
            </ul>
          )}
        </aside>
      </div>
    </div>
  );
}
