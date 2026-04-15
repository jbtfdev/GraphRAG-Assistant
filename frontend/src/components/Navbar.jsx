import { Link, useLocation } from 'react-router-dom';

export default function Navbar() {
  const location = useLocation();
  const isActive = (path) => location.pathname === path;

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 glass-panel border-b border-white/5">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2 group">
          <div className="w-8 h-8 rounded-lg bg-linear-to-br from-cyan-400 to-blue-600 flex items-center justify-center">
            <svg className="w-5 h-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
            </svg>
          </div>
          <span className="text-xl font-bold text-gradient">MedGraphRAG</span>
        </Link>

        <div className="flex items-center gap-6">
          <Link
            to="/"
            className={`text-sm font-medium transition-colors ${
              isActive('/') ? 'text-cyan-400' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Overview
          </Link>
          <Link
            to="/app"
            className={`text-sm font-medium transition-colors ${
              isActive('/app') ? 'text-cyan-400' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Launch App
          </Link>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-sm font-medium transition-all border border-white/10"
          >
            GitHub
          </a>
        </div>
      </div>
    </nav>
  );
}