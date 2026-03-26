import { useCallback, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { api, type ApiRecord } from '../api/client';
import { EntityForm } from '../components/EntityForm';
import { EntityTable } from '../components/EntityTable';
import { PhotoUploadField } from '../components/PhotoUploadField';
import { getEntityByKey } from '../config/entities';
import { useActivity } from '../hooks/useActivity';

export function EntityPage() {
  const { entityKey } = useParams<{ entityKey: string }>();
  const config = getEntityByKey(entityKey ?? '');
  const { log } = useActivity();

  const [rows, setRows] = useState<ApiRecord[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [formOpen, setFormOpen] = useState(false);
  const [editing, setEditing] = useState<ApiRecord | undefined>();
  const [search, setSearch] = useState('');
  const [deleteConfirm, setDeleteConfirm] = useState<ApiRecord | null>(null);
  const [photosRow, setPhotosRow] = useState<ApiRecord | null>(null);

  const load = useCallback(async () => {
    if (!config) return;
    setLoading(true);
    setError(null);
    try {
      const data = await api.list(config.apiPath);
      setRows(data);
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Failed to load');
    } finally {
      setLoading(false);
    }
  }, [config]);

  useEffect(() => {
    setRows([]);
    setSearch('');
    setFormOpen(false);
    setEditing(undefined);
    setPhotosRow(null);
    load();
  }, [load]);

  if (!config) {
    return <div className="page-error">Entity "{entityKey}" not found.</div>;
  }

  const displayName = (row: ApiRecord) =>
    String(row[config.nameField] ?? row.id ?? '').slice(0, 40);

  const handleSave = async (data: ApiRecord) => {
    if (editing) {
      const updated = await api.update(config.apiPath, String(editing.id), data);
      setRows((prev) =>
        prev.map((r) => (r.id === editing.id ? updated : r)),
      );
      log({
        entityKey: config.key,
        entityLabel: config.label,
        recordId: String(editing.id),
        recordName: displayName(updated),
        action: 'updated',
      });
    } else {
      const created = await api.create(config.apiPath, data);
      setRows((prev) => [created, ...prev]);
      log({
        entityKey: config.key,
        entityLabel: config.label,
        recordId: String(created.id),
        recordName: displayName(created),
        action: 'created',
      });
    }
    setFormOpen(false);
    setEditing(undefined);
  };

  const handleDelete = async (row: ApiRecord) => {
    await api.remove(config.apiPath, String(row.id));
    setRows((prev) => prev.filter((r) => r.id !== row.id));
    log({
      entityKey: config.key,
      entityLabel: config.label,
      recordId: String(row.id),
      recordName: displayName(row),
      action: 'deleted',
    });
    setDeleteConfirm(null);
  };

  const filtered = search.trim()
    ? rows.filter((r) =>
        JSON.stringify(r).toLowerCase().includes(search.toLowerCase()),
      )
    : rows;

  return (
    <div className="entity-page">
      <div className="page-header">
        <div>
          <h1>{config.label}</h1>
          <span className="record-count">{rows.length} records</span>
        </div>
        <div className="page-header-actions">
          <input
            className="search-input"
            type="search"
            placeholder="Search..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <button
            className="btn btn-primary"
            onClick={() => {
              setEditing(undefined);
              setFormOpen(true);
            }}
          >
            + New {config.label}
          </button>
          <button className="btn btn-secondary" onClick={load} title="Refresh">
            ↻
          </button>
        </div>
      </div>

      <EntityTable
        config={config}
        rows={filtered}
        loading={loading}
        error={error}
        onEdit={(row) => {
          setEditing(row);
          setFormOpen(true);
        }}
        onDelete={(row) => setDeleteConfirm(row)}
        onPhotos={(row) => setPhotosRow(row)}
      />

      {formOpen && (
        <EntityForm
          config={config}
          initial={editing}
          onSave={handleSave}
          onCancel={() => {
            setFormOpen(false);
            setEditing(undefined);
          }}
        />
      )}

      {/* Photo modal */}
      {photosRow && (
        <div className="modal-overlay" onClick={() => setPhotosRow(null)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h2>Photos — {displayName(photosRow)}</h2>
              <button className="btn-icon" onClick={() => setPhotosRow(null)}>✕</button>
            </div>
            <div className="entity-form">
              <PhotoUploadField
                entityType={config.key}
                entityId={String(photosRow.id)}
              />
            </div>
          </div>
        </div>
      )}

      {deleteConfirm && (
        <div className="modal-overlay" onClick={() => setDeleteConfirm(null)}>
          <div className="confirm-dialog" onClick={(e) => e.stopPropagation()}>
            <h3>Delete {config.label}?</h3>
            <p>
              <strong>{displayName(deleteConfirm)}</strong> will be permanently deleted.
            </p>
            <div className="form-actions">
              <button
                className="btn btn-secondary"
                onClick={() => setDeleteConfirm(null)}
              >
                Cancel
              </button>
              <button
                className="btn btn-danger"
                onClick={() => handleDelete(deleteConfirm)}
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
