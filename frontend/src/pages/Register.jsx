
import { useState } from "react";
import api from "../api";

export default function Register() {
  const [form, setForm] = useState({ username: "", password: "" });

  const submit = async e => {
    e.preventDefault();
    await api.post("/api/auth/register", form);
    alert("Registered");
  };

  return (
    <form onSubmit={submit}>
      <h2>Register</h2>
      <input placeholder="Username" onChange={e=>setForm({...form,username:e.target.value})} />
      <input type="password" placeholder="Password" onChange={e=>setForm({...form,password:e.target.value})} />
      <button>Register</button>
    </form>
  );
}
