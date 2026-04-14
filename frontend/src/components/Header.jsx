export default function Header() {
  return (
    <header className="text-center space-y-3">
      <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-cyan-500/30 bg-cyan-500/10 text-cyan-300 text-xs font-medium tracking-wide">
        <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" />
        Hybrid Medical GraphRAG v1.0
      </div>
      <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight text-gradient">
        MedGraphRAG
      </h1>
      <p className="text-slate-400 max-w-2xl mx-auto text-sm md:text-base leading-relaxed">
        Hybrid Medical Graph Retrieval & Reasoning System<br className="hidden md:block" />
        Traverses Knowledge Graphs, PubMed Literature & Vector Embeddings for Evidence-Backed Clinical Reasoning
      </p>
    </header>
  );
}