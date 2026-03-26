import React, { useEffect, useState } from 'react';
import { api, type ApiRecord } from '../api/client';
import type { EntityConfig, FieldDef } from '../config/entities';

// ── Remote option shape ───────────────────────────────────────────────────
interface RemoteOption { id: string; label: string; }

function useRemoteOptions(source?: string, labelField?: string) {
  const [options, setOptions] = useState<RemoteOption[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!source) return;
    setLoading(true);
    api.list(source)
      .then((rows) =>
        setOptions(
          rows.map((r) => ({
            id: String(r.id ?? ''),
            label: String(r[labelField ?? 'name'] ?? r.id ?? ''),
          })),
        ),
      )
      .catch(() => setOptions([]))
      .finally(() => setLoading(false));
  }, [source, labelField]);

  return { options, loading };
}

// ── Single remote select ──────────────────────────────────────────────────
interface RemoteSelectProps {
  field: FieldDef;
  value: string;
  onChange: (id: string, label: string) => void;
}

function RemoteSelectField({ field, value, onChange }: RemoteSelectProps) {
  const { options, loading } = useRemoteOptions(field.remoteSource, field.remoteLabel);

  return (
    <select
      value={value}
      onChange={(e) => {
        const opt = options.find((o) => o.id === e.target.value);
        onChange(e.target.value, opt?.label ?? '');
      }}
      disabled={loading}
    >
      <option value="">{loading ? 'Loading…' : '— select —'}</option>
      {options.map((o) => (
        <option key={o.id} value={o.id}>{o.label}</option>
      ))}
    </select>
  );
}

// ── Multi remote select (checkbox list) ───────────────────────────────────
interface RemoteMultiProps {
  field: FieldDef;
  value: string[];
  onChange: (ids: string[]) => void;
}

function RemoteMultiSelect({ field, value, onChange }: RemoteMultiProps) {
  const { options, loading } = useRemoteOptions(field.remoteSource, field.remoteLabel);
  const selected = new Set(value);

  const toggle = (id: string) => {
    const next = new Set(selected);
    next.has(id) ? next.delete(id) : next.add(id);
    onChange(Array.from(next));
  };

  if (loading) return <div className="multiselect-loading">Loading…</div>;
  if (options.length === 0) return <div className="multiselect-empty">No records found</div>;

  return (
    <div className="multiselect-list">
      {options.map((o) => (
        <label key={o.id} className={`multiselect-item ${selected.has(o.id) ? 'checked' : ''}`}>
          <input
            type="checkbox"
            checked={selected.has(o.id)}
            onChange={() => toggle(o.id)}
          />
          <span>{o.label}</span>
        </label>
      ))}
    </div>
  );
}

// ── Form state helpers ────────────────────────────────────────────────────
function emptyRecord(fields: FieldDef[]): ApiRecord {
  const rec: ApiRecord = {};
  for (const f of fields) {
    if (f.type === 'boolean') rec[f.name] = false;
    else if (f.type === 'number' || f.type === 'decimal') rec[f.name] = '';
    else if (f.type === 'tags') rec[f.name] = '';
    else if (f.type === 'remote-multiselect') rec[f.name] = [];
    else rec[f.name] = '';
  }
  return rec;
}

function toFormState(record: ApiRecord, fields: FieldDef[]): ApiRecord {
  const out: ApiRecord = {};
  for (const f of fields) {
    const v = record[f.name];
    if (f.type === 'boolean') {
      out[f.name] = Boolean(v);
    } else if (f.type === 'tags') {
      out[f.name] = Array.isArray(v) ? (v as string[]).join(', ') : String(v ?? '');
    } else if (f.type === 'datetime') {
      out[f.name] = v ? String(v).slice(0, 16) : '';
    } else if (f.type === 'remote-multiselect') {
      out[f.name] = Array.isArray(v) ? v : [];
    } else {
      out[f.name] = v !== undefined && v !== null ? String(v) : '';
    }
  }
  return out;
}

