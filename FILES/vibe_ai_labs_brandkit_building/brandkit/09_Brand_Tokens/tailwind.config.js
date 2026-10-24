module.exports = {
  theme: {
    extend: {
      colors: {
        vibe: {
          midnight: '#0B1026',
          blue: '#2563FF',
          aqua: '#14D8C4',
          violet: '#8B5CF6',
          cloud: '#F8FAFC',
          ink: '#111827',
          slate: '#667085',
          line: '#D9E2F2',
          white: '#FFFFFF',
          green: '#16A34A',
          orange: '#F97316',
          logo-navy: '#000667',
          logo-blue: '#0258FE',
          logo-cyan: '#00F9FE',
        },
      },
      fontFamily: {
        headline: ['Plus Jakarta Sans', 'Inter', 'Arial', 'sans-serif'],
        body: ['Inter', 'Arial', 'sans-serif'],
      },
      borderRadius: { xs: '6px', sm: '12px', md: '20px', lg: '32px' },
      boxShadow: { 'vibe-md': '0 8px 24px rgba(11,16,38,.10)', 'vibe-lg': '0 24px 64px rgba(11,16,38,.18)', 'vibe-glow': '0 0 48px rgba(37,99,255,.45)' },
      backgroundImage: {
        'vibe-growth': 'linear-gradient(135deg, #2563FF, #14D8C4)',
        'vibe-creative': 'linear-gradient(135deg, #8B5CF6, #2563FF)',
        'vibe-depth': 'linear-gradient(135deg, #0B1026, #2563FF)',
        'vibe-spectrum': 'linear-gradient(135deg, #0B2C9D, #00F9FE)',
      },
    },
  },
};
