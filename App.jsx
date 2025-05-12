import { useState } from 'react';
import OutputPanel from './components/OutputPanel';

export default function App() {
  const [inputQuery, setInputQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse(null); // Clear previous response
    try {
      const res = await fetch('http://localhost:5000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: inputQuery }),
      });

      // Check if backend returned an error status
      if (!res.ok) {
        const errorText = await res.text();
        console.error('Backend error:', res.status, errorText);
        throw new Error(`Server error: ${res.status}`);
      }

      // Parse the response
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Failed to connect to backend:', error);
      setResponse({ error: 'Failed to connect to backend.' });
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-3xl mx-auto bg-white shadow-xl rounded-2xl p-6">
        <h1 className="text-2xl font-bold mb-4">Natural Language to SQL Interface</h1>
        <form onSubmit={handleSubmit} className="mb-4 space-y-4">
          <input
            type="text"
            placeholder="Ask a question about the database..."
            value={inputQuery}
            onChange={(e) => setInputQuery(e.target.value)}
            className="w-full px-4 py-2 border rounded-xl shadow-sm focus:outline-none focus:ring"
            required
          />
          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded-xl"
            disabled={loading}
          >
            {loading ? 'Processing...' : 'Submit'}
          </button>
        </form>

        {response && <OutputPanel response={response} />}
      </div>
    </div>
  );
}