function fromFormState(state: ApiRecord, fields: FieldDef[]): ApiRecord {
  const out: ApiRecord = {};
  for (const f of fields) {
    const v = state[f.name];
    if (f.type === 'boolean') {
      out[f.name] = Boolean(v);
    } else if (f.type === 'number') {
      out[f.name] = v === '' ? 0 : Number(v);
    } else if (f.type === 'decimal') {
      out[f.name] = v === '' ? '0.0' : String(v);
    } else if (f.type === 'tags') {
      out[f.name] = String(v ?? '').split(',').map((s) => s.trim()).filter(Boolean);
    } else if (f.type === 'datetime') {
      out[f.name] = v ? String(v) : null;
    } else if (f.type === 'remote-multiselect') {
      out[f.name] = Array.isArray(v) ? v : [];
    } else {
      out[f.name] = v === '' ? null : v;
    }
  }
  return out;
}

// ── Main form component ───────────────────────────────────────────────────
interface Props {
  config: EntityConfig;
  initial?: ApiRecord;
  onSave: (data: ApiRecord) => Promise<void>;
  onCancel: () => void;
}

export function EntityForm({ config, initial, onSave, onCancel }: Props) {
  const [state, setState] = useState<ApiRecord>(() =>
    initial ? toFormState(initial, config.fields) : emptyRecord(config.fields),
  );
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setState(initial ? toFormState(initial, config.fields) : emptyRecord(config.fields));
    setError(null);
  }, [initial, config]);

  const set = (name: string, value: unknown) =>
    setState((prev) => ({ ...prev, [name]: value }));

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true);
    setError(null);
    try {
      await onSave(fromFormState(state, config.fields));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Save failed');
    } finally {
      setSaving(false);
    }
  };

  const isWide = (f: FieldDef) =>
    f.type === 'textarea' || f.type === 'remote-multiselect';

  return (
    <div className="modal-overlay" onClick={onCancel}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{initial ? `Edit ${config.label}` : `New ${config.label}`}</h2>
          <button className="btn-icon" onClick={onCancel}>✕</button>
        </div>
        <form onSubmit={handleSubmit} className="entity-form">
          <div className="form-grid">
            {config.fields.map((f) => (
              <div key={f.name} className={`form-group ${isWide(f) ? 'full-width' : ''}`}>
                <label>{f.label}</label>

                {f.type === 'text' && (
                  <input type="text" value={String(state[f.name] ?? '')}
                    onChange={(e) => set(f.name, e.target.value)} />
                )}

                {f.type === 'textarea' && (
                  <textarea rows={3} value={String(state[f.name] ?? '')}
                    onChange={(e) => set(f.name, e.target.value)} />
                )}

                {(f.type === 'number' || f.type === 'decimal') && (
                  <input type="number" step={f.type === 'decimal' ? '0.01' : '1'}
                    value={String(state[f.name] ?? '')}
                    onChange={(e) => set(f.name, e.target.value)} />
                )}

                {f.type === 'datetime' && (
                  <input type="datetime-local" value={String(state[f.name] ?? '')}
                    onChange={(e) => set(f.name, e.target.value)} />
                )}

                {f.type === 'boolean' && (
                  <label className="toggle">
                    <input type="checkbox" checked={Boolean(state[f.name])}
                      onChange={(e) => set(f.name, e.target.checked)} />
                    <span className="toggle-slider" />
                  </label>
                )}

                {f.type === 'select' && (
                  <select value={String(state[f.name] ?? '')}
                    onChange={(e) => set(f.name, e.target.value)}>
                    <option value="">— select —</option>
                    {f.options?.map((o) => <option key={o} value={o}>{o}</option>)}
                  </select>
                )}

                {f.type === 'tags' && (
                  <input type="text" placeholder="comma-separated values"
                    value={String(state[f.name] ?? '')}
                    onChange={(e) => set(f.name, e.target.value)} />
                )}

                {f.type === 'remote-select' && (
                  <RemoteSelectField
                    field={f}
                    value={String(state[f.name] ?? '')}
                    onChange={(id, label) => {
                      set(f.name, id);
                      if (f.linkedNameField) set(f.linkedNameField, label);
                    }}
                  />
                )}

                {f.type === 'remote-multiselect' && (
                  <RemoteMultiSelect
                    field={f}
                    value={Array.isArray(state[f.name]) ? (state[f.name] as string[]) : []}
                    onChange={(ids) => set(f.name, ids)}
                  />
                )}
              </div>
            ))}
          </div>

          {error && <div className="form-error">{error}</div>}

          <div className="form-actions">
            <button type="button" className="btn btn-secondary" onClick={onCancel} disabled={saving}>
              Cancel
            </button>
            <button type="submit" className="btn btn-primary" disabled={saving}>
              {saving ? 'Saving…' : 'Save'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
