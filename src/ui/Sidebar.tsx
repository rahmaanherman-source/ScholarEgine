import type { ReactNode } from 'react';

interface SidebarProps {
  collapsed: boolean;
  onToggle: () => void;
  children?: ReactNode;
}

export function Sidebar({ collapsed, onToggle, children }: SidebarProps) {
  return (
    <aside className={`sidebar${collapsed ? ' is-collapsed' : ''}`} aria-label="APEX sidebar">
      <button
        type="button"
        className="sidebar-toggle"
        aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
        aria-expanded={!collapsed}
        onClick={onToggle}
      >
        {collapsed ? '→' : '←'}
      </button>
      <nav aria-label="Workspace navigation">{children}</nav>
    </aside>
  );
}
