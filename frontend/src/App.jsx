import { useState } from 'react'
import axios from 'axios'

function App() {
    const [query, setQuery] = useState('')
    const [mode, setMode] = useState('hybrid')
    const [results, setResults] = useState([])
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const API_URL = import.meta.env.VITE_API_URL || '/api'

    const handleSearch = async (e) => {
        e.preventDefault()
        if (!query.trim()) return

        setLoading(true)
        setError(null)
        setResults([])
        try {
            const response = await axios.get(`${API_URL}/search`, {
                params: { q: query, mode: mode }
            })
            setResults(response.data)
        } catch (err) {
            console.error(err)
            setError('Failed to fetch results. Ensure backend is running.')
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="min-h-screen bg-gray-100 py-10 px-4 sm:px-6 lg:px-8">
            <div className="max-w-4xl mx-auto">
                <header className="text-center mb-10">
                    <h1 className="text-4xl font-extrabold text-blue-600 mb-2">Hybrid Search Demo</h1>
                    <p className="text-gray-600">Powered by FastAPI, React, PGVector & Supabase</p>
                </header>

                <div className="bg-white shadow-xl rounded-lg p-6 mb-8">
                    <form onSubmit={handleSearch} className="flex flex-col gap-4">
                        <div className="relative">
                            <input
                                type="text"
                                className="w-full p-4 pl-5 text-lg border-2 border-gray-200 rounded-lg focus:outline-none focus:border-blue-500 transition-colors"
                                placeholder="Search documents... (e.g., 'unit testing benefits', 'solar power')"
                                value={query}
                                onChange={(e) => setQuery(e.target.value)}
                            />
                        </div>

                        <div className="flex items-center justify-between">
                            <div className="flex items-center space-x-4">
                                <label className="font-medium text-gray-700">Search Mode:</label>
                                <div className="flex bg-gray-100 p-1 rounded-md">
                                    {['keyword', 'semantic', 'hybrid'].map((m) => (
                                        <button
                                            key={m}
                                            type="button"
                                            onClick={() => setMode(m)}
                                            className={`px-4 py-2 rounded-md capitalize font-medium transition-all ${mode === m
                                                ? 'bg-white text-blue-600 shadow-sm'
                                                : 'text-gray-500 hover:text-gray-700'
                                                }`}
                                        >
                                            {m}
                                        </button>
                                    ))}
                                </div>
                            </div>

                            <button
                                type="submit"
                                disabled={loading}
                                className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-8 rounded-lg shadow-md transition-transform transform active:scale-95 disabled:opacity-50"
                            >
                                {loading ? 'Searching...' : 'Search'}
                            </button>
                        </div>
                    </form>
                </div>

                {error && (
                    <div className="bg-red-50 text-red-700 p-4 rounded-lg mb-6 text-center">
                        {error}
                    </div>
                )}

                <div className="space-y-4">
                    {results.map((result) => (
                        <div key={result.id} className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow border-l-4 border-blue-500">
                            <div className="flex justify-between items-start mb-2">
                                <h3 className="text-xl font-bold text-gray-800">{result.title}</h3>
                                <div className="text-xs font-mono bg-blue-50 text-blue-700 px-2 py-1 rounded">
                                    Score: {result.score.toFixed(4)}
                                </div>
                            </div>
                            <p className="text-gray-600 mb-4">{result.body}</p>

                            <div className="flex gap-4 text-xs text-gray-400 font-mono border-t pt-2 mt-2">
                                {mode !== 'semantic' && (
                                    <span>FTS Rank: {result.fts_score ? result.fts_score.toFixed(4) : 'N/A'}</span>
                                )}
                                {mode !== 'keyword' && (
                                    <span>Vector Sim: {result.sem_score ? result.sem_score.toFixed(4) : 'N/A'}</span>
                                )}
                            </div>
                        </div>
                    ))}

                    {!loading && results.length === 0 && query && !error && (
                        <div className="text-center text-gray-500 mt-10">No results found.</div>
                    )}
                </div>
            </div>
        </div>
    )
}

export default App
