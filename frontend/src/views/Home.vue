<template>
  <div class="wicai-container">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="nav-brand">WICAI4trade.AI</div>
      <div class="nav-links">
        <a href="#" class="nav-link active">Home</a>
        <a href="#" class="nav-link">Agents</a>
        <a href="#" class="nav-link">Portfolio</a>
        <a href="#" class="nav-link">Whitepaper</a>
        <a href="#" class="nav-link">Docs</a>
      </div>
      <div class="nav-actions">
        <button class="connect-wallet-btn">Connect Wallet</button>
      </div>
    </nav>

    <div class="main-content">
      <!-- Hero Section -->
      <section class="hero-section">
        <h1 class="hero-title">AI-Trader Agent Marketplace</h1>
        <p class="hero-subtitle">
          Discover, evaluate, and deploy autonomous AI trading agents optimized for crypto markets.
        </p>
      </section>

      <!-- Agent Grid -->
      <section class="agent-marketplace">
        <div class="agent-grid">
          <!-- Agent: Midas -->
          <div class="agent-card">
            <div class="card-header">
              <div class="agent-identity">
                <div class="agent-avatar midas"></div>
                <div class="agent-info">
                  <h3 class="agent-name">Midas</h3>
                  <span class="agent-ticker">$MDS</span>
                </div>
              </div>
              <div class="status-badge active">
                <span class="pulse-dot"></span> Active
              </div>
            </div>
            <p class="agent-desc">Specializes in high-frequency arbitrage across decentralized exchanges.</p>
            <div class="agent-metrics">
              <div class="metric">
                <span class="metric-label">Win Rate</span>
                <span class="metric-value">68.4%</span>
              </div>
              <div class="metric">
                <span class="metric-label">APY</span>
                <span class="metric-value positive">+142%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Trades</span>
                <span class="metric-value">12.4K</span>
              </div>
            </div>
            <div class="agent-tags">
              <span class="tag">Arbitrage</span>
              <span class="tag">HFT</span>
            </div>
            <button class="deploy-btn">Deploy Agent</button>
          </div>

          <!-- Agent: Apollo -->
          <div class="agent-card">
            <div class="card-header">
              <div class="agent-identity">
                <div class="agent-avatar apollo"></div>
                <div class="agent-info">
                  <h3 class="agent-name">Apollo</h3>
                  <span class="agent-ticker">$APL</span>
                </div>
              </div>
              <div class="status-badge active">
                <span class="pulse-dot"></span> Active
              </div>
            </div>
            <p class="agent-desc">Trend-following algorithm utilizing advanced momentum indicators.</p>
            <div class="agent-metrics">
              <div class="metric">
                <span class="metric-label">Win Rate</span>
                <span class="metric-value">55.2%</span>
              </div>
              <div class="metric">
                <span class="metric-label">APY</span>
                <span class="metric-value positive">+84%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Trades</span>
                <span class="metric-value">3.2K</span>
              </div>
            </div>
            <div class="agent-tags">
              <span class="tag">Momentum</span>
              <span class="tag">Mid-Risk</span>
            </div>
            <button class="deploy-btn">Deploy Agent</button>
          </div>

          <!-- Agent: Hermes -->
          <div class="agent-card">
            <div class="card-header">
              <div class="agent-identity">
                <div class="agent-avatar hermes"></div>
                <div class="agent-info">
                  <h3 class="agent-name">Hermes</h3>
                  <span class="agent-ticker">$HRM</span>
                </div>
              </div>
              <div class="status-badge active">
                <span class="pulse-dot"></span> Active
              </div>
            </div>
            <p class="agent-desc">Lightning-fast execution for MEV extraction and front-running protection.</p>
            <div class="agent-metrics">
              <div class="metric">
                <span class="metric-label">Win Rate</span>
                <span class="metric-value">71.8%</span>
              </div>
              <div class="metric">
                <span class="metric-label">APY</span>
                <span class="metric-value positive">+210%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Trades</span>
                <span class="metric-value">45.1K</span>
              </div>
            </div>
            <div class="agent-tags">
              <span class="tag">MEV</span>
              <span class="tag">Scalping</span>
            </div>
            <button class="deploy-btn">Deploy Agent</button>
          </div>

          <!-- Agent: Athena -->
          <div class="agent-card">
            <div class="card-header">
              <div class="agent-identity">
                <div class="agent-avatar athena"></div>
                <div class="agent-info">
                  <h3 class="agent-name">Athena</h3>
                  <span class="agent-ticker">$ATH</span>
                </div>
              </div>
              <div class="status-badge active">
                <span class="pulse-dot"></span> Active
              </div>
            </div>
            <p class="agent-desc">Conservative strategy focusing on stablecoin yields and low-risk pairs.</p>
            <div class="agent-metrics">
              <div class="metric">
                <span class="metric-label">Win Rate</span>
                <span class="metric-value">92.1%</span>
              </div>
              <div class="metric">
                <span class="metric-label">APY</span>
                <span class="metric-value positive">+18%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Trades</span>
                <span class="metric-value">850</span>
              </div>
            </div>
            <div class="agent-tags">
              <span class="tag">Yield</span>
              <span class="tag">Low-Risk</span>
            </div>
            <button class="deploy-btn">Deploy Agent</button>
          </div>

          <!-- Agent: Zeus -->
          <div class="agent-card">
            <div class="card-header">
              <div class="agent-identity">
                <div class="agent-avatar zeus"></div>
                <div class="agent-info">
                  <h3 class="agent-name">Zeus</h3>
                  <span class="agent-ticker">$ZEU</span>
                </div>
              </div>
              <div class="status-badge active">
                <span class="pulse-dot"></span> Active
              </div>
            </div>
            <p class="agent-desc">Aggressive leveraged trading bot for major market cap assets.</p>
            <div class="agent-metrics">
              <div class="metric">
                <span class="metric-label">Win Rate</span>
                <span class="metric-value">48.5%</span>
              </div>
              <div class="metric">
                <span class="metric-label">APY</span>
                <span class="metric-value positive">+315%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Trades</span>
                <span class="metric-value">5.6K</span>
              </div>
            </div>
            <div class="agent-tags">
              <span class="tag">Leverage</span>
              <span class="tag">High-Risk</span>
            </div>
            <button class="deploy-btn">Deploy Agent</button>
          </div>

          <!-- Agent: Vulcan -->
          <div class="agent-card">
            <div class="card-header">
              <div class="agent-identity">
                <div class="agent-avatar vulcan"></div>
                <div class="agent-info">
                  <h3 class="agent-name">Vulcan</h3>
                  <span class="agent-ticker">$VUL</span>
                </div>
              </div>
              <div class="status-badge active">
                <span class="pulse-dot"></span> Active
              </div>
            </div>
            <p class="agent-desc">Market-making bot providing liquidity and earning spread fees.</p>
            <div class="agent-metrics">
              <div class="metric">
                <span class="metric-label">Win Rate</span>
                <span class="metric-value">98.2%</span>
              </div>
              <div class="metric">
                <span class="metric-label">APY</span>
                <span class="metric-value positive">+42%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Trades</span>
                <span class="metric-value">128K</span>
              </div>
            </div>
            <div class="agent-tags">
              <span class="tag">Market-Maker</span>
              <span class="tag">Liquidity</span>
            </div>
            <button class="deploy-btn">Deploy Agent</button>
          </div>

        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  // Reset any global light theme styles from previous versions
  document.body.style.backgroundColor = '#0a0a0a';
  document.body.style.color = '#ffffff';
});
</script>

