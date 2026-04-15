export default function QueryInput({ value, onChange, onSubmit, isProcessing }) {
  return (
    <form onSubmit={onSubmit} className="w-full max-w-3xl mx-auto space-y-4">
      <div className="glass-input relative group">
        <textarea
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="Ask a clinical question... (e.g., 'Mechanism of GLP-1 on cardiovascular outcomes?')"
          className="w-full bg-transparent p-5 text-slate-100 placeholder-slate-500 resize-none min-h-30 focus:outline-none"
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              onSubmit(e);
            }
          }}
        />
        <div className="absolute bottom-3 right-3 flex items-center gap-3">
          <span className="text-xs text-slate-500 hidden md:inline-block">Press ↵ to submit</span>
          <button
            type="submit"
            disabled={isProcessing || !value.trim()}
            className="glow-btn flex items-center justify-center w-10 h-10 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-900 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:shadow-none"
            aria-label="Submit query"
          >
            {isProcessing ? (
              <svg className="w-5 h-5 animate-spin" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M12 2v4m0 12v4M4.93 4.93l2.83 2.83m8.48 8.48l2.83 2.83M2 12h4m12 0h4M4.93 19.07l2.83-2.83m8.48-8.48l2.83-2.83" />
              </svg>
            ) : (
              <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z" />
              </svg>
            )}
          </button>
        </div>
      </div>
    </form>
  );
}