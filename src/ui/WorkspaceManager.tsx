import { useState } from 'react';

export interface Workspace {
  id: string;
  name: string;
  active: boolean;
}

interface WorkspaceManagerProps {
  workspaces: Workspace[];
  onSelect: (id: string) => void;
  onClose: (id: string) => void;
}

export function WorkspaceManager({ workspaces, onSelect, onClose }: WorkspaceManagerProps) {
  const [open, setOpen] = useState(true);

  return (
    <section className="workspace-manager" aria-label="Workspace manager">
      <div className="section-heading">
        <div>
          <span className="eyebrow">WORKSPACE</span>
          <h2>Workspace Manager</h2>
        </div>
        <button type="button" className="icon-button" aria-label={open ? 'Close workspace manager' : 'Open workspace manager'} onClick={() => setOpen((value) => !value)}>
          {open ? '×' : '+'}
        </button>
      </div>
      {open && (
        <div className="workspace-list">
          {workspaces.map((workspace) => (
            <div className={`workspace-row${workspace.active ? ' is-active' : ''}`} key={workspace.id}>
              <button type="button" className="workspace-name" onClick={() => onSelect(workspace.id)}>{workspace.name}</button>
              <button type="button" className="icon-button" aria-label={`Close ${workspace.name}`} onClick={() => onClose(workspace.id)}>×</button>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}
