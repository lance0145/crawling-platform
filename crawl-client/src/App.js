import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [source, setSource] = useState('fmoviesz.to');

  const searchWorks = async () => {
    const response = await axios.get(`http://localhost:8000/api/works/?title=${query}&source=${source}`);
    setResults(response.data);
  };

  return (
    <div className="App">
      <h1>Search Creative Works</h1>
      <input 
        type="text" 
        value={query} 
        onChange={(e) => setQuery(e.target.value)} 
        placeholder="Enter title..." 
      />
      <select value={source} onChange={(e) => setSource(e.target.value)}>
        <option value="fmoviesz.to">fmoviesz.to</option>
        <option value="gogoflix.shop">gogoflix.shop</option>
      </select>
      <button onClick={searchWorks}>Search</button>
      <ul>
        {results.map(work => (
          <li key={work.id}>
            <a href={work.page_link} target="_blank" rel="noopener noreferrer">{work.title}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
