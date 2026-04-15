export default function ResponsePanel({ answer, isProcessing }) {
  if (isProcessing) {
    return (
      <div className="glass-panel rounded-2xl p-6 min-h-80 flex flex-col">
        <div className="flex items-center gap-2 mb-6 text-cyan-400 text-sm font-medium">
          <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse-graph" />
          Traversing Graph & Retrieving Literature...
        </div>
        <div className="space-y-3 flex-1">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="h-4 bg-slate-700/40 rounded animate-pulse" style={{ width: `${70 + Math.random() * 30}%` }} />
          ))}
        </div>
      </div>
    );
  }

  if (!answer) {
    return (
      <div className="glass-panel rounded-2xl p-8 min-h-80 flex flex-col items-center justify-center text-center text-slate-500">
        <svg className="w-12 h-12 mb-4 text-slate-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
          <circle cx="12" cy="12" r="10" />
          <path d="M8 12h8M12 8v8" />
        </svg>
        <h3 className="text-slate-300 font-medium">Ready for Clinical Query</h3>
        <p className="text-sm mt-2 max-w-xs">Enter a medical research question to initiate hybrid GraphRAG retrieval.</p>
      </div>
    );
  }

  return (
    <div className="glass-panel rounded-2xl p-6 min-h-80 flex flex-col">
      <div className="flex items-center justify-between mb-4 border-b border-slate-700/50 pb-3">
        <h2 className="text-sm font-semibold text-slate-300 tracking-wide uppercase">Synthesized Response</h2>
        <span className="text-xs text-slate-500 bg-slate-800 px-2 py-1 rounded">LLM + Graph Reasoning</span>
      </div>
      <div className="prose prose-invert prose-sm max-w-none flex-1 text-slate-300 leading-relaxed overflow-y-auto pr-2 custom-scrollbar">
        <p>{answer}</p>
      </div>
      <div className="mt-4 pt-3 border-t border-slate-700/50 flex items-center justify-between text-xs text-slate-500">
        <span>Generated via MedGraphRAG v1.0</span>
        <span className="flex items-center gap-1">
          <svg className="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          For research use only
        </span>
      </div>
    </div>
  );
}