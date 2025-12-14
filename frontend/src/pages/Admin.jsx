
import { useState } from "react";
import api from "../api";

export default function Admin() {
  const [form, setForm] = useState({ name:"", category:"", price:0, quantity:0 });

  const submit = async e => {
    e.preventDefault();
    await api.post("/api/sweets", form);
    alert("Sweet added");
  };

  return (
    <form onSubmit={submit}>
      <h2>Admin Panel</h2>
      <input placeholder="Name" onChange={e=>setForm({...form,name:e.target.value})} />
      <input placeholder="Category" onChange={e=>setForm({...form,category:e.target.value})} />
      <input type="number" placeholder="Price" onChange={e=>setForm({...form,price:e.target.value})} />
      <input type="number" placeholder="Quantity" onChange={e=>setForm({...form,quantity:e.target.value})} />
      <button>Add Sweet</button>
    </form>
  );
}
