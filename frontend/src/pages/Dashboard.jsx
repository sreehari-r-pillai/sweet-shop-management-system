
import { useContext, useEffect, useState } from "react";
import api from "../api";
import SweetCard from "../components/SweetCard";
import SearchBar from "../components/SearchBar";
import { AuthContext } from "../context/AuthContext";

export default function Dashboard() {
  const { user } = useContext(AuthContext);
  const [sweets, setSweets] = useState([]);
  const [query, setQuery] = useState({});

  const load = async () => {
    const res = await api.get("/api/sweets/search", { params: query });
    setSweets(res.data);
  };

  useEffect(()=>{ load(); }, [query]);

  return (
    <>
      <h2>Sweet Shop</h2>
      <SearchBar onSearch={(k,v)=>setQuery({...query,[k]:v})} />

      {sweets.map(s => (
        <SweetCard
          key={s.id}
          sweet={s}
          isAdmin={user?.role === "ADMIN"}
          onPurchase={id=>api.post(`/api/sweets/${id}/purchase`).then(load)}
          onDelete={id=>api.delete(`/api/sweets/${id}`).then(load)}
        />
      ))}
    </>
  );
}
