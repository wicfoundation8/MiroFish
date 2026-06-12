import React, { useState, useEffect } from 'react';
import { ShoppingCart, User, Activity, ArrowUpRight, Search } from 'lucide-react';

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [agents, setAgents] = useState([]);
  const [user, setUser] = useState(null);
  const [walletInput, setWalletInput] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetch(`${API_BASE_URL}/agents`)
      .then(res => res.json())
      .then(data => {
        setAgents(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setError("Failed to load marketplace data");
        setLoading(false);
      });
  }, []);

  const handleLogin = async (e) => {
    e.preventDefault();
    if (!walletInput.trim()) return;

    try {
      const res = await fetch(`${API_BASE_URL}/users/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ wallet_address: walletInput })
      });
      const data = await res.json();
      setUser(data);
    } catch (err) {
      console.error(err);
      alert("Login failed");
    }
  };

  const handleBuy = async (agent) => {
    if (!user) {
      alert("Please login first");
      return;
    }

    if (user.balance < agent.price) {
      alert("Insufficient balance");
      return;
    }

    try {
      const res = await fetch(`${API_BASE_URL}/marketplace/buy`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ wallet_address: user.wallet_address, agent_id: agent.id })
      });

      if (!res.ok) throw new Error("Purchase failed");

      const newBalance = user.balance - agent.price;
      setUser({...user, balance: newBalance});
      alert(`Successfully purchased ${agent.name}! Check your wallet for the execution contract.`);
    } catch (err) {
      console.error(err);
      alert("Transaction failed");
    }
  };

  const filteredAgents = agents.filter(a =>
    a.name.toLowerCase().includes(search.toLowerCase()) ||
    a.category.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-black text-white">
      {/* Navbar */}
      <nav className="border-b border-gray-800 bg-wic-dark/90 backdrop-blur sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-20">
            <div className="flex items-center gap-2">
              <div className="w-10 h-10 rounded-full bg-wic-gold flex items-center justify-center font-bold text-black text-xl">
                W
              </div>
              <span className="font-bold text-2xl tracking-wider text-white">
                WICAI<span className="text-wic-cyan">4trade</span>.AI
              </span>
            </div>

            <div className="hidden md:flex items-center space-x-8">
              <a href="#" className="text-gray-300 hover:text-wic-cyan transition-colors">Marketplace</a>
              <a href="#" className="text-gray-300 hover:text-wic-cyan transition-colors">My Agents</a>
              <a href="#" className="text-gray-300 hover:text-wic-cyan transition-colors">Stats</a>
            </div>

            <div className="flex items-center gap-4">
              {user ? (
                <div className="flex items-center gap-4 bg-gray-900 px-4 py-2 rounded-full border border-gray-800">
                  <div className="flex flex-col items-end">
                    <span className="text-xs text-gray-400">Balance</span>
                    <span className="text-sm font-bold text-wic-gold">${user.balance.toLocaleString(undefined, {minimumFractionDigits: 2})}</span>
                  </div>
                  <div className="w-8 h-8 rounded-full bg-wic-cyan/20 flex items-center justify-center">
                    <User className="w-4 h-4 text-wic-cyan" />
                  </div>
                </div>
              ) : (
                <form onSubmit={handleLogin} className="flex gap-2">
                  <input
                    type="text"
                    placeholder="Enter Wallet Address"
                    value={walletInput}
                    onChange={(e) => setWalletInput(e.target.value)}
                    className="bg-gray-900 border border-gray-700 rounded px-3 py-1 text-sm focus:outline-none focus:border-wic-cyan"
                  />
                  <button type="submit" className="bg-wic-cyan text-black px-4 py-1 rounded font-bold hover:bg-cyan-400 transition-colors">
                    Connect
                  </button>
                </form>
              )}
            </div>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
        <h1 className="text-5xl md:text-7xl font-black mb-6 tracking-tight">
          Intelligent <span className="text-transparent bg-clip-text bg-gradient-to-r from-wic-gold to-wic-cyan">Investing</span>
        </h1>
        <p className="text-xl text-gray-400 max-w-2xl mx-auto mb-10">
          The premiere Agent Marketplace for AI trading. Connect your wallet, purchase autonomous agents, and optimize your yield with next-generation algorithms on the WICCHAIN ecosystem.
        </p>

        <div className="max-w-xl mx-auto relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Search className="h-5 w-5 text-gray-500" />
          </div>
          <input
            type="text"
            placeholder="Search agents by name or category..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="block w-full pl-10 pr-3 py-4 border border-gray-800 rounded-xl bg-gray-900/50 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-wic-cyan focus:border-transparent transition-all"
          />
        </div>
      </div>

      {/* Marketplace Grid */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="flex justify-between items-center mb-8">
          <h2 className="text-2xl font-bold border-l-4 border-wic-gold pl-3">Featured Agents</h2>
          <div className="flex gap-2">
            <span className="px-3 py-1 rounded-full bg-gray-900 text-sm border border-gray-800">All</span>
            <span className="px-3 py-1 rounded-full bg-black text-sm border border-gray-800 text-gray-400 hover:text-white cursor-pointer transition-colors">Crypto</span>
            <span className="px-3 py-1 rounded-full bg-black text-sm border border-gray-800 text-gray-400 hover:text-white cursor-pointer transition-colors">DeFi</span>
          </div>
        </div>

        {loading ? (
          <div className="text-center py-20 text-wic-cyan animate-pulse">Loading Agents...</div>
        ) : error ? (
          <div className="text-center py-20 text-red-500">{error}</div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredAgents.map(agent => (
              <div key={agent.id} className="bg-gray-900/40 border border-gray-800 rounded-2xl p-6 hover:border-wic-cyan/50 transition-all group relative overflow-hidden">
                <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-wic-gold to-wic-cyan opacity-0 group-hover:opacity-100 transition-opacity"></div>

                <div className="flex justify-between items-start mb-4">
                  <div>
                    <span className="text-xs font-bold uppercase tracking-wider text-wic-cyan bg-wic-cyan/10 px-2 py-1 rounded">
                      {agent.category}
                    </span>
                    <h3 className="text-xl font-bold mt-2 mb-1">{agent.name}</h3>
                    <p className="text-sm text-gray-500">by {agent.author}</p>
                  </div>
                  <div className="bg-black border border-gray-800 rounded-lg p-2 text-center">
                    <div className="text-xs text-gray-400">Price</div>
                    <div className="font-bold text-wic-gold">${agent.price}</div>
                  </div>
                </div>

                <p className="text-gray-400 text-sm mb-6 line-clamp-2">
                  {agent.description}
                </p>

                <div className="grid grid-cols-2 gap-4 mb-6">
                  <div className="bg-black/50 rounded-lg p-3 border border-gray-800/50">
                    <div className="flex items-center gap-1 text-xs text-gray-400 mb-1">
                      <Activity className="w-3 h-3" /> APY
                    </div>
                    <div className="text-lg font-bold text-green-400">+{agent.apy}%</div>
                  </div>
                  <div className="bg-black/50 rounded-lg p-3 border border-gray-800/50">
                    <div className="flex items-center gap-1 text-xs text-gray-400 mb-1">
                      <ArrowUpRight className="w-3 h-3" /> Win Rate
                    </div>
                    <div className="text-lg font-bold text-white">{agent.win_rate}%</div>
                  </div>
                </div>

                <button
                  onClick={() => handleBuy(agent)}
                  className="w-full bg-white/5 hover:bg-wic-cyan hover:text-black text-white font-bold py-3 rounded-xl transition-all flex items-center justify-center gap-2 border border-gray-700 hover:border-transparent group-hover:border-wic-cyan/50"
                >
                  <ShoppingCart className="w-4 h-4" /> Buy Agent
                </button>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="border-t border-gray-900 mt-20 py-10 text-center text-gray-600 text-sm">
        <p>@ {new Date().getFullYear()} Wicchain Foundation. All Rights Reserved.</p>
        <p className="mt-2 text-xs">Powered by AI</p>
      </footer>
    </div>
  );
}

export default App;