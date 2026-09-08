'use client'

import { useMemo, useState } from 'react'
import {
  Activity,
  Archive,
  ArrowUpRight,
  Bell,
  Bot,
  Check,
  ChevronDown,
  ChevronRight,
  CircleHelp,
  Clock3,
  Command,
  FileText,
  FolderKanban,
  LayoutGrid,
  Menu,
  MoreHorizontal,
  PanelLeftClose,
  Plus,
  Search,
  Send,
  Settings2,
  ShieldCheck,
  Sparkles,
  Users,
  X,
  Zap,
} from 'lucide-react'

const rails = [
  { name: 'AI CORE', icon: Bot, tone: 'sky' },
  { name: 'CONSTRUCT', icon: FolderKanban, tone: 'amber' },
  { name: 'TRADES', icon: Activity, tone: 'teal' },
  { name: 'ATELIER', icon: LayoutGrid, tone: 'rose', active: true },
]

const stages = ['Capture', 'Transform', 'Preview', 'Approve', 'Share']

const workItems = [
  { title: 'Client intake brief', type: 'Brief', status: 'In review', time: '12 min ago', color: 'blue' },
  { title: 'Concept board · Northstar', type: 'Board', status: 'Ready', time: 'Yesterday', color: 'violet' },
  { title: 'Brand system v4', type: 'System', status: 'Approved', time: 'Aug 28', color: 'teal' },
]

function Rail({ name, icon: Icon, tone, active }: { name: string; icon: typeof Bot; tone: string; active?: boolean }) {
  return (
    <button className={`rail-item ${active ? 'rail-item-active' : ''}`} aria-label={`${name} workspace`}>
      <span className={`rail-icon rail-${tone}`}><Icon size={17} strokeWidth={1.8} /></span>
      <span>{name}</span>
      {active && <span className="rail-dot" />}
    </button>
  )
}

