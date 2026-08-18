import { describe, expect, it, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { WorkspaceManager } from '../src/ui/WorkspaceManager';
import { FocusMode } from '../src/ui/FocusMode';

describe('WorkspaceManager', () => {
  it('lists, selects, and closes a workspace without deleting data', async () => {
    const user = userEvent.setup();
    const onSelect = vi.fn();
    const onClose = vi.fn();
    render(<WorkspaceManager workspaces={[{ id: 'one', name: 'Primary', active: true }]} onSelect={onSelect} onClose={onClose} />);

    await user.click(screen.getByRole('button', { name: 'Primary' }));
    await user.click(screen.getByRole('button', { name: 'Close Primary' }));

    expect(onSelect).toHaveBeenCalledWith('one');
    expect(onClose).toHaveBeenCalledWith('one');
    expect(screen.getByText('Primary')).toBeInTheDocument();
  });
});

describe('FocusMode', () => {
  it('toggles between enter and exit states', async () => {
    const user = userEvent.setup();
    const onToggle = vi.fn();
    const { rerender } = render(<FocusMode enabled={false} onToggle={onToggle} />);

    await user.click(screen.getByRole('button', { name: 'Enter focus mode' }));
    expect(onToggle).toHaveBeenCalledTimes(1);

    rerender(<FocusMode enabled onToggle={onToggle} />);
    expect(screen.getByRole('button', { name: 'Exit focus mode' })).toBeInTheDocument();
  });
});
