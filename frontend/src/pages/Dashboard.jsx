import { useState } from 'react';
import Header from '../components/Header';
import QueryInput from '../components/QueryInput';
import ResponsePanel from '../components/ResponsePanel';
import { ConfidenceBadge, GraphPathPanel, SourcesPanel } from '../components/Insights';
import BackgroundPattern from '../components/BackgroundPattern';

export default function App() {
  const [query, setQuery] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [data, setData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setIsProcessing(true);
    setData(null);

    // 🔌 API INTEGRATION NOTE: Replace with actual fetch/axios call to your FastAPI/Node backend
    // const res = await fetch('/api/query', { method: 'POST', body: JSON.stringify({ query }) });
    // const json = await res.json();
    
    await new Promise((r) => setTimeout(r, 1800)); // Simulate network + LKG traversal
    setIsProcessing(false);
    setData({
      answer: `Based on cross-referencing 142 PubMed papers and traversing the medical knowledge graph, the clinical consensus indicates that targeted GLP-1 agonists show statistically significant reduction in cardiovascular events (p<0.01) when combined with SGLT2 inhibitors. The pathway analysis reveals modulation via AMPK/mTOR signaling nodes.`,
      confidence: 0.94,
      sources: [
        { id: 'PMID:34215890', title: 'GLP-1 Receptor Agonists and Cardiovascular Outcomes', journal: 'NEJM', year: 2023 },
        { id: 'PMID:35109214', title: 'Synergistic Effects of SGLT2i in Metabolic Syndrome', journal: 'The Lancet', year: 2022 }
      ],
      path: ['Drug Class: GLP-1', '→ Target: GLP-1R', '→ Pathway: AMPK/mTOR', '→ Outcome: ↓ CV Events']
    });
  };

  return (
    <div className="min-h-screen relative overflow-x-hidden">
      <BackgroundPattern />
      <main className="relative z-10 max-w-6xl mx-auto px-4 py-12 md:py-16 flex flex-col gap-12">
        <Header />
        
        <QueryInput 
          value={query} 
          onChange={setQuery} 
          onSubmit={handleSubmit} 
          isProcessing={isProcessing} 
        />

        <div className={`transition-all duration-500 ease-out ${data || isProcessing ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <ResponsePanel answer={data?.answer} isProcessing={isProcessing} />
            </div>
            
            <div className="space-y-6">
              <ConfidenceBadge score={data?.confidence} isProcessing={isProcessing} />
              <GraphPathPanel path={data?.path} isProcessing={isProcessing} />
              <SourcesPanel sources={data?.sources} isProcessing={isProcessing} />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}