
export default function SearchBar({ onSearch }) {
  return (
    <div>
      <input placeholder="Name" onChange={e=>onSearch("name", e.target.value)} />
      <input placeholder="Category" onChange={e=>onSearch("category", e.target.value)} />
    </div>
  );
}
