interface FocusModeProps {
  enabled: boolean;
  onToggle: () => void;
}

export function FocusMode({ enabled, onToggle }: FocusModeProps) {
  return (
    <button type="button" className={`focus-control${enabled ? ' is-active' : ''}`} aria-label={enabled ? 'Exit focus mode' : 'Enter focus mode'} aria-pressed={enabled} onClick={onToggle}>
      {enabled ? 'Exit Focus' : 'Focus Mode'}
    </button>
  );
}