export default function Page() {
  const [mobileNav, setMobileNav] = useState(false)
  const [activeStage, setActiveStage] = useState(1)
  const [showGabby, setShowGabby] = useState(false)
  const [prompt, setPrompt] = useState('')
  const [toast, setToast] = useState('')
  const [collapsed, setCollapsed] = useState(false)
  const [activePanel, setActivePanel] = useState<'none' | 'repair' | 'settings' | 'help'>('none')
  const [repairStatus, setRepairStatus] = useState('Ready for observation')
  const [ticket, setTicket] = useState('')

  const stageCopy = useMemo(() => [
    'Drop anything here. Gabby will sort the signal from the noise.',
    'The brief has been normalized into a clear, reviewable structure.',
    'Your workspace preview is ready for a final look before approval.',
    'One decision remains: approve the proposed direction for sharing.',
    'Package the approved work for your team and client channels.',
  ][activeStage], [activeStage])

  const notify = (message: string) => {
    setToast(message)
    window.setTimeout(() => setToast(''), 2800)
  }

  return (
    <main className="app-shell">
      <header className="topbar">
        <div className="brand-lockup">
          <button className="icon-button mobile-menu" onClick={() => setMobileNav(!mobileNav)} aria-label="Open navigation"><Menu size={20} /></button>
          <div className="brand-mark"><span /><span /><span /></div>
          <div><p className="brand-name">APEX <span>365</span></p><p className="brand-subtitle">Enterprise workspace</p></div>
        </div>
        <div className="topbar-actions">
          <button className="command-button" aria-label="Open command menu"><Command size={15} /><span>Search anything</span><kbd>⌘ K</kbd></button>
          <button className="icon-button" aria-label="Notifications" onClick={() => notify('You are all caught up')}><Bell size={18} /><i className="notification-dot" /></button>
          <button className="avatar" aria-label="Open profile">AR</button>
        </div>
      </header>

      <div className="workspace-body">
        <aside className={`sidebar ${mobileNav ? 'sidebar-open' : ''} ${collapsed ? 'sidebar-collapsed' : ''}`}>
          <div className="sidebar-head"><span className="eyebrow">WORKSPACES</span><button className="icon-button" onClick={() => setCollapsed(!collapsed)} aria-label="Collapse navigation"><PanelLeftClose size={16} /></button></div>
          <nav className="rail-list">{rails.map((rail) => <Rail key={rail.name} {...rail} />)}</nav>
          <div className="sidebar-divider" />
          <div className="sidebar-links">
            <button className="sidebar-link"><Archive size={17} /> <span>Library</span></button>
            <button className="sidebar-link"><Users size={17} /> <span>People & access</span></button>
            <button className="sidebar-link"><ShieldCheck size={17} /> <span>Governance</span></button>
          </div>
          <div className="sidebar-bottom"><button className="sidebar-link" onClick={() => setActivePanel('settings')}><Settings2 size={17} /><span>Workspace settings</span></button><button className="sidebar-link" onClick={() => setActivePanel('help')}><CircleHelp size={17} /><span>Help center</span></button><button className="sidebar-link" onClick={() => setActivePanel('repair')}><ShieldCheck size={17} /><span>Fail-safe repair</span></button></div>
        </aside>

        <section className="content-area">
          <div className="mobile-overlay" onClick={() => setMobileNav(false)} />
          <div className="content-header">
            <div><div className="breadcrumb"><span>ATELIER</span><ChevronRight size={13} /><span className="muted">Overview</span></div><h1>Atelier 360</h1><p className="lede">A shared studio for turning early signals into aligned, finished work.</p></div>
            <div className="header-buttons"><button className="secondary-button" onClick={() => notify('Invite link copied')}><Users size={16} /> Invite</button><button className="primary-button" onClick={() => notify('New project created')}><Plus size={17} /> New project</button></div>
          </div>

          <div className="stats-row"><div className="stat-card"><span className="stat-label">ACTIVE PROJECTS</span><strong>08</strong><span className="stat-note positive">+2 this month</span></div><div className="stat-card"><span className="stat-label">IN REVIEW</span><strong>03</strong><span className="stat-note">Across 2 teams</span></div><div className="stat-card"><span className="stat-label">TEAM PULSE</span><strong>92%</strong><span className="stat-note positive"><Zap size={12} /> Healthy</span></div><div className="stat-card stat-card-wide"><span className="stat-label">LAST SYNC</span><strong>Just now</strong><span className="stat-note">All systems operational</span></div></div>

          <div className="content-grid">
            <section className="atelier-card workflow-card">
              <div className="card-heading"><div><span className="eyebrow accent-eyebrow">FEATURED WORKFLOW</span><h2>From signal to shared direction</h2></div><button className="more-button" aria-label="More workflow options"><MoreHorizontal size={19} /></button></div>
              <div className="stage-track">{stages.map((stage, index) => <button key={stage} className={`stage ${index === activeStage ? 'stage-current' : ''} ${index < activeStage ? 'stage-complete' : ''}`} onClick={() => setActiveStage(index)}><span className="stage-number">{index < activeStage ? <Check size={14} /> : `0${index + 1}`}</span><span>{stage}</span></button>)}</div>
              <div className="workflow-canvas"><div className="canvas-glow" /><div className="canvas-label"><span className="live-dot" />LIVE WORKSPACE</div><div className="canvas-content"><div className="canvas-icon"><Sparkles size={24} /></div><h3>{stages[activeStage]} is the next move.</h3><p>{stageCopy}</p><button className="canvas-action" onClick={() => notify(`${stages[activeStage]} workspace opened`)}>Open {stages[activeStage]} <ArrowUpRight size={15} /></button></div><div className="canvas-footer"><span>Northstar / Q3 launch</span><span>Private · 4 collaborators</span></div></div>
            </section>

            <aside className="atelier-card gabby-card"><div className="gabby-header"><div className="gabby-avatar"><Bot size={20} /></div><div><h2>Gabby</h2><p>Your studio guide</p></div><span className="online-status">Online</span></div><div className="gabby-message"><p>Good morning, Alex. I found three signals across your active workspaces that may need a decision today.</p><button onClick={() => setShowGabby(true)}>Show me <ArrowUpRight size={14} /></button></div><div className="gabby-suggestions"><button onClick={() => setShowGabby(true)}>Summarize project status</button><button onClick={() => setShowGabby(true)}>Find open decisions</button></div><button className="gabby-input" onClick={() => setShowGabby(true)}><span>Ask Gabby anything...</span><Send size={15} /></button></aside>
          </div>

          <section className="projects-section"><div className="section-heading"><div><span className="eyebrow">RECENT WORK</span><h2>Keep the signal moving</h2></div><button className="text-button" onClick={() => notify('Opening project library')}>View library <ArrowUpRight size={14} /></button></div><div className="project-table">{workItems.map((item) => <button className="project-row" key={item.title} onClick={() => notify(`${item.title} opened`)}><span className={`project-type project-${item.color}`}><FileText size={16} /></span><span className="project-name"><strong>{item.title}</strong><small>{item.type}</small></span><span className={`status status-${item.status.toLowerCase().replace(' ', '-')}`}><i />{item.status}</span><span className="project-time"><Clock3 size={14} />{item.time}</span><ChevronRight className="row-chevron" size={17} /></button>)}</div></section>
        </section>
      </div>

      {showGabby && <div className="gabby-modal" role="dialog" aria-modal="true" aria-label="Gabby assistant"><div className="modal-panel"><div className="modal-header"><div className="gabby-avatar"><Bot size={20} /></div><div><h2>Talk to Gabby</h2><p>Context-aware studio assistance</p></div><button className="icon-button" onClick={() => setShowGabby(false)} aria-label="Close Gabby"><X size={18} /></button></div><div className="chat-bubble">I’m ready. Ask me to synthesize work, surface decisions, or prepare the next handoff.</div><div className="prompt-row"><input value={prompt} onChange={(event) => setPrompt(event.target.value)} onKeyDown={(event) => { if (event.key === 'Enter' && !event.nativeEvent.isComposing && event.keyCode !== 229) { notify(prompt ? 'Gabby is preparing a response' : 'Try asking about your projects'); setPrompt('') } }} placeholder="Ask about your workspace..." autoFocus /><button onClick={() => { notify('Gabby is preparing a response'); setPrompt('') }} aria-label="Send prompt"><Send size={16} /></button></div></div></div>}
      {activePanel !== 'none' && <div className="ops-overlay" role="dialog" aria-modal="true" aria-label={`${activePanel} panel`}><section className="ops-panel"><div className="modal-header"><div><span className="eyebrow accent-eyebrow">APEX OPERATIONS</span><h2>{activePanel === 'repair' ? 'Fail-safe repair' : activePanel === 'settings' ? 'Workspace settings' : 'Operator manual & help desk'}</h2></div><button className="icon-button" onClick={() => setActivePanel('none')} aria-label="Close panel"><X size={18} /></button></div>{activePanel === 'repair' && <div className="ops-body"><p className="ops-lede">Root-cause first. Observe → reproduce → diagnose → repair → verify → record.</p><div className="repair-status"><span className="live-dot" />{repairStatus}</div><div className="repair-actions"><button className="primary-button" onClick={() => setRepairStatus('Audit complete · no destructive changes')}>Run diagnostic</button><button className="secondary-button" onClick={() => setRepairStatus('Checkpoint created · ready for verification')}>Create checkpoint</button></div><div className="ops-list"><div><strong>Level 0</strong><span>Observation and reproduction</span></div><div><strong>Level 1–3</strong><span>Configuration, data, and state</span></div><div><strong>Level 4–10</strong><span>Component, layout, routing, integration, build</span></div></div></div>}{activePanel === 'settings' && <div className="ops-body"><p className="ops-lede">Secrets stay on the server. Names can be classified; values are never requested here.</p><label className="setting-row"><span>Environment policy</span><strong>Server secrets only</strong></label><label className="setting-row"><span>Verification mode</span><strong>No-fake-green</strong></label><label className="setting-row"><span>Workspace scope</span><strong>Private · enterprise</strong></label><button className="primary-button" onClick={() => notify('Settings saved locally')}>Save preferences</button></div>}{activePanel === 'help' && <div className="ops-body"><p className="ops-lede">Use the manual for operating rules, then file a ticket when evidence needs a human decision.</p><div className="help-chapters"><span>01 Start here</span><span>02 Capture workflow</span><span>03 Gabby & approvals</span><span>04 Verification states</span><span>05 Integrations & secrets</span></div><div className="ticket-row"><input value={ticket} onChange={(event) => setTicket(event.target.value)} placeholder="Describe the issue or evidence gap" /><button className="primary-button" onClick={() => { notify(ticket ? 'Help ticket recorded' : 'Add a short issue description'); if (ticket) setTicket('') }}>File ticket</button></div></div>}</section></div>}
      {toast && <div className="toast"><Check size={15} />{toast}</div>}
    </main>
  )
}
