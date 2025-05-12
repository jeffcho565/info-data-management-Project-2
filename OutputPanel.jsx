import React from 'react';

export default function OutputPanel({ response }) {
  const { input, sql, result, error } = response;

  return (
    <div className="mt-6 space-y-4">
      {error && (
        <div className="bg-red-100 text-red-800 p-4 rounded-xl shadow">
          {error}
        </div>
      )}

      <div className="bg-gray-50 p-4 rounded-xl shadow">
        <h2 className="font-semibold text-lg mb-2">Original Input:</h2>
        <p>{input}</p>
      </div>

      <div className="bg-gray-50 p-4 rounded-xl shadow">
        <h2 className="font-semibold text-lg mb-2">Generated SQL:</h2>
        <code className="block whitespace-pre-wrap">{sql}</code>
      </div>

      {result && (
        <div className="bg-gray-50 p-4 rounded-xl shadow overflow-auto">
          <h2 className="font-semibold text-lg mb-2">Query Result:</h2>
          <table className="min-w-full border-collapse table-auto">
            <thead>
              <tr>
                {Object.keys(result[0] || {}).map((key) => (
                  <th key={key} className="border px-4 py-2 text-left bg-gray-200">{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {result.map((row, idx) => (
                <tr key={idx} className="hover:bg-gray-100">
                  {Object.values(row).map((value, i) => (
                    <td key={i} className="border px-4 py-2">{value}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
