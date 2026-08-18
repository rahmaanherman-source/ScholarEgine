import { describe, expect, it, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Sidebar } from '../src/ui/Sidebar';
import { CollapsiblePanel } from '../src/ui/CollapsiblePanel';

describe('Sidebar', () => {
  it('collapses and expands while preserving navigation', async () => {
    const user = userEvent.setup();
    const onToggle = vi.fn();
    const { rerender } = render(<Sidebar collapsed={false} onToggle={onToggle}><button>Workspace</button></Sidebar>);

    expect(screen.getByRole('button', { name: 'Workspace' })).toBeInTheDocument();
    await user.click(screen.getByRole('button', { name: 'Collapse sidebar' }));
    expect(onToggle).toHaveBeenCalledTimes(1);

    rerender(<Sidebar collapsed onToggle={onToggle}><button>Workspace</button></Sidebar>);
    expect(screen.getByRole('button', { name: 'Expand sidebar' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Workspace' })).toBeInTheDocument();
  });
});

describe('CollapsiblePanel', () => {
  it('collapses and expands content without destroying it', async () => {
    const user = userEvent.setup();
    const onToggle = vi.fn();
    const { rerender } = render(<CollapsiblePanel title="Tools" collapsed={false} onToggle={onToggle}><div>Tool content</div></CollapsiblePanel>);

    expect(screen.getByText('Tool content')).toBeInTheDocument();
    await user.click(screen.getByRole('button', { name: 'Collapse Tools' }));
    expect(onToggle).toHaveBeenCalledTimes(1);

    rerender(<CollapsiblePanel title="Tools" collapsed onToggle={onToggle}><div>Tool content</div></CollapsiblePanel>);
    expect(screen.getByRole('button', { name: 'Expand Tools' })).toBeInTheDocument();
  });
});
