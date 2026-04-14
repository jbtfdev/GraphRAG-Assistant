import { Link } from 'react-router-dom';
import BackgroundPattern from '../components/BackgroundPattern';

export default function Landing() {
  return (
    <div className="min-h-screen relative overflow-hidden">
      <BackgroundPattern />
      
      {/* Hero Section */}
      <main className="relative z-10 pt-32 pb-20 px-6">
        <div className="max-w-6xl mx-auto">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-cyan-500/30 bg-cyan-500/10 text-cyan-300 text-sm font-medium mb-8">
            <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse" />
            Hybrid Medical GraphRAG v1.0
          </div>

          {/* Headline */}
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6">
            <span className="text-gradient">AI-Powered</span>
            <br />
            Medical Research Intelligence
          </h1>

          <p className="text-xl text-slate-400 max-w-3xl mb-10 leading-relaxed">
            Traverse knowledge graphs, PubMed literature, and vector embeddings 
            for evidence-backed clinical reasoning. Built for researchers, 
            clinicians, and medical AI pioneers.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 mb-20">
            <Link
              to="/app"
              className="glow-btn inline-flex items-center justify-center px-8 py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-semibold text-lg hover:shadow-[0_0_30px_rgba(6,182,212,0.5)] transition-all"
            >
              Launch Application
              <svg className="w-5 h-5 ml-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M5 12h14M12 5l7 7-7 7" />
              </svg>
            </Link>
            <a
              href="#features"
              className="inline-flex items-center justify-center px-8 py-4 rounded-xl border border-white/20 text-slate-300 font-semibold text-lg hover:bg-white/5 transition-all"
            >
              Learn More
            </a>
          </div>

          {/* Features Grid */}
          <div id="features" className="grid md:grid-cols-3 gap-8 mb-20">
            <FeatureCard
              icon={
                <svg className="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <circle cx="12" cy="12" r="3" />
                  <path d="M12 2v4m0 12v4M4.93 4.93l2.83 2.83m8.48 8.48l2.83 2.83M2 12h4m12 0h4M4.93 19.07l2.83-2.83m8.48-8.48l2.83-2.83" />
                </svg>
              }
              title="Knowledge Graph Traversal"
              description="Navigate complex medical ontologies and relationships between diseases, drugs, and pathways."
            />
            <FeatureCard
              icon={
                <svg className="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M12 20h9M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4L16.5 3.5z" />
                </svg>
              }
              title="PubMed Integration"
              description="Cross-reference 35+ million research papers with real-time literature synthesis."
            />
            <FeatureCard
              icon={
                <svg className="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" />
                  <polyline points="3.27 6.96 12 12.01 20.73 6.96" />
                  <line x1="12" y1="22.08" x2="12" y2="12" />
                </svg>
              }
              title="LLM Reasoning"
              description="Advanced language models synthesize findings with confidence scoring and explainability."
            />
          </div>

          {/* How It Works */}
          <div className="mb-20">
            <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">How It Works</h2>
            <div className="grid md:grid-cols-4 gap-6">
              <StepCard number="01" title="Query" description="Ask a clinical question in natural language" />
              <StepCard number="02" title="Retrieve" description="Search graphs, vectors, and literature simultaneously" />
              <StepCard number="03" title="Reason" description="LLM synthesizes evidence with confidence scoring" />
              <StepCard number="04" title="Explain" description="View sources, pathways, and reasoning traces" />
            </div>
          </div>

          {/* Stats Section */}
          <div className="glass-panel rounded-3xl p-8 md:p-12 mb-20">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
              <StatCard value="35M+" label="PubMed Papers" />
              <StatCard value="<1s" label="Response Time" />
              <StatCard value="94%" label="Accuracy" />
              <StatCard value="100+" label="Medical Ontologies" />
            </div>
          </div>

          {/* Final CTA */}
          <div className="text-center">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Transform Medical Research?</h2>
            <p className="text-slate-400 mb-8 max-w-2xl mx-auto">
              Join researchers and clinicians using MedGraphRAG for evidence-based decision making.
            </p>
            <Link
              to="/app"
              className="glow-btn inline-flex items-center justify-center px-8 py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white font-semibold text-lg hover:shadow-[0_0_30px_rgba(6,182,212,0.5)] transition-all"
            >
              Start Researching Now
            </Link>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="relative z-10 border-t border-white/10 py-8 px-6">
        <div className="max-w-6xl mx-auto text-center text-slate-500 text-sm">
          © 2025 MedGraphRAG. For research use only.
        </div>
      </footer>
    </div>
  );
}

// Helper Components
function FeatureCard({ icon, title, description }) {
  return (
    <div className="glass-panel rounded-2xl p-6 hover:border-cyan-500/30 transition-all group">
      <div className="w-12 h-12 rounded-xl bg-cyan-500/10 text-cyan-400 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
        {icon}
      </div>
      <h3 className="text-lg font-semibold text-slate-200 mb-2">{title}</h3>
      <p className="text-slate-400 text-sm leading-relaxed">{description}</p>
    </div>
  );
}

function StepCard({ number, title, description }) {
  return (
    <div className="text-center">
      <div className="text-4xl font-bold text-gradient mb-2">{number}</div>
      <h3 className="text-lg font-semibold text-slate-200 mb-2">{title}</h3>
      <p className="text-slate-400 text-sm">{description}</p>
    </div>
  );
}

function StatCard({ value, label }) {
  return (
    <div>
      <div className="text-3xl md:text-4xl font-bold text-gradient mb-2">{value}</div>
      <div className="text-slate-400 text-sm">{label}</div>
    </div>
  );
}