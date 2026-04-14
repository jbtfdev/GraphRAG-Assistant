export function ConfidenceBadge({ score, isProcessing }) {
  if (isProcessing) return <div className="glass-panel rounded-2xl p-4 h-20 animate-pulse" />;
  if (!score) return null;

  const color = score >= 0.9 ? 'text-cyan-400' : score >= 0.75 ? 'text-yellow-400' : 'text-rose-400';
  const bg = score >= 0.9 ? 'bg-cyan-500/10' : score >= 0.75 ? 'bg-yellow-500/10' : 'bg-rose-500/10';

  return (
    <div className={`glass-panel rounded-2xl p-4 ${bg} border-l-4 ${color.replace('text', 'border')}`}>
      <div className="text-xs text-slate-400 mb-1">Reasoning Confidence</div>
      <div className={`text-2xl font-bold ${color}`}>{(score * 100).toFixed(1)}%</div>
      <div className="w-full bg-slate-800 h-1.5 rounded-full mt-2 overflow-hidden">
        <div className={`h-full ${color.replace('text', 'bg')}`} style={{ width: `${score * 100}%` }} />
      </div>
    </div>
  );
}

export function GraphPathPanel({ path, isProcessing }) {
  if (isProcessing) return <div className="glass-panel rounded-2xl p-4 h-32 animate-pulse" />;
  if (!path) return null;

  return (
    <div className="glass-panel rounded-2xl p-4">
      <div className="text-xs text-slate-400 mb-3 flex items-center gap-2">
        <svg className="w-3.5 h-3.5 text-cyan-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="12" r="3"/><path d="M8.6 7.5l7 3.8M8.6 16.5l7-3.8"/></svg>
        Traversed Graph Path
      </div>
      <div className="space-y-2">
        {path.map((node, i) => (
          <div key={i} className="flex items-center gap-2 text-xs text-slate-300 bg-slate-800/50 px-3 py-2 rounded-lg border border-slate-700/50">
            <span className="w-1.5 h-1.5 rounded-full bg-cyan-500" />
            {node}
          </div>
        ))}
      </div>
    </div>
  );
}

export function SourcesPanel({ sources, isProcessing }) {
  if (isProcessing) return <div className="glass-panel rounded-2xl p-4 h-40 animate-pulse" />;
  if (!sources) return null;

  return (
    <div className="glass-panel rounded-2xl p-4">
      <div className="text-xs text-slate-400 mb-3 flex items-center justify-between">
        <span>Retrieved Sources</span>
        <span className="text-cyan-400">{sources.length} matched</span>
      </div>
      <div className="space-y-3 max-h-64 overflow-y-auto pr-1 custom-scrollbar">
        {sources.map((src) => (
          <div key={src.id} className="group cursor-pointer p-3 rounded-lg bg-slate-800/30 hover:bg-slate-800/60 border border-transparent hover:border-cyan-500/30 transition-all">
            <div className="text-xs font-medium text-slate-200 group-hover:text-cyan-300 transition-colors">{src.title}</div>
            <div className="flex gap-2 mt-1 text-[10px] text-slate-500">
              <span className="bg-slate-700 px-1.5 py-0.5 rounded">{src.id}</span>
              <span>{src.journal}</span>
              <span>{src.year}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}