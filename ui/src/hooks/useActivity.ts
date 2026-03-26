import { useCallback, useEffect, useState } from 'react';

export type ActionType = 'created' | 'updated' | 'deleted';

export interface ActivityEntry {
  id: string; // activity entry uuid
  entityKey: string;
  entityLabel: string;
  recordId: string;
  recordName: string;
  action: ActionType;
  timestamp: string; // ISO
}

const STORAGE_KEY = 'intel_excalibur_activity';
const MAX_ENTRIES = 50;

function loadActivity(): ActivityEntry[] {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '[]');
  } catch {
    return [];
  }
}

function saveActivity(entries: ActivityEntry[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(entries.slice(0, MAX_ENTRIES)));
}

export function useActivity() {
  const [entries, setEntries] = useState<ActivityEntry[]>(loadActivity);

  useEffect(() => {
    const handler = () => setEntries(loadActivity());
    window.addEventListener('intel_activity', handler);
    return () => window.removeEventListener('intel_activity', handler);
  }, []);

  const log = useCallback(
    (entry: Omit<ActivityEntry, 'id' | 'timestamp'>) => {
      const next: ActivityEntry = {
        ...entry,
        id: crypto.randomUUID(),
        timestamp: new Date().toISOString(),
      };
      const updated = [next, ...loadActivity()].slice(0, MAX_ENTRIES);
      saveActivity(updated);
      setEntries(updated);
      window.dispatchEvent(new Event('intel_activity'));
    },
    [],
  );

  const clear = useCallback(() => {
    saveActivity([]);
    setEntries([]);
  }, []);

  return { entries, log, clear };
}
