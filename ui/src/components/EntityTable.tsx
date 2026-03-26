import { useNavigate } from 'react-router-dom';
import type { ApiRecord } from '../api/client';
import type { EntityConfig } from '../config/entities';

interface Props {
  config: EntityConfig;
  rows: ApiRecord[];
  loading: boolean;
  error: string | null;
  onEdit: (row: ApiRecord) => void;
  onDelete: (row: ApiRecord) => void;
  onPhotos?: (row: ApiRecord) => void;
}

function cellValue(val: unknown): string {
  if (val === null || val === undefined) return '—';
  if (typeof val === 'boolean') return val ? '✓' : '✗';
  if (Array.isArray(val)) return val.slice(0, 3).join(', ') + (val.length > 3 ? '…' : '');
  const s = String(val);
  // truncate ISO dates
  if (/^\d{4}-\d{2}-\d{2}T/.test(s)) return s.slice(0, 10);
  return s.length > 60 ? s.slice(0, 57) + '…' : s;
}

export function EntityTable({ config, rows, loading, error, onEdit, onDelete, onPhotos }: Props) {
  const navigate = useNavigate();
  const columns = config.fields.filter((f) => f.tableColumn);
  const isCase = config.key === 'intel-cases';

  if (loading) {
    return (
      <div className="table-state">
        <div className="spinner" />
        <span>Loading…</span>
      </div>
    );
  }

  if (error) {
    return <div className="table-state error">{error}</div>;
  }

  if (rows.length === 0) {
    return (
      <div className="table-state empty">
        No {config.label} records found.
      </div>
    );
  }

  return (
    <div className="table-wrapper">
      <table className="data-table">
        <thead>
          <tr>
            <th style={{ width: '80px' }}>ID</th>
            {columns.map((c) => (
              <th key={c.name}>{c.label}</th>
            ))}
            <th style={{ width: '120px' }}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={String(row.id)}>
              <td className="id-cell" title={String(row.id ?? '')}>
                {String(row.id ?? '').slice(0, 8)}
              </td>
              {columns.map((c) => (
                <td key={c.name}>{cellValue(row[c.name])}</td>
              ))}
              <td>
                <div className="row-actions">
                  {isCase && (
                    <button
                      className="btn-icon view"
                      onClick={() => navigate(`/entity/intel-cases/${row.id}`)}
                      title="View case & linked intel"
                    >
                      ⬈
                    </button>
                  )}
                  {onPhotos && (
                    <button
                      className="btn-icon photos"
                      onClick={() => onPhotos(row)}
                      title="Photos"
                    >
                      📷
                    </button>
                  )}
                  <button
                    className="btn-icon edit"
                    onClick={() => onEdit(row)}
                    title="Edit"
                  >
                    ✎
                  </button>
                  <button
                    className="btn-icon delete"
                    onClick={() => onDelete(row)}
                    title="Delete"
                  >
                    ✕
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
