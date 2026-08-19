import type { ReactNode } from 'react';

interface CollapsiblePanelProps {
  title: string;
  collapsed: boolean;
  onToggle: () => void;
  children?: ReactNode;
}

export function CollapsiblePanel({ title, collapsed, onToggle, children }: CollapsiblePanelProps) {
  return (
    <section className={`collapsible-panel${collapsed ? ' is-collapsed' : ''}`} aria-label={title}>
      <button
        type="button"
        className="collapsible-panel-toggle"
        aria-label={collapsed ? `Expand ${title}` : `Collapse ${title}`}
        aria-expanded={!collapsed}
        onClick={onToggle}
      >
        <span>{title}</span>
        <span aria-hidden="true">{collapsed ? '＋' : '−'}</span>
      </button>
      <div hidden={collapsed}>{children}</div>
    </section>
  );
}
