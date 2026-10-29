export default function Home() {
  return (
    <main className="container">
      <header>
        <h1>ScholarEgine</h1>
        <p className="subtitle">GODSPEED Scholar / Research Engine</p>
      </header>

      <section className="content">
        <h2>Evidence-first research and source-ingestion</h2>
        
        <p>
          ScholarEgine is the research and source-ingestion surface for the shared 
          APEX Truth / Scholar / GODSPEED architecture.
        </p>

        <div className="architecture">
          <div className="flow-item">Approved sources</div>
          <div className="arrow">↓</div>
          <div className="flow-item highlight">ScholarEgine<br/>research + source ingestion</div>
          <div className="arrow">↓</div>
          <div className="flow-item">THE-BRAIN<br/>knowledge + provenance + contradiction + confidence</div>
          <div className="arrow">↓</div>
          <div className="flow-item">GODSPEED Truth Gate<br/>fail-closed output authorization</div>
        </div>

        <h3>Non-negotiable rule</h3>
        <blockquote>
          A model-generated answer is not evidence simply because a model generated it.
        </blockquote>

        <h3>Truth states</h3>
        <ul>
          <li>OBSERVED</li>
          <li>REFERENCE_CHECKED</li>
          <li>INDEPENDENTLY_VERIFIED</li>
          <li>UNVERIFIED</li>
        </ul>

        <p className="note">
          ScholarEgine discovers and organizes candidate evidence. 
          It does <strong>not</strong> declare a claim true merely because it found the claim.
        </p>
      </section>
    </main>
  );
}