<style scoped>
.wicai-container {
  min-height: 100vh;
  background-color: #0a0a0a;
  color: #ffffff;
  font-family: 'Inter', system-ui, sans-serif;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 4rem;
  background-color: rgba(10, 10, 10, 0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(90deg, #fff, #888);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  gap: 2.5rem;
}

.nav-link {
  color: #a0a0a0;
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  transition: color 0.2s;
}

.nav-link:hover, .nav-link.active {
  color: #ffffff;
}

.connect-wallet-btn {
  background: linear-gradient(135deg, #2563eb, #3b82f6);
  color: #fff;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.2s;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
}

.connect-wallet-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
}

/* Hero Section */
.hero-section {
  text-align: center;
  margin-bottom: 5rem;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  letter-spacing: -1px;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: #a0a0a0;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Agent Grid */
.agent-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 1.5rem;
}

/* Agent Card */
.agent-card {
  background-color: #111111;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 1.5rem;
  transition: transform 0.2s, border-color 0.2s;
  display: flex;
  flex-direction: column;
}

.agent-card:hover {
  transform: translateY(-4px);
  border-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.agent-identity {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.agent-avatar {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #333, #111);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Avatar Placeholder Colors */
.agent-avatar.midas { background: linear-gradient(135deg, #f59e0b, #b45309); }
.agent-avatar.apollo { background: linear-gradient(135deg, #3b82f6, #1d4ed8); }
.agent-avatar.hermes { background: linear-gradient(135deg, #10b981, #047857); }
.agent-avatar.athena { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }
.agent-avatar.zeus { background: linear-gradient(135deg, #ef4444, #b91c1c); }
.agent-avatar.vulcan { background: linear-gradient(135deg, #64748b, #334155); }


.agent-name {
  font-size: 1.2rem;
  font-weight: 700;
  margin: 0;
}

.agent-ticker {
  font-size: 0.8rem;
  color: #6b7280;
  font-family: 'JetBrains Mono', monospace;
}

.status-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 12px;
  background-color: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  background-color: #10b981;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
  70% { box-shadow: 0 0 0 4px rgba(16, 185, 129, 0); }
  100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.agent-desc {
  font-size: 0.9rem;
  color: #9ca3af;
  line-height: 1.5;
  margin-bottom: 1.5rem;
  flex-grow: 1;
}

.agent-metrics {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  padding: 1rem;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 12px;
}

.metric {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.metric-label {
  font-size: 0.75rem;
  color: #6b7280;
}

.metric-value {
  font-size: 1rem;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
}

.metric-value.positive {
  color: #10b981;
}

.agent-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 1.5rem;
}

.tag {
  font-size: 0.7rem;
  padding: 4px 10px;
  background-color: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 100px;
  color: #d1d5db;
}

.deploy-btn {
  width: 100%;
  padding: 0.8rem;
  background-color: #ffffff;
  color: #000000;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.deploy-btn:hover {
  background-color: #e5e5e5;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-wrap: wrap;
  }
  
  .nav-links {
    display: none; /* Mobile menu would go here */
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .main-content {
    padding: 2rem 1rem;
  }
}
</style>
